#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2024-04-29 9:37
# describe：
import base64
import hashlib
from io import BytesIO

import requests
from PIL import Image

from models.m_ocr import ImgDownloadModel
from utils import u_file, u_ua

# 图片临时存储目录
TEMP_IMG_DIR = f'{u_file.project_dir}/.cache'


# 保存图片
def save_img(value, option: ImgDownloadModel = None) -> str:
    if str(value).startswith("http"):
        # 处理图片链接格式
        return download_image(value, option)
    else:
        # 处理base64
        return save_base64_to_image(value)


# 下载图片
def download_image(url, option: ImgDownloadModel = None) -> str:
    try:
        img_path = _get_img_path(url)

        if not option:
            option = ImgDownloadModel()

        # 组装代理
        proxy_url = option.proxy_url
        proxies = {"http": proxy_url, "https": proxy_url}

        # 组装headers
        headers = {'User-Agent': u_ua.random_one()}
        for k, v in (option.headers or {}).items():
            headers[k] = v

        # 下载超时时间
        timeout = option.timeout or 20

        response = requests.get(url, timeout=timeout, proxies=proxies, headers=headers)
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(response.content)
            return img_path
        else:
            return None
    except Exception as e:
        return None


def save_base64_to_image(base64_str):
    """
    保存图片的base64到文件
        注意，这里的base64不要传前缀，例如：data:image/png;base64,
        默认这里做兜底处理，自动移除 data:image/png;base64,
    """
    try:
        if ";base64," in base64_str:
            base64_str = base64_str.split(";base64,")[1]
        img_path = _get_img_path(base64_str)
        image_data = base64.b64decode(base64_str)
        image = Image.open(BytesIO(image_data))
        image.save(img_path)
        return img_path
    except Exception as e:
        return None


# 根据 url/base64的字符 转为目标保存路径
def _get_img_path(value) -> str:
    u_file.makedirs(TEMP_IMG_DIR)
    return f"{TEMP_IMG_DIR}/{_gen_md5(value)}.jpg"


# 生成md5
def _gen_md5(v) -> str:
    return hashlib.md5(str(v).encode('utf-8')).hexdigest() if v else None


if __name__ == '__main__':
    base64_str = "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"
    save_base64_to_image(base64_str)
    print("all done")

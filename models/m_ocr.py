#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 15:11
# describe：
from typing import Optional

from pydantic import BaseModel


class ImgDownloadModel(BaseModel):
    """图片下载参数"""
    headers: Optional[dict] = None    # 下载图片需要的自定义header => {"a1":"xxx", "a2":"xxx"}
    cookies: Optional[dict] = None    # 下载图片需要的自定义cookie => {"a1":"xxx"}，可选，如果headers中配置Cookie字段的话，该配置会被忽略
    proxy_url: Optional[str] = None   # 代理ip
    timeout: Optional[int] = 20       # 下载超时时间


class OcrRequest(BaseModel):
    """ocr请求体"""
    lst: list                                    # 图片列表 / 图片的base64列表 混合列表
    need_kv: Optional[bool] = False              # 是否需要返回键值对信息，如果为true，则会用 传入值+识别结果 作为键值对返回，方便对照识别结果，否则仅返回识别结果
    option: Optional[ImgDownloadModel] = None    # 图片链接下载的额外参数，可选

#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 14:56
# describe：
import json
import os

import uvicorn
from fastapi import Depends, FastAPI, Header

from models.m_ocr import OcrRequest
from utils import u_file, u_http, u_img, u_ocr

# api的简易token验证
access_token = os.environ.get('ACCESS_TOKEN') or json.loads(u_file.read('config.json') or '{}').get('access_token')


async def verify_token(authorization: str = Header(None)):
    """ token简易验证 """
    if not access_token:
        return
    if authorization != f"Bearer {access_token}":
        print(f"认证失败：{authorization}")
        u_http.fail403(msg='authorization header invalid')


app = FastAPI(dependencies=[Depends(verify_token)])


@app.post("/api/ocr")
async def ocr_post(request: OcrRequest):
    lst = request.lst or []
    if not lst:
        return u_http.fail400()

    # 遍历参数列表，解析图片中的数字并返回
    result_list = []
    for txt in lst:
        temp_img_path = u_img.save_img(txt, request.option)
        result = u_ocr.inference(temp_img_path)
        u_file.remove(temp_img_path)  # 处理完毕后删除临时图片
        if not result:
            continue
        if request.need_kv:
            result_list.append({
                "key": txt,
                "value": result
            })
        else:
            result_list.append(result)

    return u_http.success(result_list)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=1)

#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2024-04-29 9:58
# describe：
import os

from paddleocr import PaddleOCR

ocr_instance = None


def get_ocr_instance():
    global ocr_instance
    if ocr_instance:
        return ocr_instance
    ocr_instance = PaddleOCR(det=False, use_gpu=False)
    return ocr_instance


# 识别图片中的数字
def inference(img_path) -> str:
    if not img_path or not os.path.exists(img_path):
        return None
    try:
        result = get_ocr_instance().ocr(img_path, cls=True)
        return result[0][0][1][0]
    except Exception as e:
        return None

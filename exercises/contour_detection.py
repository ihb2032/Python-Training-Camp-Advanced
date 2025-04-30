# exercises/contour_detection.py
"""
练习：轮廓检测

描述：
使用 OpenCV 检测图像中的轮廓并将其绘制出来。

请补全下面的函数 `contour_detection`。
"""
import cv2
import numpy as np

def contour_detection(image_path):
    """
    使用 OpenCV 检测图像中的轮廓
    参数:
        image_path: 图像路径
    返回:
        tuple: (绘制轮廓的图像, 轮廓列表) 或 (None, None) 失败时
    """
    # 请在此处编写代码
    # 提示：
    try:
        image = cv2.imread(image_path)
        if image is None:
            return None, None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        result = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(result) == 2:
            contours, hierarchy = result
        elif len(result) == 3:
            _, contours, hierarchy = result
        else:
            raise ValueError("")
        img_copy = image.copy()
        cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)
        if not isinstance(contours, list):
            contours = list(contours)
        return img_copy, contours
    except Exception:
        return None, None
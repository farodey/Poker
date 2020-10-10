import numpy as np
import cv2
from PIL import Image, ImageGrab


def hash_image(image, ycard, xcard, y, x):

    # вырезаем карту
    roi_image = image[ycard:ycard + y, xcard:xcard + x]

    # уменьшаем разрешение  до 8х8
    resize_image = cv2.resize(roi_image, (8, 8))

    # переводим в градации серого
    gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

    # бинаризуем картинку (254 - пороговая величина)
    th, bin_image = cv2.threshold(gray_image, 254, 255, cv2.THRESH_BINARY)

    i = 0
    hash = 0
    for y in range(8):
        for x in range(8):
            # 0xff - белый пиксель
            if bin_image[y, x] == 0xff:
                hash = hash | 1 << i
            else:
                pass
            i += 1
    return hash


pil_image = Image.open("C:\\Users\\farodey\Desktop\\screen.bmp")
open_cv_image = np.array(pil_image)
open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)

print(hash_image(open_cv_image, 248, 326, 21, 14))
print("{0:b}".format(hash_image(open_cv_image, 248, 326, 21, 14)))








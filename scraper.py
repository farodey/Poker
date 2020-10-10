import cv2
import numpy as np
from PIL import Image, ImageGrab


class Scraper:

    def __init__(self):
        pass

    def screen(self):
        pil_image = Image.open("C:\\Users\\farodey\Desktop\\9.bmp")
        # pil_image = ImageGrab.grab()
        open_cv_image = np.array(pil_image)
        self.open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)
        # self.open_cv_image = open_cv_image[:, :, ::-1].copy()

    def fold(self):
        x = 494
        y = 632
        r = 128
        g = 24
        b = 15
        if self.open_cv_image[y, x][0] == b and self.open_cv_image[y, x][1] == g and self.open_cv_image[y, x][2] == r:
            return True
        return False

    def round(self):
        y = 100
        x_flop = 100
        x_tern = 100
        x_river = 100
        r = 100
        g = 100
        b = 100
        if self.pix[x_river, y][0] == r and self.pix[x_river, y][1] == g and self.pix[x_river, y][2] == b:
            return 'river'
        elif self.pix[x_tern, y][0] == r and self.pix[x_tern, y][1] == g and self.pix[x_tern, y][2] == b:
            return 'tern'
        elif self.pix[x_flop, y][0] == r and self.pix[x_flop, y][1] == g and self.pix[x_flop, y][2] == b:
            return 'flop'
        return 'prerflop'

    def pot(self):
        pass

    def play(self):
        pass

    def player(self):
        pass

    def call(self):
        pass

    def card(self, ncard):

        dict_yx_card = {1: (440, 423), 2: (440, 483), 3: (248, 326), 4: (248, 389), 5: (248, 453), 6: (248, 517), 7: (248, 580)}
        dict_hash = {9908455741284147968: 'Kc', 11061377245890996992: 'Ks'}
        print(self.hash_image(dict_yx_card[ncard], 38, 15))
        return dict_hash[self.hash_image(dict_yx_card[ncard], 38, 15)]

    # перцептивный хэш
    def hash_image(self, yx_card, y, x):

        # вырезаем картинку
        roi_image = self.open_cv_image[yx_card[0]:yx_card[0] + y, yx_card[1]:yx_card[1] + x]

        # уменьшаем разрешение  до 8х8
        resize_image = cv2.resize(roi_image, (8, 8))

        # переводим в градации серого (убираем цвет)
        gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

        # Находим среднее значение всех цветов
        result = 0
        for y in range(8):
            for x in range(8):
                result += gray_image[y, x]
        average_color = result // 64

        # бинаризуем картинку (average_color - пороговая величина)
        th, bin_image = cv2.threshold(gray_image, average_color, 255, cv2.THRESH_BINARY)

        # переводим картинку в одно 64 битное значение
        i = 0
        hash = 0
        for y in range(8):
            for x in range(8):
                # 0xff - белый пиксель, 0x00 - черный пиксель
                if bin_image[y, x] == 0xff:
                    # устанавливаем бит
                    hash = hash | 1 << i
                else:
                    pass
                i += 1
        return hash



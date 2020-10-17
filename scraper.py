import cv2
import numpy as np
from PIL import Image, ImageGrab


class Scraper:

    def __init__(self):
        pass

    def screen(self):
        pil_image = Image.open("C:\\Users\\farodey\Desktop\\card\\12.bmp")
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
        y = 250
        x_flop = 505
        x_tern = 569
        x_river = 632
        b, g, r, = 255, 255, 255

        if self.open_cv_image[y, x_river][0] == b and self.open_cv_image[y, x_river][1] == g and \
                self.open_cv_image[y, x_river][2] == r:
            return 'river'
        elif self.open_cv_image[y, x_tern][0] == b and self.open_cv_image[y, x_tern][1] == g and \
                self.open_cv_image[y, x_tern][2] == r:
            return 'tern'
        elif self.open_cv_image[y, x_flop][0] == b and self.open_cv_image[y, x_flop][1] == g and \
                self.open_cv_image[y, x_flop][2] == r:
            return 'flop'
        return 'prerflop'

    def dealer(self):
        dict_yx_dealer = {(437, 401): 1, (360, 254): 2, (268, 197): 3, (210, 302): 4, (168, 450): 5,
                          (210, 302): 6, (185, 634): 7, (234, 731): 8, (405, 652): 9}
        dict_color_dealer = {1: (209, 208, 215), 2: (209, 208, 218), 3: (211, 210, 213), 4: (211, 211, 215),
                             5: (211, 211, 211),
                             6: (209, 209, 215), 7: (213, 212, 218), 8: (211, 211, 211), 9: (210, 209, 216)}
        for i in dict_yx_dealer:
            if self.open_cv_image[i[0], i[1]][0] == dict_color_dealer[dict_yx_dealer[i]][0] and \
                    self.open_cv_image[i[0], i[1]][1] == dict_color_dealer[dict_yx_dealer[i]][1] and \
                    self.open_cv_image[i[0], i[1]][2] == dict_color_dealer[dict_yx_dealer[i]][2]:
                return dict_yx_dealer[i]
        return 0

    def pot(self):
        result = ''
        dict_char_hash = {309553956955398600580: '$', 554934618370219230: '0', 87: '.', 613566782: '1', 1135778769991306334: '2',
                          572100141243305055: '3', 572381599337550079: '5', 554934618671034812: '6', 109230716780480575: '7',
                          554934610808413406: '8', 277184749741939934: '9'}

        # Вырезаем изображение
        roi_image_pot = self.open_cv_image[226:242, 481:519]

        # Переводим в градации серого
        gray_image_pot = cv2.cvtColor(roi_image_pot, cv2.COLOR_BGR2GRAY)

        # Бинаризуем изображение, 140 - пороговая величина
        th, bin_image_pot = cv2.threshold(gray_image_pot, 140, 255, cv2.THRESH_BINARY)

        cv2.imwrite('bin_image_pot.png', bin_image_pot)

        x = 0
        while(True):
            cv2.imwrite('temp.png', bin_image_pot[:, x:])
            success, x_image = self.x_roi(bin_image_pot[:, x:])
            cv2.imwrite('x_image.png', x_image)
            if not success:
                break
            success, w_image = self.w_roi(x_image)
            cv2.imwrite('w_image.png', w_image)
            if not success:
                break
            success, y_image = self.y_roi(w_image)
            cv2.imwrite('y_image.png', y_image)
            if not success:
                break
            success, h_image = self.h_roi(y_image)
            cv2.imwrite('y_image.png', y_image)
            if not success:
                break

            cv2.imwrite('char.png', h_image)
            hash_char = self.bin_image_to_int(h_image)
            print(hash_char)
            result += dict_char_hash[hash_char]
            x = bin_image_pot.shape[1] - x_image.shape[1] + w_image.shape[1]

        return float(result[1:])

    # Поиск начала первого символа, отсекает лишнюю область слева  ->|....
    def x_roi(self, image):
        height, width = image.shape
        for x in range(width):
            for y in range(height):
                if image[y, x] == 0xff:
                    return True, image[:, x:]
        return False, image

    # Поиск ширины символа, отсечение области справа  ....|<-
    def w_roi(self, image):
        height, width = image.shape
        for x in range(12):
            bel = False
            for y in range(height):
                if image[y, x] == 0xff:
                    bel = True
                    break
            if not bel:
                return True, image[:, :x]
        return False, image  # Ошибка

    # Поиск начала символа сверху, отсечение области сверху
    def y_roi(self, image):
        height, width = image.shape
        for y in range(height):
            for x in range(width):
                if image[y, x] == 0xff:
                    return True, image[y:, :]
        return False, image

    # Поиск высоты символа, отсечение области снизу
    def h_roi(self, image):
        height, width = image.shape
        for y in range(height):
            bel = False
            for x in range(width):
                if image[y, x] == 0xff:
                    bel = True
                    break
            if not bel:
                return True, image[:y, :]
        return False, image

    def player(self):
        pass

    def call(self):
        pass

    def card(self, ncard):

        dict_yx_card = {1: (440, 423), 2: (440, 483), 3: (248, 326), 4: (248, 389), 5: (248, 453), 6: (248, 517),
                        7: (248, 580)}
        dict_hash = {9908455741284147968: 'Kc', 11061377245890996992: 'Ks', 16681869581184787439: '4d',
                     9331994987918785985: '5c',
                     9331994989483760833: '2c', 9331994988706372035: 'Qc', 11061377245224645764: 'Ts',
                     16681869580849376000: 'Kd',
                     14087783001091989383: 'Jh', 9908455741310876865: '9c', 16681869581319393152: '7d',
                     14087783000299273665: '5h',
                     16681869579781138304: '3d', 14087783001074817987: 'Qh', 9908455740238585283: '8c',
                     11061377245638549383: 'Js',
                     11061377245317490115: '6s', 11061377244781601767: 'As', 14087783000770930115: '6h'}
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
                i += 1
        return hash

    def bin_image_to_int(self, image):
        i = 0
        hash = 0
        height, width = image.shape
        for y in range(height):
            for x in range(width):
                # 0xff - белый пиксель, 0x00 - черный пиксель
                if image[y, x] == 0xff:
                    # устанавливаем бит
                    hash = hash | 1 << i
                i += 1
        return hash

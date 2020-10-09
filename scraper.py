import cv2
from PIL import Image, ImageGrab


class Scraper:

    def screen(self):
        # self.image = ImageGrab.grab()
        self.image = Image.open("C:\\Users\\farodey\Desktop\\screen.bmp")
        self.pix = self.image.load()

    def fold(self):
        x = 100
        y = 100
        r = 5
        g = 5
        b = 6
        if self.pix[x, y][0] == r and self.pix[x, y][1] == g and self.pix[x, y][2] == b:
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
        if ncard == 1:
            xmast, ymast, xcard, ycard = 372, 405, 367, 382

        elif ncard == 2:
            xmast, ymast, xcard, ycard = 387, 409, 382, 386

        elif ncard == 3:
            self.xmast, self.ymast, self.xcard, self.ycard = 280, 236, 275, 213

        elif ncard == 4:
            xmast, ymast, xcard, ycard = 334, 236, 329, 213

        elif ncard == 5:
            xmast, ymast, xcard, ycard = 388, 236, 383, 213

        elif ncard == 6:
            xmast, ymast, xcard, ycard = 442, 236, 437, 213

        elif ncard == 7:
            xmast, ymast, xcard, ycard = 496, 236, 491, 213

        self.im1 = self.image.crop((326, 248, 340, 270))
        self.im1.show()

        self.resize_image = self.image.resize(8, 8)
        self.resize_image.show()
        #self.grey_image = Image.greyscale(self.resize_image)
        #self.bin_image = self.grey_image.convert("1")
        #self.bin_image.show()





if __name__ == '__main__':
    scraper = Scraper()
    scraper.screen()
    scraper.fold()

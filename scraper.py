from PIL import Image, ImageGrab


class Scraper:

    def screen(self):
        image = ImageGrab.grab()
        # image.save("screen.bmp", "BMP")
        self.pix = image.load()

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
        pass

    def hash_card(self):
        cards = { }


if __name__ == '__main__':
    scraper = Scraper()
    scraper.screen()
    scraper.fold()

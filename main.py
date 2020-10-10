import sys
import time
from scraper import Scraper
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget


# поток эквилятора
class CalculateThread(QThread):
    def __init__(self, window):
        super(CalculateThread, self).__init__()
        self.scraper = Scraper()
        self.window = window

        self.calc_play = 0
        self.calc_pot = 0
        self.calc_round = 0

    def run(self):
        while(True):

            # Задержка для снижения нагрузки на систему
            time.sleep(1)

            # снимок экрана
            self.scraper.screen()

            print(self.scraper.card(2))

            # горит кнопка фолд
            # if self.scraper.fold():




# Окно программы
class PokerWindow(QWidget):
    def __init__(self):
        super(PokerWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1200, 200, 300, 300)
        self.setWindowTitle('Poker')
        self.show()

        # Запускаем поток эквилятора
        self.calculateThread = CalculateThread(window=self)
        self.calculateThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PokerWindow()
    window.show()
    sys.exit(app.exec())

import sys
import time
from scraper import Scraper
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


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

        # Расчитанная ситуация
        pot = 0
        round = 0
        dealer = 0

        while(True):

            # Задержка для снижения нагрузки на систему
            time.sleep(1)

            # снимок экрана
            self.scraper.screen()

            # горит кнопка
            if self.scraper.call_check():

                # для этой ситуации не выполнялся расчет
                if dealer != self.scraper.dealer() or round != self.scraper.round() or pot != self.scraper.pot():

                    # сигнал на обновление карт
                    self.window.c.showCard.emit([self.scraper.card(1), self.scraper.card(2)])

                    # Обновляем индикаторы обработанной ситуации, чтобы больше не расчитывать эту ситуацию
                    pot = self.scraper.pot()
                    round = self.scraper.round()
                    dealer = self.scraper.dealer()


class Communicate(QObject):
    showCard = pyqtSignal(list)


# Окно программы
class PokerWindow(QWidget):
    def __init__(self):
        super(PokerWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.showCard.connect(self.show_card)
        self.setGeometry(1200, 200, 300, 300)
        self.setWindowTitle('Poker')
        self.show()

        # Запускаем поток эквилятора
        self.calculateThread = CalculateThread(window=self)
        self.calculateThread.start()

    def show_card(self, list_card):

        list_pixmap = {}
        list_pixmap['Ad'] = QPixmap('card\\Ad.bmp')
        list_pixmap['Kd'] = QPixmap('card\\Kd.bmp')
        list_pixmap['Qd'] = QPixmap('card\\Qd.bmp')
        list_pixmap['Jd'] = QPixmap('card\\Jd.bmp')
        list_pixmap['Td'] = QPixmap('card\\Td.bmp')
        list_pixmap['9d'] = QPixmap('card\\9d.bmp')
        list_pixmap['8d'] = QPixmap('card\\8d.bmp')
        list_pixmap['7d'] = QPixmap('card\\7d.bmp')
        list_pixmap['6d'] = QPixmap('card\\6d.bmp')
        list_pixmap['5d'] = QPixmap('card\\5d.bmp')
        list_pixmap['4d'] = QPixmap('card\\4d.bmp')
        list_pixmap['3d'] = QPixmap('card\\3d.bmp')
        list_pixmap['2d'] = QPixmap('card\\2d.bmp')

        list_pixmap['Ah'] = QPixmap('card\\Ah.bmp')
        list_pixmap['Kh'] = QPixmap('card\\Kh.bmp')
        list_pixmap['Qh'] = QPixmap('card\\Qh.bmp')
        list_pixmap['Jh'] = QPixmap('card\\Jh.bmp')
        list_pixmap['Th'] = QPixmap('card\\Th.bmp')
        list_pixmap['9h'] = QPixmap('card\\9h.bmp')
        list_pixmap['8h'] = QPixmap('card\\8h.bmp')
        list_pixmap['7h'] = QPixmap('card\\7h.bmp')
        list_pixmap['6h'] = QPixmap('card\\6h.bmp')
        list_pixmap['5h'] = QPixmap('card\\5h.bmp')
        list_pixmap['4h'] = QPixmap('card\\4h.bmp')
        list_pixmap['3h'] = QPixmap('card\\3h.bmp')
        list_pixmap['2h'] = QPixmap('card\\2h.bmp')

        list_pixmap['As'] = QPixmap('card\\As.bmp')
        list_pixmap['Ks'] = QPixmap('card\\Ks.bmp')
        list_pixmap['Qs'] = QPixmap('card\\Qs.bmp')
        list_pixmap['Js'] = QPixmap('card\\Js.bmp')
        list_pixmap['Ts'] = QPixmap('card\\Ts.bmp')
        list_pixmap['9s'] = QPixmap('card\\9s.bmp')
        list_pixmap['8s'] = QPixmap('card\\8s.bmp')
        list_pixmap['7s'] = QPixmap('card\\7s.bmp')
        list_pixmap['6s'] = QPixmap('card\\6s.bmp')
        list_pixmap['5s'] = QPixmap('card\\5s.bmp')
        list_pixmap['4s'] = QPixmap('card\\4s.bmp')
        list_pixmap['3s'] = QPixmap('card\\3s.bmp')
        list_pixmap['2s'] = QPixmap('card\\2s.bmp')

        list_pixmap['Ac'] = QPixmap('card\\Ac.bmp')
        list_pixmap['Kc'] = QPixmap('card\\Kc.bmp')
        list_pixmap['Qc'] = QPixmap('card\\Qc.bmp')
        list_pixmap['Jc'] = QPixmap('card\\Jc.bmp')
        list_pixmap['Tc'] = QPixmap('card\\Tc.bmp')
        list_pixmap['9c'] = QPixmap('card\\9c.bmp')
        list_pixmap['8c'] = QPixmap('card\\8c.bmp')
        list_pixmap['7c'] = QPixmap('card\\7c.bmp')
        list_pixmap['6c'] = QPixmap('card\\6c.bmp')
        list_pixmap['5c'] = QPixmap('card\\5c.bmp')
        list_pixmap['4c'] = QPixmap('card\\4c.bmp')
        list_pixmap['3c'] = QPixmap('card\\3c.bmp')
        list_pixmap['2c'] = QPixmap('card\\2c.bmp')

        # список карт
        list_lbl = []
        for card in list_card:
            lbl = QLabel(self)
            lbl.setPixmap(list_pixmap[card])
            list_lbl.append(lbl)

        # горизонтальный макет
        hbox = QHBoxLayout()
        for lbl in list_lbl:
            hbox.addWidget(lbl)
        hbox.addStretch(1)

        # вертикальный макет
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # устанавливаем макет
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PokerWindow()
    window.show()
    sys.exit(app.exec())

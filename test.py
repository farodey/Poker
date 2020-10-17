from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        v_box = QtWidgets.QVBoxLayout(self)

        box = QtWidgets.QWidget()
        box.setStyleSheet(box_qss)
        box.setFixedHeight(50)
        h_box = QtWidgets.QHBoxLayout(box)
        v_box.addWidget(box)

        label_1 = QtWidgets.QLabel('label_1')
        h_box.addWidget(label_1)

        h_box.addSpacing(10)  # +++

        btn = QtWidgets.QPushButton('btn')
        btn.setStyleSheet(btn_qss)
        btn.setFixedSize(40, 30)
        h_box.addWidget(btn)  # , alignment = QtCore.Qt.AlignLeft)

        h_box.addStretch(1)  # +++

        label_2 = QtWidgets.QLabel('label_2')
        h_box.addWidget(label_2, alignment=QtCore.Qt.AlignRight)


box_qss = '''QWidget {
                      background-color: yellow;
                      border-radius: 5px;
                  }'''

btn_qss = '''QWidget {
                      background-color: white;
                      border-radius: 5px;
                  }'''

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle(' ')
    window.show()
    sys.exit(app.exec_())
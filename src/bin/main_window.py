import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Football Database")

        self.main_layout = QWidget.layout()

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()

import sys
import src.bin.main_window
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = src.bin.main_window.MainWindow()
    app.exec_()

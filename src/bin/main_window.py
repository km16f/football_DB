import sys
import src.bin.rankings
import PyQt5.QtWidgets as widget
from PyQt5.QtGui import QIcon, QPixmap, QFont
import PyQt5.QtCore


class MainWindow(widget.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Football Database")
        self.main_layout = widget.QVBoxLayout()
        self.main_label = widget.QLabel("LoneWolf's Football StatBook")
        self.main_label.setFont(QFont("Times", 18, QFont.Bold))
        self.m_image = widget.QLabel()
        self.map = QPixmap('wolfy.jpg')
        self.map = self.map.scaled(300,300, PyQt5.QtCore.Qt.KeepAspectRatio)
        self.m_image.setPixmap(self.map)
        self.power_ranks = widget.QPushButton("Power Rankings")


        self.main_layout.addWidget(self.main_label)
        self.main_layout.addWidget(self.m_image)
        self.main_layout.addWidget(self.power_ranks)
        self.setLayout(self.main_layout)

        self.show()

        self.power_ranks.clicked.connect(self.open_rankings)

    def open_rankings(self):
        self.rank = src.bin.rankings.Rankings()
        self.rank.show()


if __name__ == "__main__":
    app = widget.QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()

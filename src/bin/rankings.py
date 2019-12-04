import sys
import src.bin.util
from PyQt5.QtWidgets import QTableWidget, QWidget, QApplication, QVBoxLayout, QHeaderView
import PyQt5.QtGui


class Rankings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NFL Power Rankings")
        self.setGeometry(400,400,800,400)

        rankings = src.bin.util.get_rankings()

        self.main_layout = QVBoxLayout()
        self.rank_table = QTableWidget()
        self.rank_table.verticalHeader().setVisible(False)
        self.rank_table.setRowCount(len(rankings))
        self.rank_table.setColumnCount(5)
        self.rank_table.setHorizontalHeaderLabels(["Ranking", "Location", "Mascot_Name", "Wins", "Losses"])

        for r in rankings:
            print (r[4])



        header = self.rank_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

        self.main_layout.addWidget(self.rank_table)

        self.setLayout(self.main_layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Rankings()
    app.exec_()

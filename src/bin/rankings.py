import sys
import src.bin.util
from PyQt5.QtWidgets import QTableWidget, QWidget, QApplication, QVBoxLayout, QHeaderView, QTableWidgetItem
import PyQt5.QtGui


class Rankings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NFL Power Rankings")
        self.setGeometry(400,400,500,800)

        rankings = src.bin.util.get_rankings()

        self.main_layout = QVBoxLayout()
        self.rank_table = QTableWidget()
        self.rank_table.verticalHeader().setVisible(False)
        self.rank_table.setRowCount(0)
        self.rank_table.setColumnCount(5)
        self.rank_table.setHorizontalHeaderLabels(["Ranking", "Location", "Mascot_Name", "Wins", "Losses"])

        for row in rankings:
            num = self.rank_table.rowCount()
            self.rank_table.insertRow(num)
            self.rank_table.setItem(num, 0, QTableWidgetItem(str(row[4])))
            self.rank_table.setItem(num, 1, QTableWidgetItem(row[0]))
            self.rank_table.setItem(num, 2, QTableWidgetItem(row[1]))
            self.rank_table.setItem(num, 3, QTableWidgetItem(str(row[2])))
            self.rank_table.setItem(num, 4, QTableWidgetItem(str(row[3])))


        header = self.rank_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

        self.main_layout.addWidget(self.rank_table)

        self.setLayout(self.main_layout)
        self.show()


class AddTeam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Team")
        self.setGeometry(600, 200, 200, 200)

        self.main_layout1 = QVBoxLayout()


class BadTeams(QWidget):
    print("butt")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Rankings()
    app.exec_()

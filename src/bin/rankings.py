import sys
import src.bin.util
from PyQt5.QtWidgets import QTableWidget, QWidget, QApplication, QVBoxLayout, QHeaderView, QTableWidgetItem, QLineEdit, QPushButton, QHBoxLayout, QLabel
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

        self.submit = QPushButton("Submit")
        self.label1 = QLabel("Enter Team Location: ")
        self.label2 = QLabel("Enter Team Mascot: ")
        self.label3 = QLabel("Enter Team Wins: ")
        self.label4 = QLabel("Enter Team Losses: ")
        self.label5 = QLabel("Enter Team Rank: ")
        self.label6 = QLabel("Enter Division: ")

        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()

        self.h7.addWidget(self.submit)


        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.line6 = QLineEdit()

        self.h1.addWidget(self.label1)
        self.h1.addWidget(self.line1)

        self.h2.addWidget(self.label2)
        self.h2.addWidget(self.line2)

        self.h3.addWidget(self.label3)
        self.h3.addWidget(self.line3)

        self.h4.addWidget(self.label4)
        self.h4.addWidget(self.line4)

        self.h5.addWidget(self.label5)
        self.h5.addWidget(self.line5)

        self.h6.addWidget(self.label6)
        self.h6.addWidget(self.line6)


        self.main_layout1.addLayout(self.h1)
        self.main_layout1.addLayout(self.h2)
        self.main_layout1.addLayout(self.h3)
        self.main_layout1.addLayout(self.h4)
        self.main_layout1.addLayout(self.h5)
        self.main_layout1.addLayout(self.h6)
        self.main_layout1.addLayout(self.h7)

        self.setLayout(self.main_layout1)



    def submit(self):
        src.bin.util.insert_rankings(self.label1.text(), self.label2.text(), self.label3.text(), self.label4.text(), self.label5.text())
        src.bin.util.insert_team(self.label1.text(), self.label2.text(), self.label6.text())



class BadTeams(QWidget):
    print("butt")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Rankings()
    app.exec_()

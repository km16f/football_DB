import sys
import src.bin.util as util
from PyQt5.QtWidgets import QTableWidget, QWidget, QLabel, QApplication, QVBoxLayout, QHeaderView, QTableWidgetItem, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont


class OStats(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Offensive Statistics")
        self.setGeometry(400,400,700,400)

        self.main_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.prompt = QLabel("Enter Team Mascot Name")
        self.line_edit = QLineEdit()

        self.o_table = QTableWidget()
        self.o_table.verticalHeader().setVisible(False)
        self.o_table.setRowCount(0)
        self.o_table.setColumnCount(5)
        self.o_table.setHorizontalHeaderLabels(["Name", "Total Yards", "Pass Yards", "Rush Yards", "TD"])

        header = self.o_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)


        # # self.o_table.hide()

        self.h_layout.addWidget(self.prompt)
        self.h_layout.addWidget(self.line_edit)
        self.main_layout.addLayout(self.h_layout)
        self.main_layout.addWidget(self.o_table)
        self.setLayout(self.main_layout)
        self.show()

        self.line_edit.returnPressed.connect(self.fill_table)

    def fill_table(self):
        name = self.line_edit.text()
        stats = util.get_offense(name)

        if len(stats) != 0:
            num = self.o_table.rowCount()
            self.o_table.insertRow(num)
            self.o_table.setItem(num, 0, QTableWidgetItem(stats[0][0]))
            self.o_table.setItem(num, 1, QTableWidgetItem(str(stats[0][1])))
            self.o_table.setItem(num, 2, QTableWidgetItem(str(stats[0][2])))
            self.o_table.setItem(num, 3, QTableWidgetItem(str(stats[0][3])))
            self.o_table.setItem(num, 4, QTableWidgetItem(str(stats[0][4])))


class FiveClub(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5000 Club!")
        self.setGeometry(600, 200, 400, 200)

        self.main_layout1 = QVBoxLayout()
        self.main_layout = QVBoxLayout()
        self.h_layout1 = QHBoxLayout()
        self.h_layout2 = QHBoxLayout()
        self.prompt = QLabel("5000 Club!")
        self.prompt.setFont(QFont("Arial", 20, QFont.Bold))
        self.subtext = QLabel("Teams with 5000 or more yards of total offense:")
        self.subtext.setFont(QFont("Arial", 12))



        self.main_layout1.addWidget(self.prompt)
        self.main_layout1.addWidget(self.subtext)
        self.main_layout.addLayout(self.main_layout1)
        self.main_layout.addStretch()


        r = util.get_5000()
        print(r[0][2])
        self.location = QLabel(r[0][0])
        self.name = QLabel(r[0][1])
        self.yards = QLabel(str(r[0][2]))

        self.str1 = QLabel("%s %s (%s)" % (r[0][0], r[0][1], str(r[0][2])))
        self.str1.setFont(QFont("Arial", 14))
        self.str2 = QLabel("%s %s (%s)" % (r[1][0], r[1][1], str(r[1][2])))
        self.str2.setFont(QFont("Arial", 14))


        self.main_layout.addWidget(self.str1)
        self.main_layout.addWidget(self.str2)

        self.setLayout(self.main_layout)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = OStats()
    app.exec_()

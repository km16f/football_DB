import sys
import src.bin.util as util
from PyQt5.QtWidgets import QTableWidget, QWidget, QLabel, QApplication, QVBoxLayout, QHeaderView, QTableWidgetItem, QLineEdit, QHBoxLayout
import PyQt5.QtGui


class DStats(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Defensive Statistics")
        self.setGeometry(400,400,700,400)

        self.main_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.prompt = QLabel("Enter Team Mascot Name")
        self.line_edit = QLineEdit()

        self.o_table = QTableWidget()
        self.o_table.verticalHeader().setVisible(False)
        self.o_table.setRowCount(0)
        self.o_table.setColumnCount(5)
        self.o_table.setHorizontalHeaderLabels(["Name", "Total Yards Allowed", "Pass Yards Allowed", "Rush Yards Allowed", "TD Allowed"])

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
        stats = util.get_defense(name)

        if len(stats) != 0:
            num = self.o_table.rowCount()
            self.o_table.insertRow(num)
            self.o_table.setItem(num, 0, QTableWidgetItem(stats[0][0]))
            self.o_table.setItem(num, 1, QTableWidgetItem(str(stats[0][1])))
            self.o_table.setItem(num, 2, QTableWidgetItem(str(stats[0][2])))
            self.o_table.setItem(num, 3, QTableWidgetItem(str(stats[0][3])))
            self.o_table.setItem(num, 4, QTableWidgetItem(str(stats[0][4])))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DStats()
    app.exec_()

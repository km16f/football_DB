import sys
import src.bin.util as util
import src.bin.rankings
import src.bin.offense_stats
import src.bin.defense_stats
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
        self.off_stats = widget.QPushButton("Offense Statistics")
        self.def_stats = widget.QPushButton("Defense Statistics")
        self.five_club = widget.QPushButton("5000 Club")
        self.add_team = widget.QPushButton("Add Team")
        self.compare = widget.QPushButton("Bad Teams")

        self.main_layout.addWidget(self.main_label)
        self.main_layout.addWidget(self.m_image)
        self.main_layout.addWidget(self.power_ranks)
        self.main_layout.addWidget(self.off_stats)
        self.main_layout.addWidget(self.def_stats)
        self.main_layout.addWidget(self.five_club)
        self.main_layout.addWidget(self.add_team)
        self.main_layout.addWidget(self.compare)
        self.setLayout(self.main_layout)

        self.show()

        self.power_ranks.clicked.connect(self.open_rankings)
        self.off_stats.clicked.connect(self.open_offense)
        self.def_stats.clicked.connect(self.open_defense)
        self.five_club.clicked.connect(self.print_five)
        self.add_team.clicked.connect(self.add_new_team)
        self.compare.clicked.connect(self.bad_teams)

    def open_rankings(self):
        self.rank = src.bin.rankings.Rankings()
        self.rank.show()

    def open_offense(self):
        self.offense = src.bin.offense_stats.OStats()
        self.offense.show()

    def open_defense(self):
        self.defense = src.bin.defense_stats.DStats()
        self.defense.show()

    def print_five(self):
        self.fiver = src.bin.offense_stats.FiveClub()
        self.fiver.show()

    def add_new_team(self):
        self.add = src.bin.rankings.AddTeam()
        self.add.show()

    def bad_teams(self):
        self.bad = src.bin.rankings.BadTeams
        self.bad.show()


if __name__ == "__main__":
    app = widget.QApplication(sys.argv)
    ex = MainWindow()
    app.exec_()

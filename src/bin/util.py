import sqlite3


conn = sqlite3.connect("football_DB")
c = conn.cursor()


def create_rankings():
    c.execute('''
    CREATE TABLE rankings (
    location VARCHAR(20),
    mascot_name VARCHAR(20) PRIMARY KEY,
    wins INTEGER,
    losses INTEGER,
    ranking INTEGER UNIQUE 
    )''')


def create_teams():
    c.execute('''
    CREATE TABLE teams (
    location VARCHAR(20),
    mascot_name VARCHAR(20) PRIMARY KEY,
    division VARCHAR (30)
    )''')


def create_offense_stats():
    c.execute('''
    CREATE TABLE o_stats (
    mascot_name VARCHAR(20) PRIMARY KEY,
    total_yards INTEGER,
    pass_yards INTEGER,
    rush_yards INTEGER,
    TD INTEGER 
    )''')


def create_defense_stats():
    c.execute('''
    CREATE TABLE d_stats (
    mascot_name PRIMARY KEY,
    yards_allowed INTEGER,
    pass_yards INTEGER,
    rush_yards INTEGER,
    TD INTEGER 
    )''')


def insert_team(l,m,d):
    c.execute('''INSERT INTO teams (location, mascot_name, division) VALUES (?,?,?)''', (l,m,d))
    conn.commit()

def get_teams():
    c.execute("SELECT * FROM teams")
    return c.fetchall()

def delete_team():
    c.execute("DROP TABLE teams")

def delete_ranking():
    c.execute("DROP TABLE rankings")


def insert_rankings(l, m, w, loss, r):
    c.execute(''' INSERT INTO rankings (location, mascot_name, wins, losses, ranking) VALUES (?,?,?,?,?)''', (l, m, w, loss, r))
    conn.commit()


def change_ranking(m, r):
    c.execute('''UPDATE rankings 
    SET ranking=?
    WHERE mascot_name=?
    ''', (r, m))
    conn.commit()


def get_rankings():
    c.execute("SELECT * FROM rankings ORDER BY ranking ASC")
    return c.fetchall()


def remove_from_rankings(name):
    c.execute("DELETE FROM rankings WHERE location=?", name)
    conn.commit()


def initialize_teams():
    insert_team("Baltimore", "Ravens", "AFC North")
    insert_team("New Orleans", "Saints", "NFC South")
    insert_team("Seattle", "Seahawks", "NFC West")
    insert_team("San Francisco", "49ers", "NFC West")
    insert_team("New England", "Patriots", "AFC East")
    insert_team("Green Bay", "Packers", "NFC North")
    insert_team("Minnesota", "Vikings", "NFC North")
    insert_team("Buffalo", "Bills", "AFC East")
    insert_team("Houston", "Texans","AFC South")
    insert_team("Kansas City", "Chiefs", "AFC West")
    insert_team("Tennessee", "Titans", "AFC South")
    insert_team("Pittsburgh", "Steelers", "AFC North")
    insert_team("Indianapolis", "Colts", "AFC South")
    insert_team("Dallas", "Cowboys", "NFC East")
    insert_team("L.A.", "Rams", "NFC West")
    insert_team("Philadelphia", "Eagles",  "NFC East")
    insert_team("Chicago", "Bears", "NFC North")
    insert_team("Oakland", "Raiders", "AFC West")
    insert_team("Tampa Bay", "Buccaneers","NFC South")
    insert_team("Cleveland", "Browns", "AFC North")
    insert_team("Carolina", "Panthers", "NFC South")
    insert_team("Denver", "Broncos", "AFC West")
    insert_team("L.A.", "Chargers", "AFC West")
    insert_team("Arizona", "Cardinals", "NFC West")
    insert_team("New York", "Jets", "AFC East")
    insert_team("Jacksonville", "Jaguars", "AFC South")
    insert_team("Washington", "Redskins",  "NFC East")
    insert_team("Atlanta", "Falcons", "NFC South")
    insert_team("Miami", "Dolphins", "AFC East")
    insert_team("Detroit", "Lions", "NFC North")
    insert_team("New York", "Giants",  "NFC East")
    insert_team("Cincinnati", "Bengals", "AFC North")


def initialize_rankings():
    insert_rankings("Baltimore", "Ravens", 10, 2, 1)
    insert_rankings("New Orleans", "Saints", 10, 2, 2)
    insert_rankings("Seattle", "Seahawks", 10, 2, 3)
    insert_rankings("San Francisco", "49ers", 10, 2, 4)
    insert_rankings("New England", "Patriots", 10, 2, 5)
    insert_rankings("Green Bay", "Packers", 9, 3, 6)
    insert_rankings("Minnesota", "Vikings", 8, 4, 7)
    insert_rankings("Buffalo", "Bills", 9, 3, 8)
    insert_rankings("Houston", "Texans", 8, 4, 9)
    insert_rankings("Kansas City", "Chiefs", 8, 4, 10)
    insert_rankings("Tennessee", "Titans", 7, 5, 11)
    insert_rankings("Pittsburgh", "Steelers", 7, 5, 12)
    insert_rankings("Indianapolis", "Colts", 6, 6, 13)
    insert_rankings("Dallas", "Cowboys", 6, 6, 14)
    insert_rankings("L.A.", "Rams", 7, 5, 15)
    insert_rankings("Philadelphia", "Eagles", 5, 7, 16)
    insert_rankings("Chicago", "Bears", 6, 6, 17)
    insert_rankings("Oakland", "Raiders", 6, 6, 18)
    insert_rankings("Tampa Bay", "Buccaneers", 5, 7, 19)
    insert_rankings("Cleveland", "Browns", 5, 7, 20)
    insert_rankings("Carolina", "Panthers", 5, 7, 21)
    insert_rankings("Denver", "Broncos", 4, 8, 22)
    insert_rankings("L.A.", "Chargers", 4, 8, 23)
    insert_rankings("Arizona", "Cardinals", 3, 8, 24)
    insert_rankings("New York", "Jets", 4, 8, 25)
    insert_rankings("Jacksonville", "Jaguars", 4, 8, 26)
    insert_rankings("Washington", "Redskins", 3, 9, 27)
    insert_rankings("Atlanta", "Falcons", 3, 9, 28)
    insert_rankings("Miami", "Dolphins", 3, 9, 29)
    insert_rankings("Detroit", "Lions", 3, 8, 30)
    insert_rankings("New York", "Giants", 2, 10, 31)
    insert_rankings("Cincinnati", "Bengals", 1, 11, 32)


if __name__ == "__main__":

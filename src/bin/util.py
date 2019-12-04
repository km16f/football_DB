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
    conn.commit()


def create_teams():
    c.execute('''
    CREATE TABLE teams (
    location VARCHAR(20),
    mascot_name VARCHAR(20) PRIMARY KEY,
    division VARCHAR (30)
    )''')
    conn.commit()


def create_offense_stats():
    c.execute('''
    CREATE TABLE o_stats (
    mascot_name VARCHAR(20) PRIMARY KEY,
    total_yards INTEGER,
    pass_yards INTEGER,
    rush_yards INTEGER,
    TD INTEGER 
    )''')
    conn.commit()


def create_defense_stats():
    c.execute('''
    CREATE TABLE d_stats (
    mascot_name VARCHAR(20) PRIMARY KEY,
    yards_allowed INTEGER,
    pass_yards INTEGER,
    rush_yards INTEGER,
    TD INTEGER 
    )''')
    conn.commit()


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
    c.execute("DELETE FROM rankings WHERE location=?", (name,))
    conn.commit()


def insert_offense(m, total, p, rush, td):
    c.execute('''INSERT INTO o_stats (mascot_name, total_yards, pass_yards, rush_yards, TD) VALUES (?,?,?,?,?)''', (m, total, p, rush, td))
    conn.commit()


def get_offense(name):
    c.execute('''SELECT * FROM o_stats WHERE mascot_name=?''', (name,))
    a = c.fetchall()
    return a


def get_5000():
    c.execute('''SELECT teams.location, teams.mascot_name, o_stats.total_yards 
    FROM o_stats, teams 
    WHERE teams.mascot_name = o_stats.mascot_name AND o_stats.total_yards >= 5000''')
    a = c.fetchall()
    return a


def insert_defense(m, total, p, rush, td):
    c.execute('''INSERT INTO d_stats (mascot_name, yards_allowed, pass_yards, rush_yards, TD) VALUES (?,?,?,?,?)''',
              (m, total, p, rush, td))
    conn.commit()


def get_defense(name):
    c.execute('''SELECT * FROM d_stats WHERE mascot_name=?''', (name,))
    a = c.fetchall()
    return a


def get_bad():
    c.execute('''SELECT o_stats.mascot_name,o_stats.total_yards, d_stats.yards_allowed FROM o_stats, d_stats WHERE o_stats.total_yards < d_stats.yards_allowed''')
    a = c.fetchall()
    return a

def initialize_defense():
    insert_defense("Ravens", 3881, 2742, 1139, 22)
    insert_defense("Saints", 3882, 2819, 1062, 28)
    insert_defense("Seahawks", 4427, 3232, 1195, 34)
    insert_defense("49ers", 3011, 1611, 1134, 20)
    insert_defense("Patriots", 3096, 1962, 1134, 17)
    insert_defense("Packers", 4521, 3045, 1476, 28)
    insert_defense("Vikings", 4169, 2915, 1254, 26)
    insert_defense("Bills", 3601, 2350, 1251, 23)
    insert_defense("Texans", 4488, 3155, 1333, 31)
    insert_defense("Chiefs", 4465, 2769, 1696, 31)
    insert_defense("Titans", 4345, 3121, 1224, 26)
    insert_defense("Steelers", 3086, 2562, 1244, 25)
    insert_defense("Colts", 3944, 2723, 1221, 28)
    insert_defense("Cowboys", 3859, 2582, 1277, 25)
    insert_defense("Rams", 3924, 2674, 1250, 29)
    insert_defense("Eagles", 3992, 2900, 1092, 34)
    insert_defense("Bears", 3836, 2666, 1170, 23)
    insert_defense("Raiders", 4341, 3098, 1243, 40)
    insert_defense("Buccaneers", 4297, 3382, 915, 38)
    insert_defense("Browns", 4047, 2559, 1488, 32)
    insert_defense("Panthers", 4400, 2750, 1650, 37)
    insert_defense("Broncos", 3891, 2572, 1364, 23)
    insert_defense("Chargers", 3711, 2392, 1319, 28)
    insert_defense("Cardinals", 5116, 3690, 1426, 42)
    insert_defense("Jets", 3809, 2906, 903, 32)
    insert_defense("Jaguars", 4325, 2686, 1639, 35)
    insert_defense("Redskins", 4337, 2758, 1579, 34)
    insert_defense("Falcons", 4418, 3114, 1304, 37)
    insert_defense("Dolphins", 4796, 3074, 1722, 43)
    insert_defense("Lions", 4777, 3361, 1416, 31)
    insert_defense("Giants", 4474, 3103, 1371, 40)
    insert_defense("Bengals", 4860, 2969, 1891, 32)


def initialize_offense():
    insert_offense("Ravens", 5049, 2555, 2494, 49 )
    insert_offense("Saints", 4337, 3049, 1288, 31 )
    insert_offense("Seahawks", 4683, 2959, 1724, 40)
    insert_offense("49ers", 4536, 2760, 1776, 41)
    insert_offense("Patriots", 4329, 3173, 1156, 38)
    insert_offense("Packers", 4080, 2863, 1217, 35)
    insert_offense("Vikings", 4519, 2874, 1645, 39)
    insert_offense("Bills", 4236, 2581, 1655, 30)
    insert_offense("Texans", 4474, 2916, 1558, 36)
    insert_offense("Chiefs", 4616, 3482, 1134, 39)
    insert_offense("Titans", 3957, 2452, 1505, 36)
    insert_offense("Steelers",3496, 2406, 1090, 24)
    insert_offense("Colts", 4025, 2475, 1668, 30)
    insert_offense("Cowboys", 5193, 3662, 1531, 36)
    insert_offense("Rams", 4435, 3305, 1130, 31)
    insert_offense("Eagles", 4108, 3089, 1438, 32)
    insert_offense("Bears", 3381, 2429, 952, 24)
    insert_offense("Raiders", 4257, 2785, 1485, 29)
    insert_offense("Buccaneers", 4565, 3410, 1155, 39)
    insert_offense("Browns", 4175, 2703, 1472, 27)
    insert_offense("Panthers", 4095, 2645, 1446, 32)
    insert_offense("Broncos", 3549, 2249, 1300, 19)
    insert_offense("Chargers", 4359, 3280, 1069, 25)
    insert_offense("Cardinals", 3981, 2612, 1379, 25)
    insert_offense("Jets", 3154, 2283, 871, 24)
    insert_offense("Jaguars", 4313, 2952, 1361, 21)
    insert_offense("Redskins", 3149, 1956, 1193,17)
    insert_offense("Falcons", 4433, 3542, 891, 29)
    insert_offense("Dolphins", 3323, 2570, 753, 24)
    insert_offense("Lions", 4527, 3260, 1267, 31)
    insert_offense("Giants", 3800, 2645, 1146, 29)
    insert_offense("Bengals", 3612, 2676, 936,18)

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

#
# if __name__ == "__main__":
#
import pandas as pd
import mysql.connector
import random
import detail
user_name = ""
user_id = ""
score = 0
num_correct = 0
mysql_connector = None
difficulty = 0
g_team_id = 0
lives = 10


def check():
    player = 19061
    full_employ_data = []
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT * FROM player WHERE id = '{player}';")
    player_data = cursor.fetchone()

    cursor.execute(f"SELECT * FROM employ Where player_id = {player_data[0]};")
    employ_data = cursor.fetchall()
    team_ids = [row[1] for row in employ_data]
    team_ids_str = ",".join(map(str, team_ids))
    cursor.execute(f"SELECT * FROM team WHERE id IN ({team_ids_str});")
    team_data = cursor.fetchall()




def set_game_difficulty(diff):
    global difficulty
    difficulty = diff


def get_lives():
    global lives
    return lives


def set_game_team(team):
    global g_team_id
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT * FROM team WHERE name = '{team}' LIMIT 1;")
    row = cursor.fetchone()
    if row is not None:
        g_team_id = row[0]
        return True
    return False


def get_mysql_connector():
    global mysql_connector
    if mysql_connector is None:
        mysql_connector = mysql.connector.connect(
          host="localhost",
          user="root",
          password="223333",
          database="guess_the_player"
        )
    return mysql_connector


"""
def get_mysql_connector():
    global mysql_connector
    if mysql_connector is None:
        mysql_connector = mysql.connector.connect(
            host="localhost",
            user="team03",
            password="0003",
            database="db03"
        )
    return mysql_connector
"""


def login(username, password):
    global user_name
    global user_id
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT * FROM user WHERE username = '{username}' and password = '{password}';")
    row = cursor.fetchone()
    if row is not None:
        user_name = row[1]
        user_id = username
        return True
    return False


def get_user_name():
    return user_name


def get_user_id():
    return user_id


def check_user_exist(username):
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT * FROM user WHERE username = '{username}' LIMIT 1;")
    row = cursor.fetchone()
    if row is None:
        return True
    return False


def insert_user(username, password, name):
    if check_user_exist(username):
        cursor = get_mysql_connector().cursor()
        user_query = "INSERT INTO user (username, name, password) VALUES (%s, %s, %s)"
        cursor.execute(user_query, (username, name, password))
        get_mysql_connector().commit()
        return True
    return False


def get_answers():
    cursor = get_mysql_connector().cursor()
    player = get_random_player()
    cursor.execute(f"SELECT distinct p.full_name FROM player as p, employ as e "
                   f"WHERE e.team_id = (select e.team_id from employ as e where e.player_id = '{player}' "
                   f"order by e.year desc limit 1) and p.id = e.player_id ORDER BY RAND() LIMIT 3;")
    rows = cursor.fetchall()
    return player, rows


def get_random_player():
    global g_team_id
    player_query = f"SELECT * FROM player AS p, employ AS e WHERE e.team_id = {g_team_id} and p.id = e.player_id ORDER BY RAND() LIMIT 1;"
    if g_team_id == 0:
        player_query = "SELECT * FROM player ORDER BY RAND() LIMIT 1;"
    cursor = get_mysql_connector().cursor()
    cursor.execute(player_query)
    row = cursor.fetchone()
    return row[0]


def get_team_players(team_name):
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT * FROM team WHERE name = '{team_name}';")
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.execute(f"SELECT DISTINCT player_id FROM employ WHERE team_id = '{row[0]}';")
    rows = cursor.fetchall()
    players = [r[0] for r in rows]
    return players


def get_player_max_score():
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT max(score) FROM games as g, play as p, user as u where u.username = '{get_user_id()}' "
                   f"and g.id = p.game_id;")
    row = (cursor.fetchone())[0]
    if row is None:
        return 0
    return row


def get_score():
    global score
    return score


def get_player_by_name(name):
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT id FROM player WHERE full_name = '{name}';")
    row = cursor.fetchone()
    if row is None:
        return None
    static, dynamic = get_player_data(row[0])
    return static, dynamic


def get_player_data(player):
    full_employ_data = []
    cursor = get_mysql_connector().cursor()
    cursor.execute(f"SELECT * FROM player WHERE id = '{player}';")
    player_data = cursor.fetchone()

    cursor.execute(f"SELECT * FROM employ Where player_id = {player_data[0]};")
    employ_data = cursor.fetchall()
    team_ids = [row[1] for row in employ_data]
    team_ids_str = ",".join(map(str, team_ids))
    cursor.execute(f"SELECT * FROM team WHERE id IN ({team_ids_str});")
    team_data = cursor.fetchall()

    league_ids = [row[2] for row in team_data]
    league_ids_str = ",".join(map(str, league_ids))
    cursor.execute(f"SELECT * FROM league WHERE id IN ({league_ids_str});")
    league_data = cursor.fetchall()
    for i in range(len(employ_data)):
        team = next((t for t in team_data if t[0] == employ_data[i][1]), None)
        league = next((l for l in league_data if l[0] == team[2]), None)
        full_employ_data.append(employ_data[i] + (team[1],) + (league[1],))

    return player_data, full_employ_data


def get_question(player_data, employ_data):
    global difficulty
    func_list = [easy_question, mid_question, hard_question]
    selected_function = func_list[difficulty]
    return selected_function(player_data, employ_data)


def easy_question(player_data, employ_data):
    if len(employ_data) == 1:
        func_list = [detail.give_detail_birth, detail.give_detail_current_team, detail.give_detail_money,
                     detail.give_detail_body, detail.give_detail_preform, detail.give_detail_shirt]
    else:
        func_list = [detail.give_detail_birth, detail.give_detail_current_team, detail.give_detail_money,
                     detail.give_detail_body, detail.give_detail_preform, detail.give_detail_shirt,
                     detail.give_detail_change_team, detail.give_detail_change_features]
    selected_functions = random.sample(func_list, 6)
    question = ""
    for func in selected_functions:
        question += func(player_data, employ_data)
    return question


def mid_question(player_data, employ_data):
    if len(employ_data) == 1:
        func_list = [detail.give_detail_birth, detail.give_detail_current_team, detail.give_detail_money,
                     detail.give_detail_body, detail.give_detail_preform, detail.give_detail_shirt]
    else:
        func_list = [detail.give_detail_birth, detail.give_detail_current_team, detail.give_detail_money,
                     detail.give_detail_body, detail.give_detail_preform, detail.give_detail_shirt,
                     detail.give_detail_change_team, detail.give_detail_change_features]
    selected_functions = random.sample(func_list, 5)
    question = ""
    for func in selected_functions:
        question += func(player_data, employ_data)
    return question


def hard_question(player_data, employ_data):
    if len(employ_data) == 1:
        func_list = [detail.give_detail_birth, detail.give_detail_current_team, detail.give_detail_money,
                     detail.give_detail_body, detail.give_detail_preform, detail.give_detail_shirt]
    else:
        func_list = [detail.give_detail_birth, detail.give_detail_current_team, detail.give_detail_money,
                     detail.give_detail_body, detail.give_detail_preform, detail.give_detail_shirt,
                     detail.give_detail_change_team, detail.give_detail_change_features]
    selected_functions = random.sample(func_list, 4)
    question = ""
    for func in selected_functions:
        question += func(player_data, employ_data)
    return question


def correct_answer():
    global score
    global num_correct
    global difficulty
    num_correct += 1
    score += 1 + 1 * difficulty


def wrong_answer():
    global lives
    lives -= 1


def end_game():
    global difficulty, num_correct, score, user_id, g_team_id, lives
    play_query = "INSERT INTO play (name, game_id) VALUES (%s, %s)"
    game_query = "INSERT INTO games (difficulty, score, date, correct_answers) VALUES (%s, %s, NOW(), %s)"
    cursor = get_mysql_connector().cursor()

    cursor.execute(game_query, (str(difficulty), score, num_correct))
    game_id = cursor.lastrowid
    cursor.execute(play_query, (user_id, game_id))
    get_mysql_connector().commit()
    difficulty = 0
    num_correct = 0
    score = 0
    g_team_id = 0
    lives = 10

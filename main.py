import pandas as pd
import mysql.connector

# 3 - full name, 4 - position, 5 - rating, 7 - worth, 8 - wage, 10 - date of birth, 11 - height, 12 - weight
# 14 - team name, 15 - league name, 18 - shirt number, 23 - nationality
# rating?

mydb = mysql.connector.connect(
  host="localhost",
  user="team03",
  password="0003",
  database="db03"
)
mycursor = mydb.cursor()

def install_data_inDB(path, year):
    columns_to_extract = [2, 4, 5, 7, 8, 10, 11, 12, 14, 15, 18, 23]
    player_query = "INSERT INTO player (full_name, date_of_birth, nationality) VALUES (%s, %s, %s)"
    team_query = "INSERT INTO team (name, league_id) VALUES (%s, %s)"
    employ_query = "INSERT INTO employ (player_id, team_id, year," \
                   " position, rating, height, weight, worth, wage, jersey_number)" \
                   " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    league_query = "INSERT INTO league (name) VALUES (%s)"
    chunk_size = 1000

    mycursor.execute("SELECT DISTINCT id, full_name FROM player;")
    db_data = mycursor.fetchall()
    player_list = {full_name: id for id, full_name in db_data}
    mycursor.execute("SELECT DISTINCT id, name FROM team;")
    db_data = mycursor.fetchall()
    team_list = {full_name: id for id, full_name in db_data}
    mycursor.execute("SELECT DISTINCT id, name FROM league;")
    db_data = mycursor.fetchall()
    league_list = {full_name: id for id, full_name in db_data}
    mycursor.execute(f"SELECT DISTINCT player_id, team_id FROM employ WHERE year = {year};")
    db_data = mycursor.fetchall()
    employ_list = {p_id: t_id for p_id, t_id in db_data}

    for chunk in pd.read_csv(path, usecols=columns_to_extract, chunksize=chunk_size):
        # Process each chunk and insert data into MySQL

        for index, row in chunk.iterrows():
            if any(pd.isnull(row)):
                continue

            if row[0] not in player_list.keys():
                mycursor.execute(player_query, (row[0], row[5], row[11]))
                player_id = mycursor.lastrowid
            else:
                player_id = player_list[row[0]]

            if row[9] not in league_list.keys():
                mycursor.execute(league_query, (row[9], ))
                league_id = mycursor.lastrowid
                league_list[row[9]] = league_id
            else:
                league_id = league_list[row[9]]

            if row[8] not in team_list.keys():
                mycursor.execute(team_query, (row[8], league_id))
                team_id = mycursor.lastrowid
                team_list[row[8]] = team_id
            else:
                team_id = team_list[row[8]]

            if player_id not in employ_list.keys():
                mycursor.execute(employ_query, (player_id, team_id, year, row[1], row[2], row[6],
                                                row[7], row[3], row[4], row[10]))
                employ_list[player_id] = team_id

    mydb.commit()


if __name__ == 'main':
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_15.csv', 2015)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_16.csv', 2016)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_17.csv', 2017)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_18.csv', 2018)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_19.csv', 2019)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_20.csv', 2020)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_21.csv', 2021)
    install_data_inDB(r'C:\Users\sadna\Documents\Workshop in Data Management\team03\football_player_game\players_22.csv', 2022)
    mycursor.close()


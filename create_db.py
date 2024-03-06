import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="team03",
  password="0003",
  database="db03"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE guess_the_player")

mycursor.execute("CREATE TABLE player(id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                 "full_name VARCHAR(255) NOT NULL,"
                 "date_of_birth DATE NOT NULL,"
                 "nationality VARCHAR(255) NOT NULL);")
                 
mycursor.execute("CREATE TABLE league (id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,"
                 " name VARCHAR(255) NOT NULL"
                 ");")
mycursor.execute("CREATE TABLE games("
                 "id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                 "difficulty VARCHAR(255) NOT NULL,"
                 "score BIGINT NOT NULL,"
                 "date DATETIME NOT NULL,"
                 "correct_answers BIGINT NOT NULL"
                 ");")

mycursor.execute("CREATE TABLE user("
                 "username VARCHAR(255) NOT NULL PRIMARY KEY,"
                 "name VARCHAR(255) NOT NULL,"
                 "password VARCHAR(255) NOT NULL"
                 ");")
mycursor.execute("CREATE TABLE team("
                 "id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                 "name VARCHAR(255) NOT NULL,"
                 "league_id BIGINT UNSIGNED NOT NULL,"
                 "FOREIGN KEY (league_id) REFERENCES league (id)"
                 ");")
mycursor.execute("CREATE TABLE employ("
                 "player_id BIGINT UNSIGNED NOT NULL,"
                 "team_id BIGINT UNSIGNED NOT NULL,"
                 "year INT NOT NULL,"
                 "position VARCHAR(255) NOT NULL,"
                 "rating INT NOT NULL,"
                 "height INT NOT NULL,"
                 "weight INT NOT NULL,"
                 "worth BIGINT NOT NULL,"
                 "wage BIGINT NOT NULL,"
                 "jersey_number INT NOT NULL,"
                 "PRIMARY KEY (team_id, player_id, year),"
                 "FOREIGN KEY (team_id) REFERENCES team (id),"
                 "FOREIGN KEY (player_id) REFERENCES player (id)"
                 ");")

mycursor.execute("CREATE TABLE play("
                 "name VARCHAR(255) NOT NULL ,"
                 "game_id BIGINT UNSIGNED NOT NULL,"
                 "PRIMARY KEY (name, game_id),"
                 "FOREIGN KEY (name) REFERENCES user (username),"
                 "FOREIGN KEY (game_id) REFERENCES games (id)"
                 ");")


mycursor.close()

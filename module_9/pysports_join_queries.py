import mysql.connector
from mysql.connector import errorcode

#Database Config Section
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#Attempts to connect using config then displays connection result
try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]) + "\n\n")

#Tests for potential errors in connection to database
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
        print("The supplied username or password are invalid")
              
    elif err.errno == errorcode. ER_BAD_DB_ERROR: 
        print("The specified database does not exist")

    else:
        print(err)

#Runs inner join and displays results
finally: 
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    # Print Players Loop
    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]) + "\n")

    input("\n\n Press any key to continue...")

    db.close()
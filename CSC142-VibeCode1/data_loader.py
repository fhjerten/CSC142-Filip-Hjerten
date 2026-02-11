import csv
from player import Player
from team import Team

def load_teams_from_csv(filename):
    teams = {} 

    with open(filename, "r", encoding="utf-8-sig") as file: 
        # I add utf-8-sig because excel can add a hidden character
        reader = csv.reader(file)

        header = next(reader) # Take header later

        for row in reader:
            # skipping tghe empty rows
            if row [0]=="":
                continue

            team_name = row[0]
            gender = row[1]
            number = row[2]
            name = row[3]

        # all the stats

            stats ={
                "PPG": row[4],
                "FGA": row[5],
                "FG%": row[6],
                "3PT%": row[7],
                "FT%": row[8],
                "AST": row[9],
                "STL": row[10],
                "BLK": row[11], }
            

            
            player = Player(team_name, gender, number, name, stats)
            key = (team_name, gender)

            if key not in teams:
                teams[key] = Team(team_name, gender)

            teams[key].add_player(player)

    return teams


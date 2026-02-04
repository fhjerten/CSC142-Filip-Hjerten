import pandas as pd

FILE_NAME = "players.csv"

def load_players ():
    players = pd.read_csv(FILE_NAME, sep=";")

# Remove extra spaces

    players.columns = [c.strip() for c in players.columns]

    players["Name"] = players["Name"].str.strip()

    return players


def search_player(player, name):
    return player[player["Name"].str.contains(name, case=False, na=False)]

def main():
    players = load_players()
    name = input("Enter player name to search: ")
    result = search_player(players, name)

    print (result)



if __name__ == "__main__":
    main()

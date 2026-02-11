from data_loader import load_teams_from_csv


def main():
    # Loading all from the csv file
    teams = load_teams_from_csv("players.csv")

    #What teams were found
    print ("Team found:", )
    for (team_name, gender) in teams:
        print (f"{team_name} ({gender})")

    # Showing one team
    key = ("Albright Men's Basketball", "M")
    if key in teams:
        team = teams[key]
        print ("Roster for Men's team:")
        team.display_roster()

        number = input ("Enter a player number to see stats: ")
        player = team.find_player(number)

        if player:
            player.display_stats()
        else:
            print ("Couldn't find player.")


if __name__ == "__main__":
    main()
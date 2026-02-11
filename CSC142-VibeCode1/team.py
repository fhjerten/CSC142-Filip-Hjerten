class Team:
    def __init__(self, team_name, gender):
        self.team_name = team_name
        self.gender = gender
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_roster(self):
        sorted_players = sorted(self.players, key=lambda p: p.number)   #lambda for a one line function. and p.number for their number.
        for p in sorted_players:
            print (p)

    def find_player(self, number):
        number = int(number)
        for p in self.players:
            if p.number == number:
                return p
        
        return None

class Player:
    def __init__(self, name, number, gender, points, rebounds, assists):
        self.name = name
        self.number = number
        self.gender = gender
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def display_stats(self):
        print(f"\nStats for #{self.number} {self.name}")
        print(f"Points: {self.points}")
        print(f"Rebounds: {self.rebounds}")
        print(f"Assists: {self.assists}")
class Team:
    def __init__(self, team_name, gender):
        self.team_name = team_name
        self.gender = gender
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_players_sorted_by_number(self):
        return sorted(self.players, key=lambda p: p.number)

    def display_players(self):
        print(f"\n{self.team_name} ({self.gender}) Roster:")
        for player in self.get_players_sorted_by_number():
            print(f"#{player.number} - {player.name}")

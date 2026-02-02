def main():
    teams = load_teams_from_excel("")

    print("Available Teams:")
    for i, (team_name, gender) in enumerate(teams.keys(), start=1):
        print(f"{i}. {team_name} ({gender})")

    choice = int(input("\nSelect a team: ")) - 1
    team_key = list(teams.keys())[choice]
    team = teams[team_key]

    print(f"\n{team.team_name} ({team.gender}) Players:")
    team.display_players()

    num = int(input("\nEnter player number: "))

    for player in team.players:
        if player.number == num:
            player.display_stats()
            break
    else:
        print("Player not found.")

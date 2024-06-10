
import random

def create_round_robin_schedule(team_list):
    # function to create a round robin schedule for any number of teams
    if len(team_list) % 2 != 0:
        team_list.append(None)

    n = len(team_list)
    schedule = []

    for round in range(n - 1):
        round_matches = []

        for i in range(n // 2):
            team1 = team_list[i]
            team2 = team_list[n - 1 - i]
            if team1 is not None and team2 is not None:
                round_matches.append((team1, team2))
        schedule.append(round_matches)

        # Rotate the teams, keeping the first team fixed
        team_list = [team_list[0]] + team_list[-1:] + team_list[1:-1]

    return schedule


# list of participating teams
teams = ["SMCC", "ERIE MASON", "CRISTO REY", "CESAR CHAVEZ", "IDA", "VOYAGEUR COLLEGE PREP"]
# shuffle teams
random.shuffle(teams)

# call round robin schedule
schedule = create_round_robin_schedule(teams)

# display
for round_num, round in enumerate(schedule, 1):
    print(f"Round {round_num}:")
    for match in round:
        print(f"{match[0]} vs {match[1]}")
    print()

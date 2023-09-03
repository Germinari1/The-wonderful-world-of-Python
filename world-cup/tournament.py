# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    #Read teams into memory from file
    file = sys.argv[1]
    teams = []
    with open(file) as file2:
        reader = csv.DictReader(file2)
        for team in reader:
            team_temp = team
            team_temp['rating']= int(team_temp['rating'])
            teams.append(team_temp)

#Simulate N tournaments and keep track of win counts -> key/value = team/n° of wins
    counts = {}
    for champion in range(N):
        win = simulate_tournament(teams)
        if win in counts:
            counts[win] +=1
        elif win not in counts:
            counts[win] = 1


    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")

    #close files after usage
    file2.close()




def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])
    return winners


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    rounds = len(teams)
    if rounds >= 2:
        teams = simulate_round(teams)
        return simulate_tournament(teams)
    else:
        winner = teams[0]["team"]
        return winner
    """while len(teams)>1:
        x = simulate_round(teams)
    return x[0]['team']"""


if __name__ == "__main__":
    main()

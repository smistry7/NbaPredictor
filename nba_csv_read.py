import csv
from nba_team import NbaTeam
from nba_player import NbaPlayer
from nba_result import NbaResult


class NbaCsvReader:
    def read_player_data(filename):
        players = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = NbaPlayer(row)
                players.append(player)
            return players

    def read_team_data(filename):
        teams = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = NbaTeam(row)
                teams.append(team)
            return teams

    def read_results(filename):
        results = []
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result = NbaResult(row)
                results.append(result)
            return results


players = NbaCsvReader.read_player_data("1718playerdata.csv")
teams = NbaCsvReader.read_team_data("1718teamdata.csv")
results = NbaCsvReader.read_results("convertedOct2017Results.csv")
sorted_by_team = sorted(players, key=lambda x: x.team)


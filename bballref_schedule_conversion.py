import csv
from nba_result import NbaResult
team_names = {
     "Atlanta Hawks": "ATL",
     "Brooklyn Nets": "BKN",
     "Boston Celtics": "BOS",
     "Charlotte Hornets": "CHA",
     "Chicago Bulls": "CHI",
     "Cleveland Cavaliers": "CLE",
     "Dallas Mavericks": "DAL",
     "Denver Nuggets": "DEN",
     "Detroit Pistons": "DET",
     "Golden State Warriors": "GSW",
     "Houston Rockets": "HOU",
     "Indiana Pacers": "IND",
     "Los Angeles Clippers": "LAC",
     "Los Angeles Lakers": "LAL",
     "Memphis Grizzlies": "MEM",
     "Miami Heat": "MIA",
     "Milwaukee Bucks": "MIL",
     "Minnesota Timberwolves": "MIN",
     "New Orleans Pelicans": "NOP",
     "New York Knicks": "NYK",
     "Oklahoma City Thunder": "OKC",
     "Orlando Magic": "ORL",
     "Philadelphia 76ers": "PHI",
     "Phoenix Suns": "PHX",
     "Portland Trail Blazers": "POR",
     "Sacramento Kings": "SAC",
     "San Antonio Spurs": "SAS",
     "Toronto Raptors": "TOR",
     "Utah Jazz": "UTA",
     "Washington Wizards": "WAS"
}

def convert_schedule(filename):
    f = open("converted" + filename, "w+")
    f.write("Home,Away,Result\n")
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            home_team = team_names[row['Home/Neutral']]
            away_team = team_names[row['Visitor/Neutral']]
            result =0
            if int(row['APTS']) < int(row['HPTS']):
               result = 1
            f.write(home_team + "," + away_team + "," + str(result)+"\n")
    f.close()


convert_schedule("Oct2017Results.csv")

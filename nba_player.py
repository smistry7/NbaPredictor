# NBA player structure
class NbaPlayer:
    team = ""
    age = 0
    minutesPlayed = 0
    efficientFieldGoalPercentage = 0
    totalRebounds = 0
    assists = 0
    steals = 0
    blocks = 0
    turnovers = 0
    pointsPerGame = 0

    def __init__(self, row):
        try:
            self.team = row['Tm']
            self.turnovers = float(row['TOV'])
            self.steals = float(row['STL'])
            self.pointsPerGame = float(row['PS/G'])
            self.blocks = float(row['BLK'])
            self.assists = float(row['AST'])
            self.age = float(row['Age'])
            self.efficientFieldGoalPercentage = float(row['eFG%'])
            self.minutesPlayed = float(row['MP'])
            self.totalRebounds = float(row['TRB'])
        except:
            pass

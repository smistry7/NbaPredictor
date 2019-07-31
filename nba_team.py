# NBA team object
class NbaTeam:
    pointsPerGame = 0
    fieldGoalPercentage = 0
    threePointersMade = 0
    threePointersAttempted = 0
    twoPointersMade = 0
    twoPointersAttempted = 0
    freeThrowsMade = 0
    freeThrowsAttempted = 0
    offensiveRebounds = 0
    defensiveRebounds = 0
    assists = 0
    steals = 0
    blocks = 0
    turnovers = 0
    name = ""

    def __init__(self, row):
        self.name = row['Team']
        self.assists = float(row['AST'])
        self.blocks = float(row['BLK'])
        self.defensiveRebounds = float(row['DRB'])
        self.fieldGoalPercentage = float(row['FG%'])
        self.freeThrowsAttempted = float(row['FTA'])
        self.freeThrowsMade = float(row['FT'])
        self.offensiveRebounds = float(row['ORB'])
        self.pointsPerGame = float(row['PTS'])
        self.steals = float(row['STL'])
        self.threePointersAttempted = float(row['3PA'])
        self.threePointersMade = float(row['3P'])
        self.turnovers = float(row['TOV'])
        self.twoPointersAttempted = float(row['2PA'])
        self.twoPointersMade = float(row['2P'])

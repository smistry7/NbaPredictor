class NbaResult:
    homeTeam = ""
    awayTeam = ""
    # 1 for home win, 0 for away win
    result = 0

    def __init__(self, row):
        self.homeTeam = row['Home']
        self.awayTeam = row['Away']
        self.result = int(row['Result'])
        

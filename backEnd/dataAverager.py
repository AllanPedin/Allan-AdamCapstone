import csv
def getFileString(team):#team = 3 character string team name
    fileDict  = {# no switch cases in python apperently
        "ATL": "AtlantaHawksgamelog.csv",
        "BOS": "BostonCelticsgamelog.csv",
        "BKN": "BrooklynNetsgamelog.csv",
        "CHA": "CharlotteHornetsgamelog.csv",
        "CHI": "ChicagoBullsgamelog.csv",
        "CLE": "ClevelandCavaliersgamelog.csv",
        "DAL": "DallasMavericksgamelog.csv",
        "DEN": "DenverNuggetsgamelog.csv",
        "DET": "DetroitPistonsgamelog.csv",
        "GSW": "GoldenStateWarriorsgamelog.csv",
        "HOU": "HoustonRocketsgamelog.csv",
        "IND": "IndianaPacersgamelog.csv",
        "LAC": "LAClippersgamelog.csv",
        "LAL": "LosAngelesLakersgamelog.csv",
        "MEM": "MemphisGrizzliesgamelog.csv",
        "MIA": "MiamiHeatgamelog.csv",
        "MIL": "MilwaukeeBucksgamelog.csv",
        "MIN": "MinnesotaTimberwolvesgamelog.csv",
        "NOP": "NewOrleansPelicansgamelog.csv",
        "NYK": "NewYorkKnicksgamelog.csv",
        "OKC": "OklahomaCityThundergamelog.csv",
        "ORL": "OrlandoMagicgamelog.csv",
        "PHI": "Philadelphia76ersgamelog.csv",
        "PHX": "PhoenixSunsgamelog.csv",
        "POR": "PortlandTrailBlazersgamelog.csv",
        "SAC": "SacramentoKingsgamelog.csv",
        "SAS": "SanAntonioSpursgamelog.csv",
        "TOR": "TorontoRaptorsgamelog.csv",
        "UTA": "UtahJazzgamelog.csv",
        "WAS": "WashingtonWizardsgamelog.csv"         
    }
    return "nba_web_scraper/teamGameLogs/" + fileDict[team]


def addStats(previousStats, currentStats):
    newStats = []
    for i in range(len(previousStats)):
        try:
            newStats.append(int(previousStats[i]) + int(currentStats[i])) # int stat
        except:#string stat AKA win loss
            try:
                newStats.append(float(previousStats[i]) + float(currentStats[i])) #float stat
            except:
                newStats.append(previousStats[i] + currentStats[i]) #string stat
    return newStats

def averageStats(previousStats, numGames):
    newStats = []
    for stat in previousStats:
        try:
            newStats.append(int(stat)/numGames)
        except:
            try:
                newStats.append(float(stat)/numGames)
            except:
                wins = 0.0
                for char in stat:
                    if(char == 'W'):
                        wins += 1
                newStats.append(wins/numGames)
    return newStats
#read stats
def getDateStatsDict():
    dateteamStatsDict = {}
    teamLogs = ["AtlantaHawksgamelog.csv", "BostonCelticsgamelog.csv", "BrooklynNetsgamelog.csv", "CharlotteHornetsgamelog.csv", "ChicagoBullsgamelog.csv", "ClevelandCavaliersgamelog.csv", "DallasMavericksgamelog.csv", "DenverNuggetsgamelog.csv", "DetroitPistonsgamelog.csv", "GoldenStateWarriorsgamelog.csv", "HoustonRocketsgamelog.csv", "IndianaPacersgamelog.csv", "LAClippersgamelog.csv", "LosAngelesLakersgamelog.csv", "MemphisGrizzliesgamelog.csv", "MiamiHeatgamelog.csv", "MilwaukeeBucksgamelog.csv", "MinnesotaTimberwolvesgamelog.csv", "NewOrleansPelicansgamelog.csv", "NewYorkKnicksgamelog.csv", "OklahomaCityThundergamelog.csv", "OrlandoMagicgamelog.csv", "Philadelphia76ersgamelog.csv", "PhoenixSunsgamelog.csv", "PortlandTrailBlazersgamelog.csv", "SacramentoKingsgamelog.csv", "SanAntonioSpursgamelog.csv", "TorontoRaptorsgamelog.csv", "UtahJazzgamelog.csv", "WashingtonWizardsgamelog.csv"]
    for teamLog in teamLogs:
        with open("nba_web_scraper/teamGameLogs/" + teamLog , mode='r') as csv_file:
            previousStats = None
            numGames = 0
            for row in reversed(list(csv.reader(csv_file))):
                try:
                    currentStats = list(row[i] for i in range(len(row)))
                    del currentStats[0]
                    if previousStats == None:
                        dateteamStatsDict[row[0][:18]] = None
                        previousStats = currentStats
                    else:
                        dateteamStatsDict[row[0][:18]] = averageStats(previousStats, numGames)
                        previousStats = addStats(previousStats, currentStats)
                    numGames += 1
                except Exception as e:
                    print(e)
                    print("hererere")#row is empty
                    continue
    return dateteamStatsDict
                    
dateteamStatsDict = getDateStatsDict()
for date, stats in dateteamStatsDict.items():
    print(date, stats)
    if(stats != None):
        print(len(stats))

#average stats up to game

#average stats againsts average stats

#save game in csv
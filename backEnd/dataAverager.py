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


def addStats(stats1, stats2):
    newStats = []
    for i in range(len(stats1)):
        newStats.append(stats1[i]+stats2[i])
    return newStats

#read stats
dateteamStatsDict = {}
def fillDateStatsDict():
    teamLogs = ["AtlantaHawksgamelog.csv", "BostonCelticsgamelog.csv", "BrooklynNetsgamelog.csv", "CharlotteHornetsgamelog.csv", "ChicagoBullsgamelog.csv", "ClevelandCavaliersgamelog.csv", "DallasMavericksgamelog.csv", "DenverNuggetsgamelog.csv", "DetroitPistonsgamelog.csv", "GoldenStateWarriorsgamelog.csv", "HoustonRocketsgamelog.csv", "IndianaPacersgamelog.csv", "LAClippersgamelog.csv", "LosAngelesLakersgamelog.csv", "MemphisGrizzliesgamelog.csv", "MiamiHeatgamelog.csv", "MilwaukeeBucksgamelog.csv", "MinnesotaTimberwolvesgamelog.csv", "NewOrleansPelicansgamelog.csv", "NewYorkKnicksgamelog.csv", "OklahomaCityThundergamelog.csv", "OrlandoMagicgamelog.csv", "Philadelphia76ersgamelog.csv", "PhoenixSunsgamelog.csv", "PortlandTrailBlazersgamelog.csv", "SacramentoKingsgamelog.csv", "SanAntonioSpursgamelog.csv", "TorontoRaptorsgamelog.csv", "UtahJazzgamelog.csv", "WashingtonWizardsgamelog.csv"]
    for teamLog in teamLogs:
        with open("nba_web_scraper/teamGameLogs/" + teamLog , mode='r') as csv_file:
            previousStats = None
            for row in reversed(list(csv.reader(csv_file))):
                try:
                    print(row[0])
                    currentStats = list(row[i] for i in range(len(row))); del currentStats[0]; del currentStats[1]
                    print(row[0])
                    dateteamStatsDict[row[0][:18]] = previousStats
                    previousStats = addStats(previousStats, currentStats)

                except Exception as e:
                    print(e)
                    print("hererere")#row is empty
                    continue
                
                # dateStatsDict[row.co]
    
fillDateStatsDict()
print(dateteamStatsDict)

#average stats up to game

#average stats againsts average stats

#save game in csv
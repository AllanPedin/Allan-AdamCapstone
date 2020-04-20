import csv
#gets average tam stats up to a date
def teamStats(team, date):#team = 3 character string team name,   date = string date (Nov 23, 2019)

    with open('../NBA_Data/2019-2020_NBA_Team_Stats.csv') as NBAData:
        csvReader = csv.reader(NBAData)

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

print(getFileString("ORL"))
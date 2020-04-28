import csv
def debugLogger(log):
    if False:
        print(log)

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
teamLogs = ["AtlantaHawksgamelog.csv", "BostonCelticsgamelog.csv", "BrooklynNetsgamelog.csv", "CharlotteHornetsgamelog.csv", "ChicagoBullsgamelog.csv", "ClevelandCavaliersgamelog.csv", "DallasMavericksgamelog.csv", "DenverNuggetsgamelog.csv", "DetroitPistonsgamelog.csv", "GoldenStateWarriorsgamelog.csv", "HoustonRocketsgamelog.csv", "IndianaPacersgamelog.csv", "LAClippersgamelog.csv", "LosAngelesLakersgamelog.csv", "MemphisGrizzliesgamelog.csv", "MiamiHeatgamelog.csv", "MilwaukeeBucksgamelog.csv", "MinnesotaTimberwolvesgamelog.csv", "NewOrleansPelicansgamelog.csv", "NewYorkKnicksgamelog.csv", "OklahomaCityThundergamelog.csv", "OrlandoMagicgamelog.csv", "Philadelphia76ersgamelog.csv", "PhoenixSunsgamelog.csv", "PortlandTrailBlazersgamelog.csv", "SacramentoKingsgamelog.csv", "SanAntonioSpursgamelog.csv", "TorontoRaptorsgamelog.csv", "UtahJazzgamelog.csv", "WashingtonWizardsgamelog.csv"]

dateteamStatsDict = {}
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
                debugLogger("row is empty or column tag")#row is empty
                continue
                    

def getStatsOfGame(gameString):
    team1 = gameString[15:18]
    team2 = gameString[::-1][:3][::-1]
    statString1 = gameString[:15] + team1 
    statString2 = gameString[:15] + team2 
    return [dateteamStatsDict[statString1], dateteamStatsDict[statString2]]

# average stats againsts average stats with winner
games = [] #array of tuples first item contains array of 2 game stats, second item contains 1 or 0, 1 means first stat won
for teamLog in teamLogs:
    with open("nba_web_scraper/teamGameLogs/" + teamLog , mode='r') as csv_file:
        for row in reversed(list(csv.reader(csv_file))):
            try:
                gameString = row[0]
                if gameString == "MATCHUP":
                    raise Exception("Header of csv")
                winner = 1
                if row[1] == "L":
                    winner = 0
                games.append((getStatsOfGame(gameString), winner, gameString))
            except Exception as e:
                debugLogger("row is empty or column header")

            # game =     

for game, winner, gameString in games:
    print(game[0])
    print(game[1])
    print(winner)
# print(games)
print(len(games))

trainingGames = []
trainingLabels = []
testGames = []
testLabels = []

from random import randint 
thisWeeksGames = []
for game in games:
    if game[0][0] == None or game[0][1] == None:
        teamStats = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    else:
        teamStats = game[0]
    winner = game[1]
    if "Mar 08" in game[2] or "Mar 09" in game[2] or "Mar 10" in game[2] or "Mar 11" in game[2]:
        testGames.append(teamStats)
        testLabels.append(winner)
        thisWeeksGames.append(game)
    else:
        trainingGames.append(teamStats)
        trainingLabels.append(winner)
from numpy import save
save('./API/matchups', thisWeeksGames)

print(testGames)
print(testLabels)
print("-------------")
print(trainingGames)
print(trainingLabels)


def getTrainingGames():
    return trainingGames
def getTrainingLabels():
    return trainingLabels

def getTestGames():
    return testGames
def getTestLabels():
    return testLabels

def getGamesFromGamesAndWinners(gamesAndWinners):
    myGames = []
    for myGame in gamesAndWinners:
        if myGame[0][0] == None or myGame[0][1] == None:
            teamStats = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        else:
            teamStats = myGame[0]
        myGames.append(teamStats)
    return myGames
        
    

def getGamesFromCSV(file):
    gamesToPredict = []
    with open(file , mode='r') as csv_file:
        for row in list(csv.reader(csv_file)):
            try:
                gameString = row[0]
                if gameString == "MATCHUP":
                    raise Exception("Header of csv")
                winner = 1
                if row[1] == "L":
                    winner = 0
                gamesToPredict.append((getStatsOfGame(gameString), winner))
            except Exception as e:
                debugLogger("row is empty or column header")
    return getGamesFromGamesAndWinners(gamesToPredict)



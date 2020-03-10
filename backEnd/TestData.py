import numpy as np
#https://stats.nba.com/game/0021900684/
#Date of game: Jan 25th
lakers_game_one_total = [35,76,46.1,6,31,19.4,15,23,65.2,6,29,35,23,21,12,1,18,91,-17]
philly_game_one_total = [41,78,52.6,13,37,35.1,13,19,68.4,8,33,41,19,21,12,3,18,108,17]

#https://stats.nba.com/game/0021900754/
#Date of game: Feb 4th
lakers_other_game = [50,85,58.8,12,28,42.9,17,25,68.0,12,46,58,28,14,5,4,15,129,27]
spurs_game = [40,91,44.0,13,27,48.1,915,60.0,7,21,28,21,6,6,2,16,102,-27]

#https://stats.nba.com/game/0021900766/
#Date of game: Feb 6th
philly_other_game = [37,99,37.4,19,45,42.2,8,14,57.1,11,39,50,24,11,7,4,14,101,-11]
bucks_game = [44,94,46.8,12,37,32.4,12,18,66.7,9,51,60,19,14,3,8,18,112,11]


#THIS IS THE REAL OUTCOME FOR GAME 2
#https://stats.nba.com/game/0021900915/
#Date of game: March 3rd
lakers_game_two_total =  [46,86,53.5,13,33,39.4,15,18,83.3,10,33,43,25,13,9,6,18,120,13]
philly_game_two_total = [38,85,44.7,16,40,40.0,15,20,75.0,12,30,42,24,15,10,1,17,107,-13]

no_game_total = [0,0,0.0,0,0,0.0,0,0,0.0,0,0,0,0,0,0,0,0,0,0]

def addStats(stats1, stats2):
    newStats = []
    for i in range(len(stats1)):
        newStats.append(stats1[i]+stats2[i])
    return newStats
game1 = [no_game_total,no_game_total]
game2 = [lakers_game_one_total,no_game_total]
game3 = [philly_game_one_total,no_game_total]
game4 = [addStats(lakers_game_one_total,lakers_other_game),addStats(philly_game_one_total,philly_other_game)]

testGame = [addStats(game4[0],lakers_game_two_total),addStats(game4[1],philly_game_two_total)]

def getTrainingGames():
    return np.array([game1, game2, game3, game4])
def getTrainingLabels():
    return np.array([1,0,1,0])
def getTestGame():
    return np.array([testGame])

# print(getTrainingGames())
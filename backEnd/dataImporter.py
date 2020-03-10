import csv
def teamStats_19_20():
    with open('../NBA_Data/2019-2020_NBA_Team_Stats.csv') as NBAData:
        csvReader = csv.reader(NBAData)
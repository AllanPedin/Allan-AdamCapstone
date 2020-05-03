from selenium import webdriver
import collections
import time
import csv

driver = webdriver.Chrome()

driver.get('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2018-19&SeasonType=Regular%20Season')
time.sleep(2)

csv_file = open('nbateamstats.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(
    ['TEAM', 'GP', 'W', 'L', 'WIN%', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', '+/-'])

teams = driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')

links = []

for team in teams:
    teams_dict = collections.OrderedDict()
    link = team.find_element_by_xpath('.//td[2]/a').get_attribute('href')
    Team = team.find_element_by_xpath('.//td[2]').text
    GP = team.find_element_by_xpath('.//td[3]').text
    W = team.find_element_by_xpath('.//td[4]').text
    L = team.find_element_by_xpath('.//td[5]').text
    Winper = team.find_element_by_xpath('.//td[6]').text
    Min = team.find_element_by_xpath('.//td[7]').text
    Pts = team.find_element_by_xpath('.//td[8]').text
    FGM = team.find_element_by_xpath('.//td[9]').text
    FGA = team.find_element_by_xpath('.//td[10]').text
    FGper = team.find_element_by_xpath('.//td[11]').text
    threePM = team.find_element_by_xpath('.//td[12]').text
    threePA = team.find_element_by_xpath('.//td[13]').text
    threePper = team.find_element_by_xpath('.//td[14]').text
    FTM = team.find_element_by_xpath('.//td[15]').text
    FTA = team.find_element_by_xpath('.//td[16]').text
    FTper = team.find_element_by_xpath('.//td[17]').text
    OReb = team.find_element_by_xpath('.//td[18]').text
    DReb = team.find_element_by_xpath('.//td[19]').text
    Reb = team.find_element_by_xpath('.//td[20]').text
    Ast = team.find_element_by_xpath('.//td[21]').text
    TOv = team.find_element_by_xpath('.//td[22]').text
    Stl = team.find_element_by_xpath('.//td[23]').text
    Blk = team.find_element_by_xpath('.//td[24]').text
    BlkA = team.find_element_by_xpath('.//td[25]').text
    PF = team.find_element_by_xpath('.//td[26]').text
    PFD = team.find_element_by_xpath('.//td[27]').text
    plusMinus = team.find_element_by_xpath('.//td[28]').text
    links.append([link, Team.replace(' ', '')])

    teams_dict['Team'] = Team
    teams_dict['GP'] = GP
    teams_dict['W'] = W
    teams_dict['L'] = L
    teams_dict['Winper'] = Winper
    teams_dict['Min'] = Min
    teams_dict['Pts'] = Pts
    teams_dict['FGM'] = FGM
    teams_dict['FGA'] = FGA
    teams_dict['FGper'] = FGper
    teams_dict['threePM'] = threePM
    teams_dict['threePA'] = threePA
    teams_dict['threePper'] = threePper
    teams_dict['FTM'] = FTM
    teams_dict['FTA'] = FTA
    teams_dict['FTper'] = FTper
    teams_dict['OReb'] = OReb
    teams_dict['DReb'] = DReb
    teams_dict['Reb'] = Reb
    teams_dict['Ast'] = Ast
    teams_dict['TOv'] = TOv
    teams_dict['Stl'] = Stl
    teams_dict['Blk'] = Blk
    teams_dict['BlkA'] = BlkA
    teams_dict['PF'] = PF
    teams_dict['PFD'] = PFD
    teams_dict['plusMinus'] = plusMinus
    writer.writerow(teams_dict.values())

csv_file.close()

def gamelogtable(lin):
    driver.get(lin[0].replace('traditional', 'boxscores-traditional'))
    time.sleep(4)
    while True:
        try:
            button = driver.find_element_by_xpath(
                '/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[2]/div/a')
            button.click()
        except:
            break
    csv_files = open(lin[1] + 'gamelog.csv', 'w')
    writersss = csv.writer(csv_files)
    writersss.writerow(['MATCHUP', 'W/L', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF'])
    tabs = driver.find_elements_by_xpath(
        '/html/body/main/div[2]/div/div/div[3]/div/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')

    for tab in tabs:
        tab_dict = collections.OrderedDict()

        Matchup = tab.find_element_by_xpath('.//td[1]').text
        WL = tab.find_element_by_xpath('.//td[2]').text
        Min = tab.find_element_by_xpath('.//td[3]').text
        Pts = tab.find_element_by_xpath('.//td[4]').text
        FGM = tab.find_element_by_xpath('.//td[5]').text
        FGA = tab.find_element_by_xpath('.//td[6]').text
        FGper = tab.find_element_by_xpath('.//td[7]').text
        threePM = tab.find_element_by_xpath('.//td[8]').text
        threePA = tab.find_element_by_xpath('.//td[9]').text
        threePper = tab.find_element_by_xpath('.//td[10]').text
        FTM = tab.find_element_by_xpath('.//td[11]').text
        FTA = tab.find_element_by_xpath('.//td[12]').text
        FTper = tab.find_element_by_xpath('.//td[13]').text
        OReb = tab.find_element_by_xpath('.//td[14]').text
        DReb = tab.find_element_by_xpath('.//td[15]').text
        Reb = tab.find_element_by_xpath('.//td[16]').text
        Ast = tab.find_element_by_xpath('.//td[17]').text
        Stl = tab.find_element_by_xpath('.//td[18]').text
        Blk = tab.find_element_by_xpath('.//td[19]').text
        TOv = tab.find_element_by_xpath('.//td[20]').text
        PF = tab.find_element_by_xpath('.//td[21]').text

        tab_dict['Matchup'] = Matchup
        tab_dict['WL'] = WL
        tab_dict['Min'] = Min
        tab_dict['Pts'] = Pts
        tab_dict['FGM'] = FGM
        tab_dict['FGA'] = FGA
        tab_dict['FGper'] = FGper
        tab_dict['threePM'] = threePM
        tab_dict['threePA'] = threePA
        tab_dict['threePper'] = threePper
        tab_dict['FTM'] = FTM
        tab_dict['FTA'] = FTA
        tab_dict['FTper'] = FTper
        tab_dict['OReb'] = OReb
        tab_dict['DReb'] = DReb
        tab_dict['Reb'] = Reb
        tab_dict['Ast'] = Ast
        tab_dict['Stl'] = Stl
        tab_dict['Blk'] = Blk
        tab_dict['TOv'] = TOv
        tab_dict['PF'] = PF
        writersss.writerow(tab_dict.values())
    csv_files.close()


for i in links:
    gamelogtable(i)

driver.close()

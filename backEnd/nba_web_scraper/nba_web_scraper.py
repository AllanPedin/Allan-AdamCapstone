from selenium import webdriver
#this file
driver = webdriver.Chrome()
driver.get('https://stats.nba.com/schedule/#!?PD=N')
class Team:
    def __init__(self, _name, _fgm, _fga, _3pm, _3pa, _ftm, _fta, _oreb, _dreb, _reb, _ast, _tov, _stl, _blk, _pf, _pts):
        self.name = _name
        self.fgm = _fgm
        self.fga = _fga
        self.three_pm = _3pm
        self.three_pa = _3pa
        self.ftm = _ftm
        self.fta = _fta
        self.oreb = _oreb
        self.dreb = _dreb
        self.reb = _reb
        self.ast = _ast
        self.tov = _tov
        self.stl = _stl
        self.blk = _blk
        self.pf = _pf
        self.pts = _pts

d

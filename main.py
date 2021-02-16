from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
import matplotlib.pyplot as plt
import numpy as np
import ssl
from datetime import date


def get_Winners(url): 
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find_all('div', class_='game_summary expanded nohover')
    for header in table_rows:
        trs = header.find_all('tr', class_='winner')
        for tr in trs:
            team = tr.find('a')
            teamname = str(team)
            abrev = ''.join(re.findall('[A-Z]+',teamname))
            finalabrev = abrev[:3]
            print(finalabrev)


def get_Games(url): 
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find('table', id='schedule')
    games = table_rows.find_all('tr')
    for game in games:
        if gamedate in (game.get_text()):
            awayteam = str(game.find("td", attrs={"data-stat":"visitor_team_name"}))
            awayabrev = (''.join(re.findall('[A-Z]+',awayteam)))[:3]
            hometeam = str(game.find("td", attrs={"data-stat":"home_team_name"}))
            homeabrev = (''.join(re.findall('[A-Z]+',hometeam)))[:3]
            print(awayabrev,"at",homeabrev)
                                            

year=input("Year? ")
month=input("Month? ")
day=input("Day? ")


today = date.today()
thismonth = today.strftime("%b")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

gamedate = thismonth+" "+thisday+", "+thisyear
                        

#get_Games("https://www.basketball-reference.com/leagues/NBA_2021_games-february.html")

get_Winners("https://www.basketball-reference.com/boxscores/index.fcgi?month="+month+"&day="+day+"&year="+year+"")

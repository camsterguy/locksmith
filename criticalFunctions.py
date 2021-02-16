from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
import ssl
from datetime import date
from urllib.request import Request, urlopen

today = date.today()
thismonth = today.strftime("%b")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

gamedate = thismonth+" "+thisday+", "+thisyear

spreads = []
awayteams = []
hometeams = []

def setupHTTP(initURL):
    global soup
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(initURL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

def setup403(initURL):
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(initURL, headers=hdr)
    response = urllib.request.urlopen(req, context=ctx).read()
    soup = BeautifulSoup(response, 'html.parser')


#Usage: get_Winners("https://www.basketball-reference.com/boxscores/index.fcgi?month="+month+"&day="+day+"&year="+year+"")
def get_Winners(url): 
    setupHTTP(url)
    table_rows = soup.find_all('div', class_='game_summary expanded nohover')
    for header in table_rows:
        trs = header.find_all('tr', class_='winner')
        for tr in trs:
            team = tr.find('a')
            teamname = str(team)
            abrev = ''.join(re.findall('[A-Z]+',teamname))
            finalabrev = abrev[:3]
            print(finalabrev)

#Usage: get_Games("https://www.basketball-reference.com/leagues/NBA_2021_games-february.html")
def get_Games(url):
    setupHTTP(url)
    table_rows = soup.find('table', id='schedule')
    games = table_rows.find_all('tr')
    for game in games:
        if gamedate in (game.get_text()):
            awayteam = str(game.find("td", attrs={"data-stat":"visitor_team_name"}))
            awayabrev = (''.join(re.findall('[A-Z]+',awayteam)))[:3]
            hometeam = str(game.find("td", attrs={"data-stat":"home_team_name"}))
            homeabrev = (''.join(re.findall('[A-Z]+',hometeam)))[:3]
            #print(awayabrev,"at",homeabrev)
            awayteams.append(awayabrev)
            hometeams.append(homeabrev)
                                            
def get_Spreads(url):
    setup403(url)
    table_rows = soup.find_all('div', attrs={"id":"contentbody"})
    for tr in table_rows:
        print(tr.get_text())


    

                    

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import re
import ssl
from datetime import date
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests,os
import time

today = date.today()
thismonth = today.strftime("%b")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

gamedate = thismonth+" "+thisday+", "+thisyear

spreads = []

def setupSelenium(initurl):
    url = initurl.replace('NYK','NY').replace('NOP','NO').replace('GSW','GS').replace('PHX','PHO').replace('SAS','SA')
    global soup
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.headless = True
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    options.add_argument("--window-size=1920,1200")
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options, executable_path='./drivers/chromedriver')
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    

def setupHTTP(initURL):
    time.sleep(1)
    global soup
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(initURL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

def setup403(initURL):
    global soup
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(initURL, headers=hdr)
    response = urllib.request.urlopen(req, context=ctx).read()
    soup = BeautifulSoup(response, 'html.parser')
    return soup


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

def get_Games(year, month, day):
    print("Finding today's games...")
    dayurl=("https://www.sportsbookreview.com/betting-odds/nba-basketball/?date="+year+month+day)
    setupSelenium(dayurl)
    games = soup.find_all('div', class_='participantContainer-2nQw5')
    for game in games:
        link = game.find('a')
        newURL = "https://www.sportsbookreview.com"+(link['href'])
        break
    setupSelenium(newURL)

    
    allteams = []

    events = soup.find_all('a', class_="event-20qTD")
    for event in events:
        if event.find('section', class_="eventStatus-3EHqw postponed-ow-Wl compact-1oqj7 isMoreEvents-GSPaT") is None:
            teams = event.find_all('div', class_='participant-zVHMr')

            for team in teams:
                allteams.append(team.text[:3])
    

    global awayteams
    global hometeams
    awayteams = []
    hometeams = []
    awayteams = allteams[::2]
    hometeams = allteams[1::2]
    
    matchupDict = {}
    count = 0
    for team in awayteams:
        matchupDict[awayteams[count]] = hometeams[count]
        count += 1


    return matchupDict

    
    
                                            
def get_Spreads(year, month, day):
    print("Finding today's spreads...")
    dayurl=("https://www.sportsbookreview.com/betting-odds/nba-basketball/?date="+year+month+day)
    setupSelenium(dayurl)
    games = soup.find_all('div', class_='columnsContainer-3tVf9')
    for game in games:
        odds = game.find('span', class_='adjust-1uDgI')
        try:
            if "½" in odds.text:
                spreads.append(odds.text[:-1]+".5")
            else:
                spreads.append(odds.text)
        except:
            continue

   

    

                    

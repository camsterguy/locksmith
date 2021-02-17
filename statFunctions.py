import criticalFunctions as crit
from datetime import date
import re

today = date.today()
thismonth = today.strftime("%m")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

teamStats = {}

statURL = "https://www.sportsline.com/nba/game-forecast/NBA_"+thisyear+thismonth+thisday+"_"

year="2021"
month="02"
day="17"


def get_Opponent(team):
	matchupDict = crit.get_Games(year, month, day)
	key_list = list(matchupDict.keys())
	val_list = list(matchupDict.values())
	
	teamLookup = ((matchupDict.get(team)))

	if teamLookup is not None:
		return (teamLookup),"is"
	else:
		position = val_list.index(team)
		return (key_list[position]),"isnt"

'''
def get_Stats(team):
	opponent,isaway=(get_Opponent(team))
	if isaway == "isnt":
		scrapeURL = statURL+opponent+"@"+team
	else:
		scrapeURL = statURL+team+"@"+opponent
	crit.setupSelenium(scrapeURL)
	from criticalFunctions import soup
	if isaway == "isnt":
		stats = soup.findAll("div", class_='trends-details')[1]
	else:
		stats = soup.findAll("div", class_='trends-details')[0]
	ats = (stats.contents[0].get_text())
	percent = ats[-6:-2]
	final = (percent.replace('(','').replace(' ',''))
	teamStats[team]=[]
	teamStats[team].append(final)
	return(final)
'''

def get_SLine(team):
	print("Getting stats for",team)
	opponent,isaway=(get_Opponent(team))
	if isaway == "isnt":
		scrapeURL = statURL+opponent+"@"+team
	else:
		scrapeURL = statURL+team+"@"+opponent
	crit.setupSelenium(scrapeURL)
	from criticalFunctions import soup
	teamStats[team]=[]
	get_Stat(0,1,team,isaway,soup)
	get_Stat(2,3,team,isaway,soup)
	get_Stat(4,5,team,isaway,soup)
	get_Stat(6,7,team,isaway,soup)
	get_Stat(14,15,team,isaway,soup)


def get_Stat(homeindex, awayindex, team, isaway, soup):
	if isaway == "isnt":
		stats = soup.findAll("div", class_='trends-details')[awayindex]
	else:
		stats = soup.findAll("div", class_='trends-details')[homeindex]
	ats = (stats.contents[0].get_text())
	percent = ats[-6:-2]
	final = (percent.replace('(','').replace(' ',''))
	teamStats[team].append(float(final))

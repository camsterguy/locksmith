import criticalFunctions as crit
from datetime import date
import re

today = date.today()
thismonth = today.strftime("%m")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

teamStats = {}

statURL = "https://www.sportsline.com/nba/game-forecast/NBA_"+thisyear+thismonth+thisday+"_"

today = date.today()
month = str((today.strftime("%m"))).lower()
year = (today.strftime("%Y"))
day = (today.strftime("%d"))


def get_Opponent(team):
	print("getting opponent of",team,"...")
	matchupDict = crit.get_Games(year, month, day)
	key_list = list(matchupDict.keys())
	val_list = list(matchupDict.values())

	teamLookup = ((matchupDict.get(team)))

	if teamLookup is not None:
		print(team,"@",teamLookup)
		return (teamLookup),"is"
	else:
		position = val_list.index(team)
		print(key_list[position],"@",team)
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
	get_Stat(0,team,isaway,soup)
	get_Stat(1,team,isaway,soup)
	get_Stat(2,team,isaway,soup)
	get_Stat(3,team,isaway,soup)
	get_Stat(4,team,isaway,soup)
	get_Stat(5,team,isaway,soup)
	get_Stat(6,team,isaway,soup)
	get_Stat(7,team,isaway,soup)


def get_Stat(statnum, team, isaway, soup):
	if isaway == "isnt":
		final = soup.findAll("div", class_='home-trend')[statnum]
		stat = final.findAll("div",)[1].get_text()
		stat = str(stat[:-1])
		if "0-" in stat:
			teamStats[team].append(float(50))
		else:
			teamStats[team].append(float(stat))
		print(teamStats)
	else:
		final = soup.findAll("div", class_='away-trend')[statnum]
		stat = final.findAll("div")[0].get_text()
		stat = str(stat[:-1])
		if "0-" in stat:
			teamStats[team].append(float(50))
		else:
			teamStats[team].append(float(stat))
		

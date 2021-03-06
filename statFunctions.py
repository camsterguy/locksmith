import criticalFunctions as crit
from datetime import date
import re
import statistics

today = date.today()
thismonth = today.strftime("%m")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

teamStats = {}
ballRefStats = {}

statURL = "https://www.sportsline.com/nba/game-forecast/NBA_"+thisyear+thismonth+thisday+"_"
bballRefURL = "https://www.basketball-reference.com/teams"

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
        try:
            stat = final.findAll("div",)[1].get_text()
            stat = str(stat[:-1])
            teamStats[team].append(float(stat))
        except:
            pass
        
    else:
        final = soup.findAll("div", class_='away-trend')[statnum]
        try:
            stat = final.findAll("div")[0].get_text()
            stat = str(stat[:-1])
            teamStats[team].append(float(stat))
        except:
            pass
        

'''get FG%, 3PT%, FT%. As well as Team Misc stats like effective FG%, Offensive rebound percentage
    defensive rebound percentage. All you can find at https://www.basketball-reference.com/teams/"teamname"(aka BOS or PHI)/2021
    '''
        

# BASKETBALL REFERENCE STATS:

statsToGet = ["fg_pct", "fg3_pct", "ft_pct", "efg_pct", "orb_pct", "drb_pct", "tov_pct"]

def get_TeamStat(team, tdname):
    url = "https://www.basketball-reference.com/teams/"+str(team)+"/2021.html"
    url = url.replace('BKN', 'BRK').replace('CHA', 'CHO').replace('PHX', 'PHO')
    crit.setupHTTP(url)
    from criticalFunctions import soup
    
    table = soup.find("div", {"id": "div_team_and_opponent"})
    miscTable = soup.find("div", {"id": "all_team_misc"})
    
    stat = table.find("td", attrs={"data-stat":tdname})
    miscStat = miscTable.find("td", attrs={"data-stat":tdname})

    if(stat == None):
        return miscStat.get_text()
    else:
        return stat.get_text()

def get_BRStats(team):
    teamBRStats = []
    for stat in statsToGet:
        pulledStat = get_TeamStat(team, stat)

        if(stat == "fg3_pct"):
            three = float(pulledStat)*100
            diff = 50 - three
            if(diff < 0):
                teamBRStats.append(three)
            else:
                teamBRStats.append(50 + diff)

        if(stat == "fg_pct"):
            fg = float(pulledStat)*100
            diff = 50 - fg
            if(diff < 0):
                teamBRStats.append(fg)
            else:
                teamBRStats.append(50 + diff)

        if(stat == "ft_pct"):
            teamBRStats.append((float(pulledStat)*100) - 15)

        if(stat == "efg_pct"):
            teamBRStats.append(float(pulledStat)*100)

        if(stat == "drb_pct"):
            teamBRStats.append(float(pulledStat) - 10)


        '''appending turnover percentage to teamBRStats'''
        if(stat == "tov_pct"):
            teamBRStats.append(50 - (float(pulledStat)*2))

        '''appending offensive rebound percentage to teamBRStats'''
        if(stat == "orb_pct"):
            teamBRStats.append(40 + float(pulledStat))

    return statistics.mean(teamBRStats)





        

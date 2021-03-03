import criticalFunctions as crit
import statFunctions as stat
from datetime import date
import statistics

today = date.today()
month = str((today.strftime("%m"))).lower()
year = (today.strftime("%Y"))
day = (today.strftime("%d"))


scheduleURL = "https://www.basketball-reference.com/leagues/NBA_"+year+"_games-"+month+".html"



crit.get_Spreads(year, month, day)
from criticalFunctions import spreads
crit.get_Games(year, month, day)
from criticalFunctions import hometeams, awayteams


for team in hometeams:
	stat.get_SLine(team)

for team in awayteams:
	stat.get_SLine(team)

from statFunctions import teamStats


print("Slate:")
count = 0
for spread in spreads:
	try:
		print(awayteams[count],(stat.get_BRStats(awayteams[count])+(statistics.mean(teamStats[awayteams[count]])))/2,spreads[count],"@",hometeams[count],(stat.get_BRStats(hometeams[count])+(statistics.mean(teamStats[hometeams[count]])))/2)
		count += 1
	except:
		print("Complete.")







import criticalFunctions as crit
import statFunctions as stat
from datetime import date
import statistics

today = date.today()
month = str((today.strftime("%B"))).lower()
year = (today.strftime("%Y"))


scheduleURL = "https://www.basketball-reference.com/leagues/NBA_"+year+"_games-"+month+".html"


year="2021"
month="02"
day="17"

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
	print(awayteams[count],statistics.mean(teamStats[awayteams[count]]),spreads[count],"@",hometeams[count],statistics.mean(teamStats[hometeams[count]]))
	count += 1



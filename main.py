import criticalFunctions as crit
from datetime import date

today = date.today()
month = str((today.strftime("%B"))).lower()
year = (today.strftime("%Y"))
scheduleURL = "https://www.basketball-reference.com/leagues/NBA_"+year+"_games-"+month+".html"
spreadsURL = "https://mybookie.ag/sportsbook/nba/"

print("Today's Games:",today)

crit.get_Games(scheduleURL)
crit.get_Spreads(spreadsURL)

from criticalFunctions import hometeams, spreads, awayteams
#print(hometeams, spreads, awayteams)
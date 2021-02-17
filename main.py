import criticalFunctions as crit
from datetime import date

today = date.today()
month = str((today.strftime("%B"))).lower()
year = (today.strftime("%Y"))


scheduleURL = "https://www.basketball-reference.com/leagues/NBA_"+year+"_games-"+month+".html"


crit.get_Spreads("2021", "02", "16")
from criticalFunctions import spreads

print(spreads)

crit.get_Games(scheduleURL)
from criticalFunctions import hometeams, awayteams
print(hometeams, awayteams)
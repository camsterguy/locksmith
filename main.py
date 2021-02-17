import criticalFunctions as crit
from datetime import date

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

print("Slate:")
count = 0
for spread in spreads:
	print(awayteams[count],spreads[count],"@",hometeams[count])
	count += 1

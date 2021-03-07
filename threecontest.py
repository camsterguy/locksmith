import criticalFunctions as crit
from datetime import date
import re
import statistics

playerList = ["/t/tatumja01.html", "/c/conlemi01.html", "/c/curryst01.html", "/l/lavinza01.html", "/m/mitchdo01.html", "/b/brownja02.html"]
statURL = "https://www.basketball-reference.com/players"

statsToGet = ["fg3a", "fg3", "fg3_pct", "efg_pct"]

for player in playerList:
	soup = crit.setupHTTP(statURL+str(player))
	playerName = soup.find("h1", attrs={"itemprop":"name"})
	cleanedName = playerName.get_text()

	print(cleanedName)

	threelist = []

	for stat in statsToGet:
		scrapedStat = soup.find("td", attrs={"data-stat":stat}).get_text()
		threelist.append(scrapedStat)

	count = 0
	for stat in threelist:
		print(statsToGet[count]+":",stat)
		count += 1



import criticalFunctions as crit
import statFunctions as stat
from datetime import date
import re
import statistics

today = date.today()
thismonth = today.strftime("%m")
thisday = today.strftime("%d")
thisyear = today.strftime("%Y")

def compareBRStat(team, opponent, statistic):
	teamstat = (stat.get_TeamStat(team, statistic))
	opponentstat = (stat.get_TeamStat(opponent, statistic))

	differential = (str((float(teamstat) - float(opponentstat))*1000)[:5])

	print(float(differential)+50)



compareBRStat("BOS", "ATL", "fg_pct")


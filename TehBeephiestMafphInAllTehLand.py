# -*- coding: utf-8 -*-
import timeit
start=timeit.default_timer()
teamList=[81,135,234,292,461,9135,9234,1646,4028,1747,1781,2171,2197,9197,3487,3814,3865,3940,4103,4272,9272,4284,4485,9485,4926,5822,6721,6451,9926,6721,868,6956]
matchList=[]
pickList=[]
finalTeamScoresList=[]
def addMatch(individualMatch):
    matchList.append(individualMatch)
    
def getOriginalTeamScore(TeamNumber):
    teamScore=0
    for matchNumber in range(0,len(matchList)):
        if TeamNumber in matchList[matchNumber]:
            teamScore+= matchList[matchNumber].index(TeamNumber)
    return teamScore

def getFinalScore(TeamNumber):
    totalTeamScore=getOriginalTeamScore(TeamNumber)
    numberofMatches=0
    teamsBetterThanThem=[]
    for matchNumber in range(0,len(matchList)):
        if TeamNumber in matchList[matchNumber]:
            numberofMatches+=1
            if matchList[matchNumber].index(TeamNumber)==2:
                teamsBetterThanThem.append(matchList[matchNumber][0])
                teamsBetterThanThem.append(matchList[matchNumber][1])
            elif matchList[matchNumber].index(TeamNumber)==2:
                teamsBetterThanThem.append(matchList[matchNumber][0])
    for x in range(0,len(teamsBetterThanThem)):
        totalTeamScore+=getOriginalTeamScore(teamsBetterThanThem[x])
    return totalTeamScore/numberofMatches

def getAllFinalScores():
    for x in range(0,len(teamList)):
        finalTeamScoresList.append(getFinalScore(teamList[x]))
    return finalTeamScoresList

def FillPickList():
    for x in range(0,len(teamList)):
        pickList.append(teamList[finalTeamScoresList.index(min(finalTeamScoresList))])
        finalTeamScoresList[finalTeamScoresList.index(min(finalTeamScoresList))]=100000000000000000000
    return pickList
addMatch([292,4485,9926]) 
addMatch([5822,135,2171]) 
addMatch([9721,6451,9135]) 
addMatch([4028,1234,461]) 
addMatch([4272,3487,4284]) 
addMatch([3814,868,4103]) 
addMatch([3940,1747,81]) 
addMatch([6956,1646,4926]) 
addMatch([234,5484,1781]) 
addMatch([2197,6721,9485]) 
addMatch([868,6956,3865]) 
addMatch([4485,9272,2171]) 
addMatch([2197,1747,9135]) 
addMatch([4272,5822,6721]) 
addMatch([9272,4926,6451]) 
addMatch([4103,292,1781]) 
addMatch([234,1646,4284]) 
addMatch([4028,135,3865]) 
addMatch([3487,5484,3814]) 
addMatch([9721,81,9926]) 
addMatch([461,3940,2171]) 
addMatch([9234,4284,9485]) 
addMatch([4028,5484,6727])  
addMatch([868,4926,135])  
addMatch([4272,3940,9472]) 
addMatch([234,6451,9926]) 
addMatch([4103,4485,9721]) 
addMatch([1646,9485,9135]) 
addMatch([9234,6956,1747]) 
addMatch([2197,292,3814]) 
addMatch([5822,461,1781]) 
addMatch([3487,3865,81]) 
addMatch([135,9272,9135]) 
addMatch([4926,3814,9485]) 
addMatch([4485,4284,6451]) 
addMatch([1747,6721,3487]) 
addMatch([234,5822,9234]) 
addMatch([868,1781,1646]) 
addMatch([4272,3865,292]) 
addMatch([5484,9197,3940]) 
addMatch([4028,2197,6956]) 
addMatch([461,4103,9926])
getAllFinalScores()
stop=timeit.default_timer()
print(FillPickList())

print(stop-start)
#Team Chooser

from random import choice
# import os

players = []
# print(os.getcwd()) Prints current working directory
playersFile = open('Team Chooser/players.txt', 'r')
players = playersFile.read().splitlines()
print(players)

teamA = []
teamB = []
teamC = []

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

    if players == []:
        break

    playerC = choice(players)
    teamC.append(playerC)
    players.remove(playerC)    

teamNames = []
teamNamesFile = open('Team Chooser/teamNames.txt', 'r')
teamNames = teamNamesFile.read().splitlines()

nameA = choice(teamNames)
teamNames.remove(nameA)

nameB = choice(teamNames)
teamNames.remove(nameB)

nameC = choice(teamNames)
teamNames.remove(nameC)

print('Here are your teams:')

print(nameA, teamA)
print(nameB, teamB)
print(nameC, teamC)
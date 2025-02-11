"""
There's an algorithms tournament taking place in which teams of programmers compete against
each other to solve algorithmic problems as fast as possible.
Teams compete in a round robin, where each team faces off against all other teams.
Only two teams compete against each other at a time, and for each competition,
one team is designated the home team, while the other team is the away team.
In each competition there's always one winner and one loser; there are no ties.
A team receives 3 points if it wins and 0 points if it loses.
The winner of the tournament is the team that receives the most amount of points.

Given an array of pairs representing the teams that have competed against each other and an array
containing the results of each competition, write a function that returns the winner of the tournament.
The input arrays are named competitions and results, respectively.
The competitions array has elements in the form of [homeTeam, awayTeam],
where each team is a string of at most 30 characters representing the name of the team.
The results array contains information about the winner of each corresponding competition in the competitions array.
Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array means that the
home team in the corresponding competition won and a 0 means that the away team won.

It's guaranteed that exactly one team will win the tournament and that each team will compete against all
other teams exactly once.
It's also guaranteed that the tournament will always have at least two teams.


Test 1: {"competitions": [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]],
         "results": [0, 0, 1]}
Expected Output: Python

Test 2: { "competitions": [["HTML", "Java"],["Java", "Python"],["Python", "HTML"]],
          "results": [0, 1, 1]}
Expected Output: Java

Test 3: { "competitions": [["HTML", "Java"],["Java", "Python"],["Python", "HTML"],["C#", "Python"],["Java", "C#"],["C#", "HTML"]],
          "results": [0, 1, 1, 1, 0, 1]}
Expected Output: C#

Test 4: {
  "competitions": [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
  ],
  "results": [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
}
Expected Output: C#

Test 5: {
  "competitions": [
    ["Bulls", "Eagles"]
  ],
  "results": [1]
}
Expected Output: Bulls

Test 6: {
  "competitions": [
    ["Bulls", "Eagles"],
    ["Bulls", "Bears"],
    ["Bears", "Eagles"]
  ],
  "results": [0, 0, 0]
}
Expected Output: Eagles

Test 7: {
  "competitions": [
    ["Bulls", "Eagles"],
    ["Bulls", "Bears"],
    ["Bulls", "Monkeys"],
    ["Eagles", "Bears"],
    ["Eagles", "Monkeys"],
    ["Bears", "Monkeys"]
  ],
  "results": [1, 1, 1, 1, 1, 1]
}
Expected Output: Bulls

Test 8: {
  "competitions": [
    ["AlgoMasters", "FrontPage Freebirds"],
    ["Runtime Terror", "Static Startup"],
    ["WeC#", "Hypertext Assassins"],
    ["AlgoMasters", "WeC#"],
    ["Static Startup", "Hypertext Assassins"],
    ["Runtime Terror", "FrontPage Freebirds"],
    ["AlgoMasters", "Runtime Terror"],
    ["Hypertext Assassins", "FrontPage Freebirds"],
    ["Static Startup", "WeC#"],
    ["AlgoMasters", "Static Startup"],
    ["FrontPage Freebirds", "WeC#"],
    ["Hypertext Assassins", "Runtime Terror"],
    ["AlgoMasters", "Hypertext Assassins"],
    ["WeC#", "Runtime Terror"],
    ["FrontPage Freebirds", "Static Startup"]
  ],
  "results": [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
}
Expected Output: AlgoMasters

Test 9: {
  "competitions": [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
  ],
  "results": [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
}
Expected Output: SQL

Test 10: {
  "competitions": [
    ["A", "B"]
  ],
  "results": [0]
}
Expected Output: B
"""

#Solution number 1
def tournamentWinner(competitions, results):
    return_dict = {}
    for ind in range(len(results)):
        team1 = competitions[ind][0]
        team2 = competitions[ind][1]
        if team1 not in return_dict.keys():
            return_dict[team1]=0
        if team2 not in return_dict.keys():
            return_dict[team2]=0
        if results[ind]==1:
            return_dict[team1]+=3
        else:
            return_dict[team2]+=3
    
    return max(return_dict, key=return_dict.get)

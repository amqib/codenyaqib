""" 	Goal
You are a teacher who holds an assessment. After the assessment, you must give your students their score.
Input
'X' means the selected choice
Each answer contains 5 choices of A,B,C,D, and E

Note: If there are two or more selected choices in a question, it is counted as wrong.
Output
One line with the score of your student based on the key and their answer
Constraints
Example
Input
5
ADBCE
XOOOO
OOOXO
OXOOO
OOXOO
OOOOX
Output
100 """

import math

n = int(input())
k = input()
ans = list(k)
new =[]
score = 0 
for a in ans:
    if a == "A":
        new.append("XOOOO")
    if a == "B":
        new.append("OXOOO")
    if a == "C":
        new.append("OOXOO")
    if a == "D":
        new.append("OOOXO")
    if a == "E":
        new.append("OOOOX")

for i in range(n):
    b = input()
    if b == new[i]:
        score = score + 1
    else:
        score = score
print(score*100/n)

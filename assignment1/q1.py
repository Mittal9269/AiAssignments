import sys
from collections import deque

moveI = [1 , -1 , 0 , 0]
moveJ = [0 ,  0, 1,  -1]

def isValid(i , j):
    m = len(lines)
    n = len(lines[0])
    if(i >= 0 and i < m and j >= 0 and j < m and lines[i][j] == ' '):
        return 1
    return 0

def bfs():
    queue = deque([])
    queue.append([0 , 0])
    while(len(queue)):
        temp = queue.popleft()
        if(lines[temp[0]][temp[1]] == "*"):
            return 
        for i in range(4):
            if(isValid(temp[0] + moveI[i] , temp[0] + moveI[i])):
                queue.append([temp[0] + moveI[i] , temp[0] + moveI[i]])

def dfs():
    pass

def dfid():
    pass

file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
 

intital_number = int(Lines[0][0])
Lines = Lines[1:]

lines = [] #main grid
for line in Lines:
    lines.append(line.replace("\n" , ""))

if(intital_number == 0):
    bfs()
elif(intital_number == 1):
    dfs()
else:
    dfid()




    
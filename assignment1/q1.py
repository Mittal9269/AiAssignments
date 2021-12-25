import sys
from collections import deque

moveI = [1 , -1 , 0 , 0]
moveJ = [0 ,  0, 1,  -1]

def isValid(i , j ):
    m = len(lines)
    n = len(lines[0])
    if(i >= 0 and i < m and j >= 0 and j < m and lines[i][j] == ' '):
        return 1
    return 0

def bfs():
    m = len(lines)
    n = len(lines[0])
    queue = deque([])
    queue.append([0 , 0])
    # visited = []
    # for i in range(m):
    #     visited.append([0]*n)
    # visited[0][0] = 1
    while(len(queue)):
        temp = queue.popleft()
        if(lines[temp[0]][temp[1]] == "*"):
            return temp[0],temp[1]

        for k in range(4):
            i ,j = temp[0] + moveI[k] , temp[1] + moveJ[k]
            if(isValid(i , j)):
                queue.append([i , j])
                lines[i][j] = '+'
                # visited[temp[0] + moveI[i]][temp[0] + moveI[i]]


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
    print(bfs())
elif(intital_number == 1):
    print(dfs())
else:
    print(dfid())




    
import sys
from collections import deque
from queue import Queue

moveI = [1 , -1 , 0 , 0]
moveJ = [0 ,  0, 1,  -1]



def isValid(i , j ):
    m = len(lines)
    n = len(lines[0])
    if(i >= 0 and i < m and j >= 0 and j < n and lines[i][j] == ' '):
        # print("somef ")
        return 1
    return 0



def bfs():
    m = len(lines)
    n = len(lines[0])
    # queue = deque([])
    q = Queue(maxsize = m*n)
    q.put([0 , 0])
    visited = []
    for i in range(m):
        visited.append([0]*n)
    visited[0][0] = 1
    # print(visited)
    while(not(q.empty())):
        print("time")
        temp = q.get()
        if(lines[temp[0]][temp[1]] == "*"):
            return temp

        for k in range(4):
            i ,j = temp[0] + moveI[k] , temp[1] + moveJ[k]
            if(isValid(i , j) and visited[i][j] == 0):
                q.put([i , j])
                visited[i][j] = 1

    return -1


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




    
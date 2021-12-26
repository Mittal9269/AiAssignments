import sys
from collections import deque

moveJ = [1, -1, 0, 0]  # movement along the rows
moveI = [0, 0, 1,  -1]  # movement along the columns
# the above combination follows the DURL preference order: Down > Up > Right > Left

def isValid(i, j):
    m = len(lines)
    n = len(lines[0])
    if(i >= 0 and i < m and j >= 0 and j < n and (lines[i][j] == ' ' or lines[i][j] == "*")):
        return 1
    return 0


def PathFind(i, j):
    pathLength = 0
    while(True):
        if(i == 0 and j == 0):
            break
        lines[i][j] = '0'
        pathLength += 1
        i, j = parent[i][j][0], parent[i][j][1]
    lines[0][0] = "0"
    return pathLength


def bfs():
    length = 0
    queue = deque([])
    queue.append([0, 0])
    while queue:
        temp = queue.popleft()
        if(visited[temp[0]][temp[1]] == 1):
            continue
        visited[temp[0]][temp[1]] = 1
        length += 1 
        if(lines[temp[0]][temp[1]] == "*"):
            return temp[0] , temp[1],  length

        for k in range(4):
            i, j = temp[0] + moveJ[k], temp[1] + moveI[k]
            if(isValid(i, j) and visited[i][j] == 0):
                parent[i][j][0] = temp[0]
                parent[i][j][1] = temp[1]
                queue.append([i, j])



def dfs(x , y , length):
    file1.write(str(x) + " " + str(y) + "\n")
    if(lines[x][y] == "*"):
        list_of_dfs[0] = x
        list_of_dfs[1] = y
        list_of_dfs[2] += 1
        list_of_dfs[3] = 1
        
        return

    visited[x][y] = 1
    if(list_of_dfs[3] == 0):
        list_of_dfs[2] += 1 
    for k in range(4):
        i,j = x + moveJ[k], y + moveI[k]
        if(isValid(i , j) and visited[i][j] == 0):
            # print(i , j)
            parent[i][j][0] = x
            parent[i][j][1] = y
            dfs(i , j , length + 1)
        
    


def dfid():
    pass


file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
initial_number = int(Lines[0][0])
file1.close()

Lines = Lines[1:]
length = 0
lines = []

for line in Lines:
    lines.append(line.replace("\n", ""))

temp_line = []
parent = []
visited = []

for i in range(len(lines)):   # creation of the parent matrix
    temp = []
    for i in range(len(lines[0])):
        temp.append([0, 0])
    parent.append(temp)

for i in lines:
    temp_line.append(list(i))
lines = temp_line  # converting lines from string to list data type

file1 = open("output.txt" , "w")
for i in range(len(lines)):
    visited.append([0]*len(lines[0]))

list_of_dfs = [0 , 0 , 0 , 0]

if(initial_number == 0):
    i, j , leng = bfs()
    length = PathFind(i, j)
    length += 1
    print(leng)
    print(length)
    for i in lines:
        i = ''.join(map(str , i))
        print(i)

elif(initial_number == 1):
    dfs(0 , 0 , 0)
    print(list_of_dfs)
    length = PathFind(list_of_dfs[0], list_of_dfs[1])
    length += 1
    print(list_of_dfs[2])
    print(length)
    for i in lines:
        i = ''.join(map(str , i))
        print(i)

else:
    print(dfid())

file1.close()
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
    m = len(lines)
    n = len(lines[0])
    queue = deque([])
    queue.append([0, 0])
    visited = []
    for i in range(m):  # creation of the visited matrix
        visited.append([0]*n)

    while queue:
        temp = queue.popleft()
        if(visited[temp[0]][temp[1]] == 1):
            continue
        visited[temp[0]][temp[1]] = 1
        if(lines[temp[0]][temp[1]] == "*"):
            return temp

        for k in range(4):
            i, j = temp[0] + moveI[k], temp[1] + moveJ[k]
            if(isValid(i, j) and visited[i][j] == 0):
                parent[i][j][0] = temp[0]
                parent[i][j][1] = temp[1]
                if(lines[i][j] == "*"):
                    return i, j
                queue.append([i, j])


def dfs():
    m = len(lines)
    n = len(lines[0])
    stack = deque([])
    stack.append([0, 0])
    visited = []
    for i in range(m):
        visited.append([0]*n)

    while stack:
        temp = stack.pop()
        if(visited[temp[0]][temp[1]] == 1):
            continue
        visited[temp[0]][temp[1]] = 1
        if(lines[temp[0]][temp[1]] == "*"):
            return temp

        for k in range(4):
            i, j = temp[0] + moveI[k], temp[1] + moveJ[k]
            if(isValid(i, j) and visited[i][j] == 0):
                parent[i][j][0] = temp[0]
                parent[i][j][1] = temp[1]
                if(lines[i][j] == "*"):
                    return i, j
                stack.append([i, j])


def dfid():
    pass


file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()
initial_number = int(Lines[0][0])

Lines = Lines[1:]

lines = []

for line in Lines:
    lines.append(line.replace("\n", ""))

temp_line = []
parent = []

for i in range(len(lines)):   # creation of the parent matrix
    temp = []
    for i in range(len(lines[0])):
        temp.append([0, 0])
    parent.append(temp)

for i in lines:
    temp_line.append(list(i))
lines = temp_line  # converting lines from string to list data type

if(initial_number == 0):
    i, j = bfs()
    length = PathFind(i, j)
    length += 1
    print(length)
    for i in lines:
        for j in i:
            print(j, end="")  # note that this works only in python3
        print("\n")

elif(initial_number == 1):
    i, j = dfs()
    length = PathFind(i, j)
    length += 1
    print(length)
    for i in lines:
        for j in i:
            print(j, end="")  # note that this works only in python3
        print("\n")
else:
    print(dfid())

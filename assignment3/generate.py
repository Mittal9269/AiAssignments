import sys
import random

def perClause(n):
    listOfVar = []
    for i in range(-n , n+1):
        if i == 0:
            continue
        listOfVar.append(i)

    sampleClause = []
    for i in range(NumberOfLiteral):
        FirstRand = random.choice(listOfVar)
        sampleClause.append(FirstRand)
        listOfVar.remove(FirstRand)
        listOfVar.remove(-1*FirstRand)

    return sampleClause


    # list = random.sample(list, n)
    # pass

def genClauses(n , k):
    clauseList = []
    i = 0
    while i < k:
        testClause = perClause(n)
        testClause.sort()
        if testClause not in clauseList:
            clauseList.append(testClause)
            i += 1 
    return clauseList

    # pass

n = int(sys.argv[1])
k = int(sys.argv[2])
NumberOfLiteral = 3
Clause = genClauses(n ,k)
# print(Clause)
file = open('input.txt', 'w')
count = 0
for PerClause in Clause:
    string  = ""
    for element in PerClause:
        string += str(element) + " "
    string  = string[:len(string) - 1]
    if (count == len(Clause) - 1):
        file.write(string)
    else:
        file.write(string + '\n')
    count += 1 
file.close()

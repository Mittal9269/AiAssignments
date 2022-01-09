import sys
from collections import deque
import random
from queue import PriorityQueue
import copy
from generate import Clause
from itertools import combinations

def printState(current_state, length):
    print("Current State " + str(length))
    for state in current_state:
        print(state)


def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp
    return(key1)


def Heuristic(Clause , stringOfVar):
    state_value = 0
    for PerClause in Clause:
        for literal in PerClause:
            if int(literal) < 0 and stringOfVar[abs(int(literal)) - 1] == '0':
                state_value += 1 
                break
            if int(literal) > 0 and stringOfVar[abs(int(literal)) - 1] == '1':
                state_value += 1
                break      
    return -1*state_value



def nextGenfunction(string, density):
    neighbour  = []
    allCombinations=list(combinations(range(len(string)),density))
    for combination in allCombinations:
        new_string = string
        for position in combination:
            new_string = string[:position] + str(1 - int(new_string[position])) + string[position+1:] 
        value = Heuristic(Clause , new_string)
        neighbour.append((value, new_string))
    return neighbour
    


def TebuSearch(StringOfVar):
    bestState = StringOfVar
    CandidateOfBestState = StringOfVar
    if(Heuristic(Clause, bestState) == (-1*k)):
        print("First State itself is final state")
        print(bestState)

    tabuList = deque([])
    tabuList.append(bestState)
    limit = 2**(n)

    limitChecker = 0
    while (limitChecker < limit and Heuristic(Clause, bestState) != (-1*k)):
        limitChecker += 1
        print("Visited state " + bestState)
        sNeighborhood = nextGenfunction(CandidateOfBestState, 1)
        CandidateOfBestState = sNeighborhood[0][1]
        for sCandidate in sNeighborhood:
            if sCandidate[1] not in tabuList  and (sCandidate[0] < Heuristic(Clause, CandidateOfBestState)):
                CandidateOfBestState = sCandidate[1]
        
        if (Heuristic(Clause, CandidateOfBestState) < Heuristic(Clause, bestState)):
            bestState = CandidateOfBestState
        tabuList.append(CandidateOfBestState)
        if (len(tabuList) > maxTabuSize):
            tabuList.popleft()

    if(limitChecker >= limit):
        print("Solution don't exist by limit")
        print("best possible state " + str(bestState))
        return False
    print("Found the Solution ")
    print("number of interation " + str(limitChecker + 1))
    return bestState




def VarNeighbourDescent(stringOfVar):
    visited = []
    visited.append(stringOfVar)
    length_path = 0
    checkValue = Heuristic(Clause , stringOfVar)

    density = 1
    if(checkValue == (-1*k)):
        print("Success! Number of states explored are " + str(length_path + 1))
        print(stringOfVar)
        return True
    while(checkValue != (-1*k) and density <= n):
        length_path += 1
        checkValue = Heuristic(Clause , stringOfVar)
        if(checkValue == (-1*k)):
            print("Success! Number of states explored are " + str(length_path))
            print("Final State " + stringOfVar)
            return True
        print("Visited state " + stringOfVar)

        next_Gen_neighbours = nextGenfunction(stringOfVar, density)
        Indicator = False
        for neighbours in next_Gen_neighbours:
            if neighbours[1] not in visited:
                visited.append(neighbours[1])
                if neighbours[0] <= checkValue:
                    Indicator = True
                    checkValue = neighbours[0]
                    stringOfVar = copy.deepcopy(neighbours[1])

        if(checkValue == (-1*k)):
            print(stringOfVar)
            print(length_path)
            return True

        if(Indicator == False):
            density += 1
        else:
            density = 1

        if(density == n):
            print("Stuck at local maxima")
            print("There is no solution for Hill Climbing approach with this Heuristic and number of states explored are " + str(length_path))
            print("Stuck at" + stringOfVar)
            return False

    print("Nothing work check the function")
    return False



def BeamSearch(stringOfVar , beta):
    visited = []
    visited.append(stringOfVar)
    length_path = 0
    checkValue = Heuristic(Clause, stringOfVar)
    open =  PriorityQueue()
    open.put((checkValue , stringOfVar))

    while(not open.empty()):
        length_path += 1
        listOfCandidate = []
        while(not open.empty()):
            topElement = open.get()
            if(topElement[0] == -1*k):
                print("Success! Number of states explored are " + str(length_path))
                print("Final state is " + topElement[1])
                return True
            print("Visited state " + topElement[1])

            next_Gen_neighbours = nextGenfunction(topElement[1], 1)
            for neighbours in next_Gen_neighbours:
                if neighbours[1] not in visited:
                    visited.append(neighbours[1])
                    if neighbours[0] <= topElement[0]:
                        listOfCandidate.append(neighbours)
        listOfCandidate = sorted(listOfCandidate , key = lambda  x : (x[0]))

        if len(listOfCandidate) >= beta:
            for i in range(beta):
                open.put(listOfCandidate[i])
        else:
            for Candidate in listOfCandidate:
                open.put(Candidate)


        if(open.empty()):
            print("Stuck at local maxima " + str(stringOfVar))
            print("There is no solution for Hill Climbing approach with this Heuristic and number of states explored are " +str(length_path))
            return False


# file1 = open(sys.argv[1], 'r')
# Lines = file1.readlines()
# initial_number = int(Lines[0][0])
# file1.close()
print(Clause)
k = len(Clause)
n = int(sys.argv[1])
string = rand_key(n)
print("intial string " + string)
print("\n" + "\n" + "\n")
# print(Heuristic(Clause , string))
print("Performance of Beam Search")
print(BeamSearch(string , 4))
print("#########################-----------------------#############---------------------------------------#################--------------")
print("-------------------------#######################-------------#######################################-----------------##############")
maxTabuSize = 5 
print("\n" + "\n" + "\n")
print("Performance of VND")
print(VarNeighbourDescent(string))
print("#########################-----------------------#############---------------------------------------#################--------------")
print("-------------------------#######################-------------#######################################-----------------##############")
print("\n" + "\n" + "\n")
print("Performance of Tabu Search")
print(TebuSearch(string))
print("#########################-----------------------#############---------------------------------------#################--------------")
print("-------------------------#######################-------------#######################################-----------------##############")
import sys
from collections import deque
import random
from queue import PriorityQueue
import copy
from generate import Clause
from itertools import combinations

def printState(stringOfVar):
    string = ""
    for position in range(len(stringOfVar)):
        if stringOfVar[position] == "0":
            string += "~" +  chr(ord("A") + position) + " "
        else:
            string += chr(ord("A") + position) + " "

    return string


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
        print("First State itself is final state " + printState(bestState))
        print("Total Nodes explored 1")
        print("Total state explored 1")
        return True

    tabuList = deque([])
    tabuList.append(bestState)
    limit = 2**(n)

    print("present State " + printState(CandidateOfBestState))

    limitChecker = 1
    totalStateVisited  = 1
    while (limitChecker < limit and Heuristic(Clause, bestState) != (-1*k)):
        limitChecker += 1
        sNeighborhood = nextGenfunction(CandidateOfBestState, 2)
        CandidateOfBestState = []
        for sCandidate in sNeighborhood:
            totalStateVisited += 1 
            if (sCandidate[1] not in tabuList):
                if len(CandidateOfBestState) == 0:
                    CandidateOfBestState = sCandidate[1]
                else:
                    if(sCandidate[0] < Heuristic(Clause, CandidateOfBestState)):
                        CandidateOfBestState = sCandidate[1]
        
        if len(CandidateOfBestState) == 0:
            print("No Futher Improvement possible stuck at local maxima " + printState(bestState))
            print("total Node explored " + str(limitChecker))
            print("total state explored " + str(totalStateVisited))
            return False
        print("present State " + printState(CandidateOfBestState))

        if  (Heuristic(Clause, CandidateOfBestState) < Heuristic(Clause, bestState)):
            bestState = CandidateOfBestState

        tabuList.append(CandidateOfBestState)
        if (len(tabuList) > maxTabuSize):
            tabuList.popleft()




    if(limitChecker >= limit):
        print("Solution don't exist by limit")
        print("best possible state " + printState(bestState))
        print("total Nodes explored " + str(limitChecker))
        print("total state explored " + str(totalStateVisited))
        return False
    print("Found the Solution " + printState(bestState))
    print("number of interation " + str(limitChecker + 1))
    print("number of States " + str(totalStateVisited + 1))
    return True




def VarNeighbourDescent(stringOfVar):
    visited = []
    visited.append(stringOfVar)
    length_path = 0
    checkValue = Heuristic(Clause , stringOfVar)

    density = 1
    totalStateVisited = 0
    if(checkValue == (-1*k)):
        print("Success! Number of Nodes explored are " + str(length_path + 1))
        print("Success! Number of states explored are " + str(totalStateVisited + 1))
        print("Final state " + printState(stringOfVar))
        return True
    while(checkValue != (-1*k) and density <= n):
        if (density == 1):
            length_path += 1
        checkValue = Heuristic(Clause , stringOfVar)
        if(checkValue == (-1*k)):
            print("Success! Number of Nodes explored are " + str(length_path + 1))
            print("Number of Nodes explored are " + str(totalStateVisited + 1))
            print("Final State " + printState(stringOfVar))
            return True
        print("Present state " + printState(stringOfVar) + " with density " + str(density))

        next_Gen_neighbours = nextGenfunction(stringOfVar, density)
        Indicator = False
        for neighbours in next_Gen_neighbours:
            totalStateVisited += 1
            if neighbours[1] not in visited:
                visited.append(neighbours[1])
                if neighbours[0] <= checkValue:
                    Indicator = True
                    checkValue = neighbours[0]
                    stringOfVar = copy.deepcopy(neighbours[1])

        if(checkValue == (-1*k)):
            print("Final state " + printState(stringOfVar))
            print("Total Nodes explored " + str(length_path + 1))
            print("Total State explored " + str(totalStateVisited + 1))
            return True

        if(Indicator == False):
            density += 1
        else:
            density = 1

        if(density == n):
            print("Stuck at local maxima")
            print("There is no solution for VND approach and number of Nodes explored are " + str(length_path))
            print("There is no solution for VND approach and number of states explored are " + str(totalStateVisited))
            print("Stuck at" + printState(stringOfVar))
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
    totalStateVisited = 1

    while(not open.empty()):
        listOfCandidate = []
        while(not open.empty()):
            length_path += 1
            topElement = open.get()
            if(topElement[0] == -1*k):
                print("Success! Number of Nodes explored are " + str(length_path))
                print("Success! Number of states explored are " + str(totalStateVisited))
                print("Final state is " + printState(topElement[1]))
                return True
            print("Present state " + printState(topElement[1]))

            next_Gen_neighbours = nextGenfunction(topElement[1], 1)
            for neighbours in next_Gen_neighbours:
                totalStateVisited += 1 
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
            print("Stuck at local maxima " + printState(stringOfVar))
            print("There is no solution for Beam search approach  and number of Nodes explored are " +str(length_path))
            print("There is no solution for Beam search approach  and number of states explored are " +str(totalStateVisited))
            return False


# file1 = open(sys.argv[1], 'r')
# Lines = file1.readlines()
# initial_number = int(Lines[0][0])
# file1.close()
print(Clause)
k = len(Clause)
n = int(sys.argv[1])
string = rand_key(n)
print("intial string " + printState(string))
print("\n" + "\n" + "\n")
# print(Heuristic(Clause , string))
print("Performance of Beam Search")
print(BeamSearch(string , int(sys.argv[3])))
print("#########################-----------------------#############---------------------------------------#################--------------")
print("-------------------------#######################-------------#######################################-----------------##############")
maxTabuSize = int(sys.argv[4])
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
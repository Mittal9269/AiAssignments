import random
from queue import PriorityQueue
import copy


def randomGenerate():
    state = [[], [], []]
    random.shuffle(number_list)
    for i in number_list:
        column = random.randint(0, 2)
        state[column].append(i)
    return state

def printState(current_state, length):
    print("current State " + str(length))
    for state in current_state:
        print(state)

def HightHeuristic(current_state, final_state):
    state_value = 0

    length_current_state = len(current_state)
    for stack_position in range(length_current_state):
        length_current_stack = len(current_state[stack_position])

        for element_pos in range(length_current_stack):

            if (len(final_state[stack_position]) > element_pos):

                if(current_state[stack_position][element_pos] == final_state[stack_position][element_pos]):
                    state_value += element_pos + 1

                else:
                    state_value -= (element_pos + 1)

            else:
                state_value -= (element_pos + 1)

    return -1*state_value

def HightSqareHeuristic(current_state, final_state):
    state_value = 0

    length_current_state = len(current_state)
    for stack_position in range(length_current_state):
        length_current_stack = len(current_state[stack_position])

        for element_pos in range(length_current_stack):

            if (len(final_state[stack_position]) > element_pos):

                if(current_state[stack_position][element_pos] == final_state[stack_position][element_pos]):
                    state_value += (element_pos + 1)**2

                else:
                    state_value -= (element_pos + 1)**2

            else:
                state_value -= (element_pos + 1)**2

    return -1*state_value

def StateHeuristic(current_state, final_state):
    state_value = 0

    for number in range(1, 7):

        if(number in current_state[0] and number in final_state[0]):
            if(current_state[0].index(number) == final_state[0].index(number)):
                state_value += 1
            else:
                state_value -= 1

        elif(number in current_state[1] and number in final_state[1]):
            if(current_state[1].index(number) == final_state[1].index(number)):
                state_value += 1
            else:
                state_value -= 1

        elif(number in current_state[2] and number in final_state[2]):
            if(current_state[2].index(number) == final_state[2].index(number)):
                state_value += 1
            else:
                state_value -= 1
        else:
            state_value -= 1

    return -1*state_value





def CallWhichHeurastic(current_state, final_state, index):
    if(index == 1):
        return StateHeuristic(current_state, final_state)

    elif(index == 2):
        return HightHeuristic(current_state, final_state)
    
    else:
        return HightSqareHeuristic(current_state , final_state)


def nextGenfunctionHelper(current_list, index, finalState, WhichHeurestic):
    list_of_neibors = []

    temp_list = copy.deepcopy(current_list)
    last_number = current_list[index][len(current_list[index]) - 1]
    temp_list[index].pop()
    temp_list[(index+1) % 3].append(last_number)
    list_of_neibors.append(
        [CallWhichHeurastic(temp_list, finalState, WhichHeurestic), temp_list])

    temp_list[(index+1) % 3].pop()
    temp_list[(index+2) % 3].append(last_number)
    list_of_neibors.append(
        [CallWhichHeurastic(temp_list, finalState, WhichHeurestic), temp_list])

    # print("dvn" , list_of_neibors)

    return list_of_neibors


def nextGenfunction(current_list, finalState, WhichHeurestic):
    list_of_neibors = []
    if(len(current_list[0])):
        list_of_neibors += nextGenfunctionHelper(
            current_list, 0, finalState, WhichHeurestic)

    if(len(current_list[1])):
        list_of_neibors += nextGenfunctionHelper(
            current_list, 1, finalState, WhichHeurestic)

    if(len(current_list[2])):
        list_of_neibors += nextGenfunctionHelper(
            current_list, 2, finalState, WhichHeurestic)

    return list_of_neibors


def BFS(startState, finalState, WhichHeurestic):

    queu = PriorityQueue()
    heuristic_value = CallWhichHeurastic(startState, finalState, WhichHeurestic)

    queu.put((heuristic_value, startState))
    visited = []
    visited.append(startState)
    length_path = 0

    while(not queu.empty()):

        value_at_top = queu.get()
        length_path += 1
        printState(value_at_top[1] , length_path)

        if(value_at_top[1] == finalState):
            print(length_path)
            return True

        next_Gen_neighbours = nextGenfunction(
            value_at_top[1], finalState, WhichHeurestic)

        for neighbours in next_Gen_neighbours:
            if neighbours[1] not in visited:
                queu.put((neighbours[0], neighbours[1]))
                visited.append(neighbours[1])

    return False


def HillClimbing(startState , finalState, WhichHeurestic):

    # heuristic_value = CallWhichHeurastic(startState, finalState, WhichHeurestic)
    visited = []
    visited.append(startState)
    length_path = 0

    while(True):

        length_path += 1
        printState(startState , length_path)

        if(startState == finalState):
            print(length_path)
            return True

        next_Gen_neighbours = nextGenfunction(startState, finalState, WhichHeurestic)

        queu = PriorityQueue()
        for neighbours in next_Gen_neighbours:
            if neighbours[1] not in visited:
                queu.put((neighbours[0], neighbours[1]))

        if(queu.empty()):
            print(length_path)
            return False

        next_move = queu.get()
        startState = next_move[1]
        visited.append(next_move[1])

        

    return False



number_list = [1, 2, 3, 4, 5, 6]
startState = randomGenerate()
print("random initial state")

for stack in startState:
    print(stack)
print()

finalState = randomGenerate()
print("random Final state")

for stack in finalState:
    print(stack)
print()

# print(HightHeuristic(startState, finalState))
WhichHeurest = 2
print("#######################################################################################################################################")
print("For StateHeuristic Value is ")
print(BFS(startState, finalState, 1))
print("#######################################################################################################################################")
print("For HightHeuristic Value is ")
print(BFS(startState, finalState, 2))
print("#######################################################################################################################################")
print("For HightSqareHeuristic Value is ")
print(BFS(startState, finalState, 3))
print("#######################################################################################################################################")
print()
print()
print("For Hill Climbing in HeightHeuristic vlaue is ")
print(HillClimbing(startState, finalState, WhichHeurest))
print("#######################################################################################################################################")
# print(StateHeuristic(startState, finalState))

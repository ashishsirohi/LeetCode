import Queue
def getSuccessors(maze, currState,currPathValues, currPath):
    removeAllowed = True
    if 1 in currPathValues:
        removeAllowed = False
    succList = list()
    if currState[0]-1 >= 0:
        if (currState[0]-1,currState[1]) not in currPath:
            if maze[currState[0]-1][currState[1]] == 0 or removeAllowed == True:
                newState = (currState[0]-1,currState[1])
                newpathvalue = list(currPathValues)
                newpathvalue.append(maze[currState[0]-1][currState[1]])
                succ = (newState,newpathvalue)
                succList.append(succ)

    if currState[0]+1 <= len(maze)-1:
        if (currState[0]+1,currState[1]) not in currPath:
            if maze[currState[0]+1][currState[1]] == 0 or removeAllowed == True:
                newState = (currState[0]+1,currState[1])
                newpathvalue = list(currPathValues)
                newpathvalue.append(maze[currState[0]+1][currState[1]])
                succ = (newState,newpathvalue)
                succList.append(succ)

    if currState[1]-1 >= 0:
        if (currState[0],currState[1]-1) not in currPath:
            if maze[currState[0]][currState[1]-1] == 0 or removeAllowed == True:
                newState = (currState[0],currState[1]-1)
                newpathvalue = list(currPathValues)
                newpathvalue.append(maze[currState[0]][currState[1]-1])
                succ = (newState,newpathvalue)
                succList.append(succ)

    if currState[1]+1 <= len(maze[0])-1:
        if (currState[0],currState[1]+1) not in currPath:
            if maze[currState[0]][currState[1]+1] == 0 or removeAllowed == True:
                newState = (currState[0],currState[1]+1)
                newpathvalue = list(currPathValues)
                newpathvalue.append(maze[currState[0]][currState[1]+1])
                succ = (newState,newpathvalue)
                succList.append(succ)
    return succList
shortestpath = float("inf")
def findshortestpath(maze):
    startState = (0,0)
    states = list()
    t = (startState,[0],[(0,0)],1)
    states.append(t)
    expandedStates = []
    while len(states) != 0:
        states = sorted(states, key=lambda x:x[3])
        currState, currPathValues, currPath,_ = states.pop(0)
        if currState[0] == len(maze)-1 and currState[1] == len(maze[0])-1:
            return len(currPathValues)

        if currState not in expandedStates:
            expandedStates.append(currState)
            successors = getSuccessors(maze, currState, currPathValues, currPath)
            for succ in successors:
                succState = succ[0]
                succPathValues = succ[1]
                currPath.append(succState)
                states.append((succState, succPathValues,currPath, len(succPathValues)+sum(succPathValues)))
    return 0

def answer():
    maze = [  [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0],
              [1, 1, 1, 1, 1, 0, 1, 1, 0],
              [1, 1, 1, 1, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0] ]
    #maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    print findshortestpath(maze)

answer()
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """ FUNCTIONALITY DESCRIPTION
    takes the problem and the function (1) into the graph search
    """
    #util.raiseNotDefined()
    return graph(problem , 1)
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return graph(problem , 2)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return graph(problem, 3)
    util.raiseNotDefined()
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    """ FUNCTIONALITY DESCRIPTION
    this is technically the same graph but implemented here to avoid complications of
    priority queue with a fucntion. the huristic fucntion is explained in the proceeding 
    """
    
    
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState()) 
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "list of visited nodes"
    visited = []
    node = []
    
    "for A8 the best data structure is priority queue with huristic. the huristic is defiined here"
    frontierPath = util.PriorityQueue()
    firstElem = [(problem.getStartState(), " ")]
    frontierPath.push(firstElem, 0)
   

    while True is True: 
        node = frontierPath.pop()
        for i in range (0,len(node)):
            lenNode = len(node)
  	    lastNode = node[i]
  	lastNodeXY = lastNode[0]
  	
  	returnVal = []
  	for i in range(1,lenNode):
  	    "this loop always keeps the return diection updated to the latest path by taking the values form node and updaing"
  	    nodeXY = node[i]
  	    returnVal.append(nodeXY[1])
      	    
  	    
        if problem.isGoalState(lastNodeXY) is True:
            "if this is the goal, return the value "
  	    return returnVal

 	if lastNodeXY in visited:
            "if lastNodeXY is among the visited then do nothing, it is already visited. This is to avoid redundancy "
 	    #print " XY IS ALREADY IN VISITED LIST! "
 	    pass
  	else:
  	    visited.append(lastNodeXY)
  	    newSucessors = problem.getSuccessors(lastNodeXY)
 	    for ii in range(0, len(newSucessors)):
  	        succ = newSucessors[ii]
  	        if succ[0] in visited:
  	            #print " SUCCESSOR ALREADY ADDED! "
  	            pass
  	             
  	        else :
  	            newSuccPath = []
  	            for i in range(0,len(node)):
  	                newSuccPath.append(node[i])
  	            newSuccPath.append(succ)
  	            cost = 0
  	            for i in range(1,len(newSuccPath)):
  	                passTemp = newSuccPath[i]
  	                cost = cost + passTemp[2]
  	            "for every point cost is calculated as the cumilative distance + ONE huristic "
  	            #print "pass temp", passTemp[0]
  	            cost = cost + heuristic(passTemp[0], problem)
  	            #print "cost", cost
  	            #print "heuristic", heuristic(passTemp[2], problem)
  	            frontierPath.push(newSuccPath, cost)

    
    util.raiseNotDefined()

def graph(problem, inputType):
    """ FUNCTIONALITY DESCRIPTION
    depending on what is the input number it iterats between stack, queue and Priority queue
    and initialize the problem. Then push the first node which is the current node into the frontierPath. 
    from this moment depending on the data structure nodes are pushed and poped from the structure.
    The esiest way to deal with this problem is using the same architecture that the get successor function 
    returns and putting appending all of then in a list and retuning. In this case, there is less hastile dealing
    with stack object. I also implemented a seprate code with just the last node and the whole path but it had etechnical
    issues. then, I changed to this one. I left them commented at the enf of this code
    
    1: Stack         --> good for DFS
    2: Queue         --> good for BFS
    3: PriorityQueue --> good for UCS
    
    PriorityQueue is also good for A* but due to complexity of implementation A* has a separate 
    implemetation 
    
    """
    if   inputType == 1:
        frontierPath = util.Stack()
        
        #firstElem = [(problem.getStartState(), "NA", problem.getStartState(), problem.getStartState())]
        firstElem = [(problem.getStartState(), " ")]
        frontierPath.push(firstElem)
        
    elif inputType == 2:
        frontierPath = util.Queue()
        #firstElem = [(problem.getStartState(), "NA", problem.getStartState(), problem.getStartState())]
        firstElem = [(problem.getStartState(), " ")]        
        frontierPath.push(firstElem)
        
    elif inputType == 3:
        frontierPath = util.PriorityQueue()
        #firstElem = [(problem.getStartState(), "NA", problem.getStartState(), problem.getStartState())]
        firstElem = [(problem.getStartState(), " ")]        
        frontierPath.push(firstElem, 0)
        
        
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState()) 
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    visited = []
    node = []
    

    while True is True:
        "pop value from the frontierPath and put in node" 
        node = frontierPath.pop()
        
        for i in range (0,len(node)):
            lenNode = len(node)
  	    lastNode = node[i]
  	"this is the last node on the list, which will be used for to find sucessors"
  	lastNodeXY = lastNode[0]
  	
  	returnVal = []
  	for i in range(1,lenNode):
  	    "this loop always keeps the return diection updated to the latest path by taking the values form node and updaing"
  	    nodeXY = node[i]
  	    returnVal.append(nodeXY[1])
      	    
  	    
        if problem.isGoalState(lastNodeXY) is True:
            "if this is the goal, return the value. the list is already made up. this is all the W E N S"
  	    return returnVal

 	if lastNodeXY in visited:
            "if lastNodeXY is among the visited then do nothing, it is already visited. This is to avoid redundancy "
 	    #print " XY IS ALREADY IN VISITED LIST! "
 	    pass
  	else:
            "if lastNodeXY is NOT (else) among the visited, then append the node to teh visited and get all sucessor for that point" 
            "since we took the node as a valid sucessor and we are going to add to the frontierPath then it is visited. This is to avoid reaching to the same sucessor and putting it into stack"
            
            visited.append(lastNodeXY)
            
            "here is the list of new sucessors"
  	    newSucessors = problem.getSuccessors(lastNodeXY)
  	    for ii in range(0, len(newSucessors)):
  	        succ = newSucessors[ii]
  	        "if the first value which is the next sucessor is in the visited list then skip"
  	        if succ[0] not in visited:
  	            pass
  	        
  	        if succ[0] in visited:
  	            "if sucsessor is in the visited list then do nothing. this is to avoid redundancy"
  	            #print " SUCCESSOR ALREADY ADDED! "
  	            pass
  	             
  	        else :
  	            "if sucsessor is not in the visited list then a new path(newSuccPath) has to be made for it by taking all nodes of the path and appending the new node. the reason for a new success path is to avoid messing up the path for next sucessor. each time loop is implemented a new set of newSuccPath is made which will be use exclusively for that path "
  	            newSuccPath = []
  	            "this function is similar to the returnVal function. it puts all nodes together and ready for the sucessor to be added"
  	            for i in range(0,len(node)):
  	                newSuccPath.append(node[i])
  	                
  	            newSuccPath.append(succ)
  	            "depending on the input number different data structure will be implemented"
  	            if  inputType==1:
  	                " if the input type is 1, then push for Stack"
  	                frontierPath.push(newSuccPath)
  	            if inputType==2:
  	                " if the input type is 2, then push for priorityQueue"
  	                frontierPath.push(newSuccPath)
  	            if inputType==3:
  	                "if input is 3 do for usc"
  	                cost = 0
  	                "for priority queue, cost is calculated here. cost is calculated as the cost of all steps combined"
  	                for i in range(1,len(newSuccPath)):
  	                    passTemp = newSuccPath[i]
  	                    cost = cost + passTemp[2]
  	                frontierPath.push(newSuccPath, cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


""""
    
    if   inputType == 1:
        frontierPath = util.Stack()
        firstElem = [problem.getStartState(), [], 0]
        frontierPath.push(firstElem)
        
    elif inputType == 2:
        frontierPath = util.Queue()
        firstElem = [problem.getStartState(), [], 0]
        frontierPath.push(firstElem)
        
    elif inputType == 3:
        frontierPath = util.PriorityQueue()
        firstElem = [problem.getStartState(), [], 0]
        frontierPath.push(firstElem)
        
        
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState()) 
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    visitedList = []
    sucessorList = []
    

    while True is True: 
     
        currentNode, currentActionList, huristic  = frontierPath.pop()
        
        #print "NowcurrentNode:", currentNode
        #print "currentActionList", currentActionList
        if problem.isGoalState(currentNode) is True:
            "if this is the goal, append the nodes of the path inti returnVal and return "
  	    return currentActionList
  	
  	visitedList.append(currentNode)
  	#print "visitedList", visitedList    
  	for successors in problem.getSuccessors(currentNode):
  	    #print "successors: ", successors
  	    #print "sucessor: ", successors
  	    newSucessor = successors[0]
  	    newAction   = successors[1]     
  	    newHuristic     = successors[2]
  	    
  	    #print "new action:", newAction
  	    
  	    if newSucessor in visitedList:
  	        #print "here"
  	        pass
  	    else:
  	        
  	        localActionList = []
  	        for i in range (0, len(currentActionList)):
  	            localActionList.append(currentActionList[i])


  	        localActionList.append(newAction)
  	        #print "currentActionList" , currentActionList
  	        appendReturn = [newSucessor, localActionList, 0]
  	        frontier.push(appendReturn)
  	        #visitedList.append(currentNode)
"""

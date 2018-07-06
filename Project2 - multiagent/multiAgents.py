# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        In this part the evaluation function for each node is calculated. In the first
        step the ghost abd food node closest to the current postion is calucated. if the 
        ghost node is located on the current node or it is within a few blocks aways it is 
        assumed as failure. The reason for this decision to scare the pacman to avoid getting
        too close to the closest ghost. By returning the smallest score I am telling pacman
        that this is the worse path. Vicinity of a ghost can be very small >1 or it can be 
        large. It would be very risky to set the vicinity area too close to the ghost since
        pacman can get too close and before it gets to the danger zone it is eaten by ghost.
        On the other hand, of this zone is set to be large, pacman would always keep its distance 
        from the ghost which will increase the run time. if the zone is larger that the size 
        of the maze, this value loses its functionality and all returned values would be 
        -infinity. BTW, -infinity is set to a very small number. a reasonable zone would be
        2 to 4 blocks around ghost, 2 is the most risky and 4 the most conservative. I went 
        with 3 as average.
        
        if the location of ghost and pacman is the same, pacman does not die ONLY IF it has
        already eaten the capsul which means that the ghost time (newScaredTimes[0] ) is and
        pacman is invisible. if the scared time is zero, it is a failure and failEval 
        which is the smallest number is returned.
        
        Assuming ghost is not on the pacman lcoation or is not within the vicinity; 
        if foods are finished (foodLen==0), then +infinity is returned which means tha game is 
        over and goal is achieved. This is the largest return value. 
        
        otherwise the evaluation function is calcualted according to the following function:
        
        EVALUATION = EVALUATION - W1 * MIN_FOOD_DISTANCE + W1 / MIN_GHOST_DISTANCE - W1 * CURRENT_FOOD_NUMBER
        
        food numebr is the most important paramenter and it drives pacman toward directions
        which more food is eaten. NEXT is the nearest food distance. this parameter contains the 
        manimum distance to food. and finally the minimum distance to ghost. 
        
        The initial value of the SUM is set to zero and it really does not matter for this section. 
        this is essentially important for the last section. 
        
        - MIN_FOOD_DISTANCE:
            minimum distance to food deducts from the score. the farther the distance to the nearest food is
            the worse the score. this makes pacman to eat all the foods close to it. 
        - MIN_GHOST_DISTANCE:
            minimum distance to ghost deducts from the score and it is the flip of the minimum distance to the
            ghost. The larger the distance to ghost , the less score is deducted.   
        - CURRENT_FOOD_NUMBER:
            the current number of foods deducts from the final score. so more foods results in worse score.
            this makes pacman to take the route which decreases the number of foods  
        
            
        all these parameters are deducted together with a weight from the initial value. the weight is 
        calcuated manually. Thus, the fewer number of food, the closer to the food and the more distant 
        from the ghost results in a better evaluation result. 
        
        """
        
        #print "successorGameState: ", successorGameState
        #print "newPos: ", newPos
        #print "newFood: ", newFood
        #print "newGhostStates: ", newGhostStates
        #print "newScaredTimes: ",newScaredTimes
 
        failEval = -9999999
        winEval = 9999999
        minDistanceGhost = 9999999
        minDistanceFood = 10000
        ghostWeight   = 100
        foodWeight    = 3
        numFoodWeight = 70
        
        foodList = newFood.asList()
        foodLen = len(foodList)
        
        "this is the terminal state: if win--> return the highest value AND if lose--> return the lowest"
        if currentGameState.isWin():
            return winEval
        if currentGameState.isLose():
            return failEval

        "setting the inital value for the returned value to zero"
        sumEval = 0
        
        "knowing the ghost states lets loop through all of them and find the closest one"
        for i in range(0, len(newGhostStates)):
           #print "successorGameState.getGhostPosition(i+1): ", successorGameState.getGhostPosition(i+1)
           ghostNode = successorGameState.getGhostPosition(i+1)
           ghostDistance = manhattanDistance(newPos , ghostNode)
           if ghostDistance < minDistanceGhost:
              minDistanceGhost = ghostDistance
              updatedGhostNode = ghostNode
        " if the minimum distance to ghost is 3 or 2 or 1 or 0 return a faileur ONLY if the scared time is zero too "   
        if manhattanDistance(newPos,updatedGhostNode)==3 or manhattanDistance(newPos,updatedGhostNode)==2 or manhattanDistance(newPos,updatedGhostNode)==1 or manhattanDistance(newPos,updatedGhostNode)==0 :
           if (newScaredTimes[0] == 0):
               return failEval
        "if all food is consumed, return the best evaluation --> maximize"
        if foodLen == 0 :
           return winEval
           
        " find the minimum distance too food "
        for i in range(0, len(foodList)):
           foodNode = foodList[i]
           foodDistance = manhattanDistance(newPos , foodNode)
           if foodDistance < minDistanceFood:
              minDistanceFood = foodDistance
        
        
        sumEval = sumEval -3 * minDistanceFood - 100 / minDistanceGhost - 70 * foodLen
        #sumEval = sumEval -3 * minDistanceFood + 100 / minDistanceGhost - 70 * foodLen
        #sumEval = 70 * foodLen 
        #print sumEval       
        return sumEval
        return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        instead of defining three functions as 1.the parent 2.the maximizer 
        3.the minimizer. to begine the function I recall it with the currnt 
        following information
        
        minDepth = 1 which is the parent
        maxDepth which is how deep I would search, 
        maxAgent which is the maximum number of agents
        agent = 0 which is the current agent. if 0 means pacman
        gameState which is what it is :-)
        
        the parent of the whole tree is set to 1 so if the tree has max depth 
        of 4, then the tree has 1 parent and 3 children.I made one function 
        called maxMiner wich has three sections:
        
        Section 1:
            this section is at the beginning of each time the fucntion is recalled, 
            and makes sure of the terminal state is achived or not, which is lose 
            or win, and sets agent to zero once agent rolls over and goes larger 
            than the actual number of agents.
            
        Section 2:
            section 2 happens when the agent is agent 0 which is pacman. If that is 
            the case, it should be a maximizer. thus the maximizer value is set to 
            -infinity and ten it recursively recalls itself and increments the agent. 
            we know for sure that all other agents are ghost now. thus next time 
            maxMiner will go to minimizer function since agent > 0. if depth is 1 
            which is the parent node of all tree, it returns the action associated 
            with the best evaluation fucntion. 
        
        Section 3:
            section 3 gets executed only when the current agent is anything but zero 
            which means the current agent is a ghost. in this stage we can have 1 or 
            more agents and all these agents will try to minimize values. The loop 
            will go through all the available actions of the ghost and for any of 
            them finds a sucessor, then agent is incremented and depending on
            one of the three following contitions it recursivelt recalls itself.

            Condition 1:  	if maxAgent - newAgent > 0:
                if the next agent is less than the number of agents, and knowing 
                the current agent is a ghost we are sure that the next stage is 
                also another ghost with the same depth. so the next step would be 
                a minimizer with an incremented agent 
                
            Condition 2:        if maxAgent - newAgent == 0 and depth != maxDepth :
                if the current agent is the last agent, we have decide if it is 
                the leaf or there is another maximizer as the next step. this decision 
                is amde by taking the depth into account. if the depth is NOT the 
                maximum depth then we still have to get deeper which means that the
                next stage will be another ghost  

            Condition 3:        if maxAgent - newAgent == 0 and depth == maxDepth:
                if maximum number of agents is achived and also maximum depth is achived,
                then the next stage will be an evaluation function of the node. this value
                will be returned back to the previous agent and back to top.
            
        """
        "this is the maximum depth"
        maxDepth = self.depth
        "depth of the parent or highest node which is the start point too"
        minDepth = 1
        "maximum number of agents"
        maxAgent = gameState.getNumAgents()
        return self.maxMiner(gameState, minDepth, 0, maxDepth, maxAgent)
       

    def maxMiner(self, state, depth, agent, maxDepth, maxAgent):

        "SECTION 1: TERMINAL STAGE"
        "determinig the winning to losing state "
        if state.isLose(): 
            return state.getScore()
        if state.isWin():
            return state.getScore()

        "set sgent to zero if it axceets the number of agents"
        if agent == maxAgent :
             agent = 0

        "SECTION 2:"
        if agent == 0:
            "set the maximizer value to a -infinity so any other value is larger"
            maximizerVal = -99999999
            for action in state.getLegalActions(agent):
                "get the sucessor"
                sucessor = state.generateSuccessor(agent, action)
                "increment agent for next step"
                newAgent = agent + 1
                "get evaluation function of next steps which is the rest of the ghosts"
                evalFunRet = self.maxMiner(sucessor, depth, newAgent, maxDepth, maxAgent)
                "maxilizing all returned values"
                if evalFunRet > maximizerVal:
                    maximizerVal = evalFunRet
                    minMaxAction = action
            
            "this is the termianl stage for maximizer. if depth is 1 which is the parent of all return action"
            if depth == 1:
                return minMaxAction
            "otherwise return the maximum value"
            return maximizerVal
            
        else: 
            "SECTION 3"      
            "set the minimizer to a maximum value +infinity"
            minimizerVal = 99999999
            "in all avalable action of the current ghost agent find sucessor"
            for action in state.getLegalActions(agent):
                successor = state.generateSuccessor(agent, action)
                "increment agent for next stage. if next stage is leaf this will not be needed"
                newAgent = agent + 1
                
                if maxAgent - newAgent > 0:
                    "condition for next agent as another ghost: keep depth and increment agent"
                    evalFunRet = self.maxMiner(successor, depth, newAgent, maxDepth, maxAgent)

                elif maxAgent - newAgent == 0 and depth != maxDepth :
                    "condition for next stage as a pacman: increment depth and increment agent"
                    newDepth = depth + 1
                    evalFunRet = self.maxMiner(successor, newDepth, newAgent, maxDepth, maxAgent)
                    
                elif maxAgent - newAgent == 0 and depth == maxDepth:
                    "condition for the next stage as the leaf. just get the evaluation function !!!"
                    evalFunRet = self.evaluationFunction(successor)
                   
                "this is the minimizing stage"   
                if evalFunRet < minimizerVal:
                    minimizerVal = evalFunRet

            return minimizerVal

        util.raiseNotDefined()
    
        
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        this function is essentially the same as the MaxMini but instead of minimizing 
        the values it takes an average of all returned values.
    
        """
        maxDepth = self.depth
        minDepth = 1
        maxAgent = gameState.getNumAgents()
        return self.maxMiner(gameState, minDepth, 0, maxDepth, maxAgent)

    def maxMiner(self, state, depth, agent, maxDepth, maxAgent):
       
        if state.isLose(): 
            return state.getScore()
        if state.isWin():
            return state.getScore()
        
        if agent == maxAgent :
             agent = 0

        if agent == 0:
            maximizerVal = -99999999
            for action in state.getLegalActions(agent):
                sucessor = state.generateSuccessor(agent, action)
                newAgent = agent + 1
                evalFunRet = self.maxMiner(sucessor, depth, newAgent, maxDepth, maxAgent)
                if evalFunRet > maximizerVal:
                    maximizerVal = evalFunRet
                    minMaxAction = action
            
            if depth == 1:
                return minMaxAction
            return maximizerVal
      
        else: 
            sumAverage = 0
            i = 0
            for action in state.getLegalActions(agent):
                "increments the number of possible actions which will be used as denominator"
                i = i + 1
                successor = state.generateSuccessor(agent, action)
                newAgent = agent + 1
                
                if maxAgent - newAgent > 0:
                    evalFunRet = self.maxMiner(successor, depth, newAgent, maxDepth, maxAgent)

                elif maxAgent - newAgent == 0 and depth != maxDepth :
                    newDepth = depth + 1
                    evalFunRet = self.maxMiner(successor, newDepth, newAgent, maxDepth, maxAgent)
                    
                elif maxAgent - newAgent == 0 and depth == maxDepth:
                   evalFunRet = self.evaluationFunction(successor)
                "summing all values"   
                sumAverage = sumAverage + evalFunRet
            
            "taking average"
            returnVal = float(sumAverage)/i

            return returnVal

        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    
    """ FUNCTIONALITY DESCRIPTION
    this is essentially the same as the original evaluation fucntion with a few
    parameters added. There are a number of parameters that I brainstormed and
    I added them one after the other to improve the function. I gave up once I got
    the full mark. Thus some of these factors were not reflectd in the evaluation 
    fucntion. Here are all the possible factors:
    
        -- current score: this is the biggest improvement. since we lose point 
           if pacman is stationaly, the initial evaluation fucntion is set to 
           score and the rest of the following criteria will deduct or add to it.
        
        -- minimum distance to the ghost: this should always be maximized. In 
           other word, the larger the better. 
    
        -- minimum distance to food: this criteria should be minimized and should 
           lead pacman to preferably focus on the foods around.
            
        -- number of foods: this factor should be minimized. In other words, pacman 
           should take the route which minimizes this. 
           
        -- scared time: scared time is a helping factor which means that it should 
           be minimized. the more scared time the more flexible pacman is
        
        -- number of capsules: number of capsules is related to scare time and the 
           fewer number of capsuler the more flexible the pacman is. in other words, 
           more casules mean more invisible pacman and more flexible action,.
           
        -- minimum distance to capsules: since capsules are helpful we should get 
           as close as possible to them to consume them and act with flexibility.
           
    the evaluation finction is:

    Eval = Score - W1*minDistanceFood  - W2*foodLen - W2/minDistanceGhost 
    
    this is essentially the same as the first one with just score added. these 
    numbers were found manually with a lot of trial and error. There are a few more
    considerations that are listed bellow:   
        
        1. I limited the danger zone around pacman to only 2 tiles
        2. If the distance to ghost is really far I set the minDistanceGhost to be 2.
           if this value is larger than 3, I set to a contant value to keep its eefect.
           Considerin the risky danger zone, I'd like to keep a constant value if ghost
           is more than 3 tiles away and only increase it once it is really close. BTW
           if ghost is really close, the return will be -infinity   
      
    
     
    """
    
    failEval = -9999999
    winEval = 9999999
    minDistanceGhost = 9999999
    minDistanceFood = 10000
    ghostWeight   = 100
    foodWeight    = 3
    numFoodWeight = 70
    
    newFood = currentGameState.getFood()
    foodList = newFood.asList()
    foodLen = len(foodList)
     
    if currentGameState.isWin():
        return winEval
    if currentGameState.isLose():
        return failEval


    sumEval = scoreEvaluationFunction(currentGameState)
    ghostNum = currentGameState.getNumAgents() 
    #print "XXXXX: ", ghostNum
        
    for i in range(1, ghostNum):
       #print "successorGameState.getGhostPosition(i+1): ", successorGameState.getGhostPosition(i+1)
       ghostNode = currentGameState.getGhostPosition(i)
       newPos = currentGameState.getPacmanPosition()      
       
       ghostDistance = manhattanDistance(newPos , ghostNode)
       if ghostDistance < minDistanceGhost:
          minDistanceGhost = ghostDistance
          updatedGhostNode = ghostNode
       "setting constant if ghost is too far"
       if minDistanceGhost>3:
          minDistanceGhost = 2
    

    if manhattanDistance(newPos,updatedGhostNode)==2 or manhattanDistance(newPos,updatedGhostNode)==1 or manhattanDistance(newPos,updatedGhostNode)==0 :
       return failEval

    if foodLen == 0 :
       return winEval

    for i in range(0, len(foodList)):
       foodNode = foodList[i]
       foodDistance = manhattanDistance(newPos , foodNode)
       if foodDistance < minDistanceFood:
          minDistanceFood = foodDistance
    
    sumEval = sumEval - 2.5*minDistanceFood  - 4*foodLen - 30/minDistanceGhost   #this works  too!                                                                                                               
    #sumEval = sumEval - 2.5*minDistanceFood  - 4*foodLen - 2*minDistanceGhost   #this works!
    #sumEval = sumEval - 3*minDistanceFood  - 6*foodLen - 1.5*minDistanceGhost
    #sumEval = sumEval -3 * minDistanceFood - 100 / minDistanceGhost - 70 * foodLen
    #sumEval = 70 * foodLen 
    #print sumEval       
    return sumEval
    return successorGameState.getScore()

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction


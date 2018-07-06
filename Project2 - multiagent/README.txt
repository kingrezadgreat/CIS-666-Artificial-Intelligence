Name: Reza Shisheie
CSU ID: 2708062
Project1

I put 35+ hours on the project. 

Here is the description for everyone of the fucntions. Please refer to the code for complete explanation of each sement
and also comments. 


class ReflexAgent(Agent):
    def evaluationFunction(self, currentGameState, action):
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



class MinimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
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




class ExpectimaxAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        this function is essentially the same as the MaxMini but instead of minimizing 
        the values it takes an average of all returned values.
    
        """
def betterEvaluationFunction(currentGameState):
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


# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math,time

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    "---------------------------------------------------------------------------Question 4"
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        here I just initilize the dictionary
        """
        self.qDict = util.Counter()

    "---------------------------------------------------------------------------Question 4"
    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        first I generate the dual composition of current state and next 
        action. This is the actual format of the Q matrix. In Q matrix for 
        each state, there are maximum of 4 actions for this problem an for 
        each one of them there is an associated value which is the Q value. 
        Thus, the Q matrix has maximum of 4 different values for 4 different 
        actions for each single state.
        
          1. if the dual-value of (state, action) is already in the qDict, 
             it means that it was already seen and thus there is an a value 
             associated with that which has already been initilized. The 
             return value in this case would be the value associated with 
             the (state, action)
             
          2. if the (state, action) is not in the qDict, it means that it 
             was not seen before and since it is the first time it is being 
             seen, the value should be 0.0. The return value in this case 
             would be the initialized value which is 0.0
        
        """
        "the two-variable value is initilized here"
        qDictComp = (state, action) 
        
        if qDictComp in self.qDict:
           "if seen before --> just return the value which was calculated before"
           #print "do nothing!"
           return self.qDict[(state, action)]
           
        else :
           "if not seen before --> update the value in Q and return 0.0 as initialized"
           self.qDict[(state, action)] = 0.0
           return 0.0
 
        util.raiseNotDefined()
        util.raiseNotDefined()

    "---------------------------------------------------------------------------Question 4"
    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION        
        for this section actionListis generated which stores all avauilabe 
        actions. 
        
          1. if the lengt of qValList is still equal to the initilized 
             value, which is zero --> retrn 0.0 as the maximum value. 
             The reason behind this decision is that there were no legal 
             actions avaialbe, and thus there were no Q value. thus for 
             all assumed actions there should be only zero.
        
          2. if there are legal actions availabel from the "getLegalActions", 
             then put all of them in the actionList and then find te maximum
             value among them and return return.
        
        
        """
        actionList = self.getLegalActions(state)
        qValList = []
        
        "append all legal actions to actionList"
        for actions in actionList:
          qValList.append(self.getQValue(state, actions))
        "if qValList is still empty, there is not legal action-->return 0 as best Q"
        if len(qValList)==0:
           #print " "
           return 0.0
           "if there are values in qValList then find maximum and return"
        else: 
           maxQVal = qValList[0]
           for i in range (0,len(qValList)):
              if qValList[i] > maxQVal:
                 maxQVal = qValList[i]
           return maxQVal 
        
        
        util.raiseNotDefined()
        util.raiseNotDefined()

    "---------------------------------------------------------------------------Question 4"
    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION        
        like "computeValueFromQValues", we find the maximum value for Q
           1. if there is no value found for qValList then the action
              associated with it would be None
           2. if there is a maximum value for Q, then teh return action 
              would be the one associated with the maximum value of Q 
              for that state
        """        
        actionList = self.getLegalActions(state)
        #print actionList  
        
        qValList = []
        qActionList = []
        maxQVal = 0
        actQVal = None

        for actions in actionList:
          qValList.append(self.getQValue(state, actions))
          qActionList.append(actions)
        
        #print actionList  
        #print qValList, actionList
        
        if len(qValList)==0:
           actQVal = None
           return None
        
        else: 
           maxQVal = qValList[0]
           actQVal = qActionList[0]
           for i in range (0,len(qValList)):
              if qValList[i] > maxQVal:
                 maxQVal = qValList[i]
                 actQVal = qActionList[i]
           
           #print "actQVal:      ", actQVal  
           #print qValList, actionList
           #print " "
           return actQVal 
        
        util.raiseNotDefined()
        util.raiseNotDefined()     
       
  

    "---------------------------------------------------------------------------Question 5"
    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION        
        in this section probablity of the expsilon value is put in prob. 
        then the value of util.flipCoin(prob) is calcualted and put into
        the "oldOrNew" variable. this variable says what the result is 
        if the you flip a coin with probability of epsilon. the results 
        can be eitehr 0 or 1.
         
           1. if the result is 1 --> we will randonly choose from the list
              of legal actions and return one of them.
           2. if the resukt is 0--> we will compute the action for that 
              state using "computeActionFromQValues" which finds the maximum
              value of Qs for that state and then returns the actions associated 
              with that Q value. 
              
         once the action is computed:
           1. if there is nothing in the legalActions list (len(legalActions)==0),
              we will return "None" as the action. This is the terminal state
           2. if there is something in the legalActions (len(legalActions)!=0), we
              return the calculated action    
              
        """        
        prob = self.epsilon
        "calcualte if coin is 1 or 0"
        oldOrNew = util.flipCoin(prob)
        if oldOrNew == 1:
           "if it is 1 then pick one random action from the action list"
           action = random.choice(legalActions)
        else:
           "if it is 0 then find the action associated with the maximum value of Q"
           action = self.computeActionFromQValues(state)
         
        
        if len(legalActions)==0:
          "if the action list is empty return None as terminal state action"
          return None
        else:
          "if the action list is not empty retun the calculated action above"
          return action

        util.raiseNotDefined()
        util.raiseNotDefined()
 
        return action

    "---------------------------------------------------------------------------Question 4"
    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION        
        this is the update section. here are the explanation of all values:
        
           vCurrent : the value of V for the current state
           vNext    : the value of V for the next state taking a particular action 
        
           ALPHA    : learning rate or the rate toward weighting old values
           Gamma    : discount factor
           R        : reward
           
        having these values i can update Q
        
        """

        vCurrent = self.getQValue(state,action)
        vNext = self.computeValueFromQValues(nextState)
        
        ALPHA = self.alpha
        Gamma = self.discount
        R = reward
        
        sample = R + Gamma*vNext
        self.qDict[(state,action)] =  (1-ALPHA) * vCurrent + ALPHA * sample
        
        #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()
        

    def getWeights(self):
        print self.weights
        print ""	
        return self.weights
        
    "---------------------------------------------------------------------------Question 8"
    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION        
        this function gets all the features of a (state,action) and stores 
        them in "features". Then it goes into a loop of all elements of 
        "featrue" and one by one it extracts the following two elements
        
            - feature[i]
            - self.weights[i]
        
        here is a list of important notes:
        
           1. note that i is a counter but it actually is one of the 
              elements of "feature" and is liek ((2,1),"north").
        
           2. note that "self.weights" is already initialized in 
              "def __init__", above as a dictionary:
                  
                  self.weights = util.Counter()
              
           3. features are also initialized as dictionary in "featExtractor" 
              library.
        
                 features = util.Counter()
           
           4. "self.featExtractor.getFeatures(state, action)" is defined 
              in the "featExtractor" library as:
                 
                 def getFeatures(self, state, action):
                    # extract the grid of food and wall locations and get the ghost locations
                    food = state.getFood()
                    walls = state.getWalls()
                    ghosts = state.getGhostPositions()
                    features = util.Counter()
                    
              and is pulled into this class in the __init__ by:
              
                 self.featExtractor = util.lookup(extractor, globals())()
        
        
        NOW, back to the function itself: 
        once we have all features, we would loop through the features and multiply
        weight by feature and sum them to Q: 
        
           Q(s,a)=ZIGMA( fi(s,a)*wi )
        
        if in case W is not initialized (a feature is not in self.weights), I
        would initilized that value to 0.0

        
        """        
        Q_sa = 0    
        
        "extract dictionary list of features"
        feature = self.featExtractor.getFeatures(state, action)
        #print "" 
        #print "  ", state, action
        #print "  ", self.weights
        #print "  ", feature
        #time.sleep(.01)
        
        "iterate through the features make sure all W s have value or initialized"
        for s in feature:
          
           "if a feature is met in W or if a feature does not exist in W, then intitilize to zero" 
           if s not in self.weights:
              self.weights[s] = 0.0
              #print "No"
   
        "iterate through the features and take the sum of multiplications"        
        for i in feature:
     
          #print "  ","  ", i , feature[i],   self.weights[i]  
           Q_sa = Q_sa + feature[i] * self.weights[i] 
        
        return Q_sa
        
        util.raiseNotDefined()
        
    "---------------------------------------------------------------------------Question 8"
    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION        
        here I update the weights by extracting ALPHA, GAMMA, R, and etc. then,
        max Q of current state and next state are extracted.
           
           - note that the Q value of the current state is calculated using
             "getQValue(state, action)" in whcih Q value is maximized between 
             all Q values of all 4 actions and returned '
             
           - However, the Q value of the next state is calculated using 
             "getValue(nextState)" which is just depandant of the state of the 
             nextState. invoking "getValue" invokes "computeValueFromQValues" which
             invokes "getQValue" which gets all Q values of a state and maximizes them.
             
        one of the mistakes I made in this section was putting the difference value in the
        for loop which causes difference to update in each for loop. I figured difference
        should be outside as a constant for the for loop
        
        """
        feature = self.featExtractor.getFeatures(state, action)
        
        ALPHA = self.alpha
        GAMMA = self.discount
        R = reward
        
        "Q value for the current state and max of next state "
        maxQNext = self.getValue(nextState)
        maxQCurr = self.getQValue(state, action)
        
        "find the difference"
        difference = R + GAMMA * maxQNext - maxQCurr
        
        for i in feature:
           " the following is wrong! if implemented it would update difference everytime "
           #difference = R + GAMMA * maxQNext - maxQCurr    
           self.weights[i] = self.weights[i] + ALPHA * difference * feature[i]

        #util.raiseNotDefined()
        

    "---------------------------------------------------------------------------Question 8"
    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            print "weight: ", self.weights
            print " "
            print " "
            pass

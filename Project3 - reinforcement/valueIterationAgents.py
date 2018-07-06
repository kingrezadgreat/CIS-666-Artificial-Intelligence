# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        in this section the summation of all qValues for each state and 
        each action is calculated and then summed together according to the 
        following equation:
           
           qSum = qSum + T * (R + Gamma*V) 
           
        in order to do that dictRet as a dictionary is made which keeps track
        of all states and its values for each iteration. Obviously as more and 
        more iterations are advanced, the numbers in dictRet will converge. 
        
        as mentioned above this algorithm is implemented for the number of 
        iterations. 
        1. if the terminal state is reached set the value of TERMINAL_STATE 
           to zero
        2. if the state is not the termianl state, then one of the 4 valid 
           actions get the probability of moving toward that direction and noise
           as well as the next step if that actions is taken. here is an 
           explanation of the definition of variables;
              
              nextState = the location of next state 
              T 	= transition fucntion or the probability of that action taken
              R		= reward function or how much reward you acquired
              Gamma	= discount or how much you loose in each step
              V		= value of next state 
           
           summing all of the qValues and then putting them into a list make a 
           list of all qValues for 4 possibel actions. then we only pick the 
           largest value since we want to maximize reward. then the maximum value 
           is returned
        
        """

        dictRet = util.Counter()

        for i in range(0,iterations):
           "make the dictRet as a dictionary which keeps track of values of all states in each iteration" 
           dictRet = util.Counter()
           #print self.mdp.getStates()
           for state in self.mdp.getStates():
              "if terminal state is true then set the value of TERMINAL_STATE to zero or min value"
              if self.mdp.isTerminal(state) is True:
                 #print state
                 dictRet[state] = 0
              "if terminal state is not achived we can calculate the q values"
              if self.mdp.isTerminal(state) is False:
                 "the list that keeps all Qs for all directions"
                 qSumList = []
                 for action in self.mdp.getPossibleActions(state):
                    qSum = 0
                    for TSAP in self.mdp.getTransitionStatesAndProbs(state,action):
                       nextState = TSAP[0]
                       T = TSAP[1]
                       R = self.mdp.getReward(state,action,nextState)
                       Gamma = self.discount
                       V = self.values[nextState]
                       #print T, R, Gamma, V
                    
                       qSum = qSum + T * (R + Gamma*V)

                    "adding the summation of all Qs for that state taking an action as default the default action"
                    qSumList.append(qSum)
                 "finding maximum value of all summations"
                 maxVal = qSumList[0]
                 for i in range (1,len(qSumList)):
                    if (qSumList[i]>maxVal):
                       maxVal = qSumList[i]
                 "returning max value of all qSums and updating the qSum value of that state "
                 dictRet[state] = maxVal
           "return all distret values"
           self.values = dictRet


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        this function calculates the qValue for each action by 
        taking the Transition state and its probabilies and plug 
        then ino the following equation:
              
              qSum = qSum + T * (R + Gamma*V) 
              
        and taking all summations of all qvalues and finally returning teh value
        
        """
        qSum = 0
        for TSAP in self.mdp.getTransitionStatesAndProbs(state,action):
           nextState = TSAP[0]
           T = TSAP[1]
           R = self.mdp.getReward(state,action,nextState)
           Gamma = self.discount
           V = self.values[nextState]
                   
           qSum = qSum + T * (R + Gamma*V)
        return qSum
        util.raiseNotDefined()


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        """ FUNCTIONALITY DESCRIPTION
        this functions return the policy associated with the maximum 
        qValue for all actions of a particular state. it saves all qValues 
        and actions (as policy) into a list and then iterates in the list
        to find the maximum value and return the associated action (policy).
        
        as mentioned above if terminal state is reached the return value should
        be None        
        
        """
        "if NO terminal state "        
        if self.mdp.isTerminal(state) is False:
           "two recording Lists" 
           valList = []
           actionList = []
           for action in self.mdp.getPossibleActions(state):
              QValue = self.computeQValueFromValues(state, action)
              "adding qvalue and actions into the lists"
              valList.append(QValue)
              actionList.append(action) 
           
           "finding the maximum qValue and saving both value and action"
           valTemp = valList[0]
           actionTemp = actionList[0]
           for i in range (1, len(valList)):
              if (valList[i]>valTemp):
                 valTemp = valList[i]
                 actionTemp = actionList[i]
           
           "return the actions associated with the maximum qvalue"
           return actionTemp
           util.raiseNotDefined()
        "if terminal state --> return None"        
        return None
        
 
 
    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

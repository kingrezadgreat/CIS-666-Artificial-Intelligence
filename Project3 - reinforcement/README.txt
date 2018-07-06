Name: Reza Shisheie
CSU ID: 2708062
Project3

I put 20+ hours on the project. 

Here is the description for everyone of the fucntions. Please refer to the code for complete explanation of each sement
and also comments. 


class ValueIterationAgent(ValueEstimationAgent):
    def __init__(self, mdp, discount = 0.9, iterations = 100):
    
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



    def computeQValueFromValues(self, state, action):
        """ FUNCTIONALITY DESCRIPTION
        this function calculates the qValue for each action by 
        taking the Transition state and its probabilies and plug 
        then ino the following equation:
              
              qSum = qSum + T * (R + Gamma*V) 
              
        and taking all summations of all qvalues and finally returning teh value
        
        """
        
        
        
    def computeActionFromValues(self, state): 
        """ FUNCTIONALITY DESCRIPTION
        this functions return the policy associated with the maximum 
        qValue for all actions of a particular state. it saves all qValues 
        and actions (as policy) into a list and then iterates in the list
        to find the maximum value and return the associated action (policy).
        
        as mentioned above if terminal state is reached the return value should
        be None        
        
        """

def question2():
    """ FUNCTIONALITY DESCRIPTION
    the goal is to change only ONE of the discount and noise parameters 
    so that the optimal policy causes the agent to attempt to cross the 
    bridge.
       
    The only solution would be settin noise to zero. Noise refers to how 
    often an agent ends up in an unintended successor state when they 
    perform an action and by setting it to zero (answerNoise = 0.0) 
    I am forcing the pacman to only take the forward action and take
    no unintended action 
    """
         


class QLearningAgent(ReinforcementAgent):
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


    def computeValueFromQValues(self, state):
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
  

    def computeActionFromQValues(self, state):
        """ FUNCTIONALITY DESCRIPTION        
        like "computeValueFromQValues", we find the maximum value for Q
           1. if there is no value found for qValList then the action
              associated with it would be None
           2. if there is a maximum value for Q, then teh return action 
              would be the one associated with the maximum value of Q 
              for that state
        """        
  

    def getAction(self, state):
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
   

    def update(self, state, action, nextState, reward):
        """ FUNCTIONALITY DESCRIPTION        
        this is the update section. here are the explanation of all values:
        
           vCurrent : the value of V for the current state
           vNext    : the value of V for the next state taking a particular action 
        
           ALPHA    : learning rate or the rate toward weighting old values
           Gamma    : discount factor
           R        : reward
           
        having these values i can update Q
        
        """



class ApproximateQAgent(PacmanQAgent):
    def getQValue(self, state, action):
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
     

    def update(self, state, action, nextState, reward):
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
   













































   
























  
  
         




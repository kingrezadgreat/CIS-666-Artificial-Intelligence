Name: Reza Shisheie
CSU ID: 2708062
Project4

I put 35+ hours on the project. 

Here is the description for everyone of the fucntions. Please refer to the code for complete explanation of each sement
and also comments. 



Question 1: Bayes net structure

def constructBayesNet(gameState):
    """FUNCTIONALITY
    in this section structure of the Bayesnet is made. for the first section, all
    observations are made through the following alorithm mentioned in the description
    above:
    
        for housePos in gameState.getPossibleHouses():
            for obsPos in gameState.getHouseWalls(housePos)
                obsVar = OBS_VAR_TEMPLATE % obsPos
                
    Then all edges are added. for each X_POS_VAR and Y_POS_VAR, there are two options of 
    FOOD_HOUSE_VAR which contains food and GHOST_HOUSE_VAR whcih contains ghost. these 4
    values can be added to the edge manually and then all other possible edges based on the 
    observation is added consequently. This implementation is based on the two X_POSITION
    and Y_POSITION are connected to FoodHouse and GhostHouse and thus 4 possibilities are
    availabe. 
    
    
    The same process is made for the variableDomainsDict too. first all possible values
    are added manually and then based upon observations all other observation values are
    added. these values can be [BLUE_OBS_VAL, RED_OBS_VAL, NO_OBS_VAL] for any observation
    point.

    """
    
   
    
    
    
Question 2a: Bayes net probabilities

def fillYCPT(bayesNet, gameState):
    """ FUNCTIONALITY
    here all 4 possibilies BOTH_TOP_VAL, BOTH_BOTTOM_VAL, LEFT_TOP_VAL, and LEFT_BOTTOM_VAL
    are linked to their position. this is related to the 4 possibilieties set manually.
    """





Question 2b: Bayes net probabilities

def fillObsCPT(bayesNet, gameState):
    """ FUNCTIONALITY
    this section is dedicated to the probability distribution of the following
    
    			food house	ghost house 
    			      \         /
    			       \       /
    			      observation 
    
    for each food house and ghost house there are 4 possibiliers:
        topLeft, topRight, bottomLeft, bottomRight
    and for each observation there are 3 possibilies:
    	red, blue, none
    multiplying all three values 4*4*3 = 48, there are 48 possibilies for 
    each obsevation. Not all of them are necessaryly have a probability (prob)
    
    in order to get the probability of values I loop through the housePos 
    and obsPos as mentioned in problem 1
 
 	    for housePos in gameState.getPossibleHouses():
        	for obsPos in gameState.getHouseWalls(housePos):
 	            obsVar = OBS_VAR_TEMPLATE % obsPos
    
    and get al values and put them into the factor function. this function is 
    mentioned in the bayesNet.py and is consists of:
    
        Factor(inputUnconditionedVariables, inputConditionedVariables, inputVariableDomainsDict):
    		inputUnconditionedVariables:	observations: 	obsVar
    		inputConditionedVariables:	two parents: 	FOOD_HOUSE_VAR, GHOST_HOUSE_VAR	
    		inputVariableDomainsDict: 	domain:		bayesNet.variableDomainsDict()
    
    once the factor is constructed, all possibilies of the current structure 
    can be extracted using the following command:
    	obsCPT = factor.getAllPossibleAssignmentDicts()
    
    this command give me all permutation of the uncondition and condition variabels
    which is 4*4*3 = 48 
    
    now that al possibiliets are available we would loop through obsCPT and 
    examin each one of them. since we are only intersted in the 9 blocks around
    each house, we only take the manhattan distance of the current observation 
    position (obsPos) and each of the houses (bottomLeftPos, etc...) and if any 
    of them is less than 3, then that the observation is adjacent to that houose
    location and consequently, the VAL of that location is saved into 'closestHouse'. 
    the default value of 'closestHouse' is None and if observation is not close 
    to any of the houses, then the closestHouse would be default which is Noen. 
    
    Now it is time to do probability. the default probability is ZERO unless 
    proven
    
    	1. If the adjacent house center is occupied by neither the ghost house or 
    	   the food house, an observation is none with certainty (probability 1).
    	2. If the adjacent house center is occupied by the food house, it is red 
    	   with probability PROB_FOOD_RED and blue otherwise.
    	3. If the adjacent house center is occupied by the ghost house, it is red 
    	   with probability PROB_GHOST_RED and blue otherwise.
    	4. If the adjacent house center is occupied by the ghost house and food house,
    	   it is red with probability PROB_FOOD_RED and blue otherwise. the structure 
    	   of the Bayes Net means that the food house and ghost house might be assigned 
    	   to the same position. This will never occur in practice. But the observation 
    	   CPT needs to be a proper distribution for every possible set of parents. In 
    	   this case, you should use the food house distribution.
    	5. else --> probe =0
    
    finally factor is updated by factor.setProbability(eachCPT, prob) for each CPT line
    and probability of that section and bayesNet is updated by bayesNet.setCPT(obsVar, factor)    
    
    """
    
   
    


Question 3: Your join implementation 

def joinFactors(factors):
    """FUNCTIONALITY
    assume that the variableDomainsDict for all the input factors are the same,
    it is imported using the "factors[1].variableDomainsDict()" function. any of
    the inputs in this function would work.
    
    then, I would loop through all the factors and save them one by one in the currentFactor.
    currentFactor for the first test would be P(D0 | W0) and P(W0). for each factor all
    conditioned and unconditioned values are saved into two temp lists called;
    	conditionedTemp: saving all conditioned values among all factors
    	unconditionedTemp: saving all unconditioned values among all factors
    	
    it is obvious that there might be redundancy in both lists. thus the following 
    two lists are made:
    	conditionedFinal: to save the final values of conditioned
    	unconditionedFinal: to save the final values of unconditioned
    	
    to achieve this goal first i would loop through the "unconditionedTemp" and only 
    add values to "unconditionedFinal" if it is not already there. then I would loop 
    through the "conditionedTemp" and only add values to "conditionedFinal" if that 
    value is not already in there and not available in the unconditionedFinal. In other
    words, I am removing all redundancies in  conditionedTemp as well as all values that are 
    currently in both conditionedTemp and unconditionedTemp. Since they exist in both, it means 
    that, they will be moved to uncondition in the final form.
    
    once done, a newFactor is made by the new values of condirional, unconditional, and dict
    structure. 
    	Factor(unconditionedFinal, conditionedFinal, variableDomainsDict1)
    
    once new factors are achieved, all possible assignment of them are generated using:
    	newAllPossibleAssignmentDicts = newFactor.getAllPossibleAssignmentDicts()
    
    for the test run this value would be:
    	[{'D': 'wet', 'W': 'sun'}, 
    	 {'D': 'dry', 'W': 'sun'}, 
    	 {'D': 'wet', 'W': 'rain'}, 
    	 {'D': 'dry', 'W': 'rain'}]
    	 
    now that all possible assignemtns are achived I would loop through them and do the
    multiplication of values. for the test run there are two factors
    	[Factor(set(['D']), set(['W']), {'D': ['wet', 'dry'], 'W': ['sun', 'rain']}),  --> P(D0 | W0)
    	 Factor(set(['W']), set([]),    {'D': ['wet', 'dry'], 'W': ['sun', 'rain']})]  --> P(W0)
    	 
    looping through them gives and doing the multiplication would give the fincaly value of P(D0 , W0)
    
    for instance the multiplication of the first value of P(W0) = 0.1 and P(D0 | W0)=0.8 is 
    
	    
	 P(D | W):

	 |  D  |  W   |  Prob:  |
	 ------------------------
	 | wet | sun  | 0.10000 |
	 | dry | sun  | 0.90000 |
	 ------------------------	
	 | wet | rain | 0.70000 |
	 | dry | rain | 0.30000 |


	 P(W):

	 |  W   |  Prob:  |
	 ------------------
	 | sun  | 0.80000 |
	 | rain | 0.20000 |
	 
	 
	 result: 0.08

    executing all the loops would give the following result as the newfactor probability:
    	
    	P(D, W)

	|  D  |  W   |  Prob:  |
 	------------------------
 	| wet | sun  | 8.0e-02 |
 	| dry | sun  | 0.72000 |
 	| wet | rain | 0.14000 |
 	| dry | rain | 6.0e-02 |

    """
    
  
  
  
    
Question 4: Your eliminate implementation 

def eliminateWithCallTracking(callTrackingList=None):
   def eliminate(factor, eliminationVariable):
        """FUNCTIONALITY
        first it is needed to display the all possible assigments of the input
        factor for the sample which is:
        	[{'D': 'wet', 'W': 'sun'}, 
        	 {'D': 'dry', 'W': 'sun'}, 
        	 {'D': 'wet', 'W': 'rain'}, 
        	 {'D': 'dry', 'W': 'rain'}]

        
        in this function one of the variables in the factor will be removed 
        or summed out. to achive this goal all conditioned and unconditioned 
        parameters are groupped into 3 groups:
        	1. conditionedFinal: whose value for the sample run is "EMPTY" 
        	2. unconditionedFinal: whose value for the sample run is "D" 
        		which is either "dry" or "wet"
        	3. eliminationVariable: mentioned by the program and in sample it is "W"
        		which is either "sun" or "rain"
        
        once grouped, the summed out parameter is removed from  unconditionedTemp
        and the result is saved into a new list.
        
        Having "conditionedFinal" and "unconditionedFinal", I can generate a 
        newFactor using the Factor function. for the test this value is
        	P(D)

		|  D  |  Prob:  |
 		-----------------
 		| wet | 0.0e+00 |
 		| dry | 0.0e+00 |
 	
 	this is the value after the elimination value is summed out of it. as 
 	you see all values are zero and they will be calculated later
 	
 	using newFactor "keepDomain" can be generated which hass all variables 
 	which will show up in the final result. in the sample run the results 
 	are the values of the "D" variable which are "dry" and "wet"
 	
 	using "variableDomainsDict" with "eliminationVariable" as input, i can 
 	get all parameters which should be removed from the final result or 
 	summed out. in the sample run the results are the values of the "W" 
 	variable which are "sun" and "rain" 
 	
 	Now i can loop through the keepvalues in the main for loop and sum all 
 	the values of the second loop as remove and store them in a list.
 	this list will be added to the newFactor.setProbability as for results
 	of probabilities in the newFactor. to get the values from the original 
 	factors whcih was shown at the beginning of the description the input 
 	format of the dict should be constructed. this has achieved through 3 
 	steps of making a temp input, then placing the current keep values and 
 	current remove values:
 	
 		tempAssignment = {}
                tempAssignment = keep
                tempAssignment[eliminationVariable] = remove
                
        then i can get the probability of the tempAssignment structure by using 
        the initial factor structure: 
 	
	 	tempAssignmentProb = factor.getProbability(tempAssignment)
	 	
	once probability is achived it is summed to other prob of the remove 
	section and saved into a list which is used in the next line to updated
	newFactor
         
        """
        
        
Question 5: Your normalize implementation 
def normalize(factor):
    """FUNCTIONALITY
    all test results are based on 
    	python autograder.py -t test_cases/q5/5-extended-normalize
    
    thus the initial factor would be values for
 	P(Q1, N1, M1, O1, L1)
     
    to start with all conditioned and unconditioned values are imported to two
    temp variables. The reason that they are initially imported into temp 
    variables is that, those with only one argument will be probably observations
    and will be moved from unconditioned into conditioned. in other words, since 
    there is only one entry in that variable's domain, we can either assume it 
    was assigned as evidence to have only one variable in its domain, or it only 
    had one entry in its domain to begin with. This blurs the distinction between 
    evidence assignments and variables. the results of temo would be:
    
    	unconditionedTemp = set(['Q1', 'N1', 'M1', 'O1', 'L1'])
    	conditionedTemp = set([])
    
    once all imported all the entries in the unconditioned temp which only has 
    one domain entry is added from "unconditionedTemp" to "conditionedTemp". once
    all single-entry domains were added to "conditionedTemp", we have to remove all
    those argments from "unconditionedTemp". to achive this, a new variabel set is 
    made as "unconditionedFinal" and all arguments of "unconditionedTemp" are copied
    to "unconditionedFinal" as long as that argument does not exist in "conditionedTemp".
    finally "conditionedTemp" is put into a new variable called "conditionedFinal".
    
    	unconditionedFinal = ['N1', 'O1', 'L1']
    	conditionedFinal = ['Q1', 'M1']
    
    as you see the two values with single entry moved from unconditioned to 
    conditioned.

    both of the new variabels "unconditionedFinal" and "conditionedFinal" are
    used to generate newFactor and newFactor is used to make the structure with 
    all possibilies. 
    
    To Normalize all probabilies in the new assignment list, first all prob of the
    initial assignment list has to calculated. to achive this task "initialAssignment"
    is taken using the following function:
    
	initialAssignment = factor.getAllPossibleAssignmentDicts()
    
    and by looping through all cells, we can sum all probabilities and save it into 
    "sumDenominator"
    
    Now using the "unconditionedFinal" and "conditionedFinal", a new factor "newFactor"
    is generated and new assignment are generated consequently: 
    
    	newFactor = Factor(unconditionedFinal, conditionedFinal, variableDomainsDict)
    	newAssignment = newFactor.getAllPossibleAssignmentDicts()
    	
    now by looping through the values of this "newAssignment" we can get the probability
    of the initial factor and divide it by the sumDenominator, and then save it as a new
    value as "newProb". "newProb" is the new value of the new probability.
    
    here is results after normalize for sample test 5:
    	P(N1, O1, L1 | Q1, M1)
     
    """




Question 6: Your inference by variable elimination implementation
def inferenceByVariableEliminationWithCallTracking(callTrackingList=None):
    def inferenceByVariableElimination(bayesNet, queryVariables, evidenceDict, eliminationOrder):
        "*** YOUR CODE HERE ***"
        """
        this section is heavily based on the "inferenceByEnumeration" section. 
        In "inferenceByEnumeration" section we would join all "joinVariable" 
        to the "currentFactorsList" according to:
        
        	    for joinVariable in bayesNet.variablesSet():
        		currentFactorsList, joinedFactor = joinFactorsByVariable(currentFactorsList, joinVariable)
		        currentFactorsList.append(joinedFactor)
	
	and then eliminate by:
	
		    for eliminationVariable in eliminationVariables:
        		incrementallyMarginalizedJoint = eliminate(incrementallyMarginalizedJoint, eliminationVariable)
   		    fullJointOverQueryAndEvidence = incrementallyMarginalizedJoint

        and then normalize so that the probability sums to one
        	    
        	    queryConditionedOnEvidence = normalize(fullJointOverQueryAndEvidence)
        
        and then return "queryConditionedOnEvidence"
        
        
        
        
        NOW, for "inferenceByVariableElimination" we would heavily use the same 
        method but instead of adding all of them together and then removing 
        all together, we would add one and then remove the same:
        
        to achieve this task we would loop through all the "eliminationOrder" 
        and form a "currentFactorsList" with the "joinedFactor" and "elimVariable"
           	
           	 currentFactorsList, joinedFactor = joinFactorsByVariable(currentFactorsList, elimVariable)
           	 
        then I would eliminate "elimVariable" from "joinedFactor" as long as 
        there is at least more than 1 variable in the unconditioned in the 
        "joinedFactor". I am not fully sure why I have to do it but the comments 
        above say:
        
	        If a factor that you are about to eliminate a variable from has 
	        only one unconditioned variable, you should not eliminate it 
       		and instead just discard the factor.  This is since the 
        	result of the eliminate would be 1 (you marginalize 
        	all of the unconditioned variables), but it is not a 
        	valid factor.  So this simplifies using the result of eliminate. 
        
        I guess the reason is that if there is only one unconditioned in the 
        joint and we remove them there would be no unconditioned left in joint.
        if there is only 1 unconditioned this is what happens:
        
        	P(A|B).P(B) = P(A,B) --> end of it --> cant eliminate B from P(A,B)
        
        once the currentfactorList is updated a new factors list is generated
        and the normalized result is returned. 
        
        	finalFactorsList = joinFactors(currentFactorsList)
        	finalFactorsListNormalized = normalize(finalFactorsList)

   
        """



   
    
    



    


































  


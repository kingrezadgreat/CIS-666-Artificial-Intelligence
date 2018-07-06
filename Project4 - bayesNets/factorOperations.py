# factorOperations.py
# -------------------
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


from bayesNet import Factor
import operator as op
import util

def joinFactorsByVariableWithCallTracking(callTrackingList=None):


    def joinFactorsByVariable(factors, joinVariable):
        """
        Input factors is a list of factors.
        Input joinVariable is the variable to join on.

        This function performs a check that the variable that is being joined on 
        appears as an unconditioned variable in only one of the input factors.

        Then, it calls your joinFactors on all of the factors in factors that 
        contain that variable.

        Returns a tuple of 
        (factors not joined, resulting factor from joinFactors)
        """

        if not (callTrackingList is None):
            callTrackingList.append(('join', joinVariable))

        currentFactorsToJoin =    [factor for factor in factors if joinVariable in factor.variablesSet()]
        currentFactorsNotToJoin = [factor for factor in factors if joinVariable not in factor.variablesSet()]

        # typecheck portion
        numVariableOnLeft = len([factor for factor in currentFactorsToJoin if joinVariable in factor.unconditionedVariables()])
        if numVariableOnLeft > 1:
            print "Factor failed joinFactorsByVariable typecheck: ", factor
            raise ValueError, ("The joinBy variable can only appear in one factor as an \nunconditioned variable. \n" +  
                               "joinVariable: " + str(joinVariable) + "\n" +
                               ", ".join(map(str, [factor.unconditionedVariables() for factor in currentFactorsToJoin])))
        
        joinedFactor = joinFactors(currentFactorsToJoin)
        return currentFactorsNotToJoin, joinedFactor

    return joinFactorsByVariable

joinFactorsByVariable = joinFactorsByVariableWithCallTracking()


def joinFactors(factors):
    """
    Question 3: Your join implementation 

    Input factors is a list of factors.  
    
    You should calculate the set of unconditioned variables and conditioned 
    variables for the join of those factors.

    Return a new factor that has those variables and whose probability entries 
    are product of the corresponding rows of the input factors.

    You may assume that the variableDomainsDict for all the input 
    factors are the same, since they come from the same BayesNet.

    joinFactors will only allow unconditionedVariables to appear in 
    one input factor (so their join is well defined).

    Hint: Factor methods that take an assignmentDict as input 
    (such as getProbability and setProbability) can handle 
    assignmentDicts that assign more variables than are in that factor.

    Useful functions:
    Factor.getAllPossibleAssignmentDicts
    Factor.getProbability
    Factor.setProbability
    Factor.unconditionedVariables
    Factor.conditionedVariables
    Factor.variableDomainsDict
    """

    # typecheck portion
    setsOfUnconditioned = [set(factor.unconditionedVariables()) for factor in factors]
    if len(factors) > 1:
        intersect = reduce(lambda x, y: x & y, setsOfUnconditioned)
        if len(intersect) > 0:
            print "Factor failed joinFactors typecheck: ", factor
            raise ValueError, ("unconditionedVariables can only appear in one factor. \n"
                    + "unconditionedVariables: " + str(intersect) + 
                    "\nappear in more than one input factor.\n" + 
                    "Input factors: \n" +
                    "\n".join(map(str, factors)))


    "*** YOUR CODE HERE ***"
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
    "importing the domain dict"
    variableDomainsDict = {}
    variableDomainsDict1 = factors[0].variableDomainsDict()
    #variableDomainsDict2 = factors[1].variableDomainsDict()    

    #print variableDomainsDict1
    #print variableDomainsDict2
    #print len(factors)
    
    "setting the two lists that contain all condition and uncondition"
    conditionedTemp = []
    unconditionedTemp = []
    
    #print factors
    "saving all condition and uncondition temps"
    for i in range (0, len(factors)):
    
        currentFactor = factors[i]
        #print currentFactor

        for unconditioned_var in currentFactor.unconditionedVariables():
            unconditionedTemp.append(unconditioned_var)
        
        for conditioned_var in currentFactor.conditionedVariables():
            conditionedTemp.append(conditioned_var)
    
    "final values of condition and uncondition to get all new factors"	
    conditionedFinal = []
    unconditionedFinal = []
    
    "removing redundancies from uncondition temp"
    for i in unconditionedTemp:
        if i not in unconditionedFinal:
            unconditionedFinal.append(i)

    "removing redundancies and duplicates of unconditionfinal from condition temp "
    for i in conditionedTemp:
        if i not in unconditionedFinal and i not in conditionedFinal:
            conditionedFinal.append(i)
    "generate new factor"
    newFactor = Factor(unconditionedFinal, conditionedFinal, variableDomainsDict1)
    
    "get all possibilities"
    newAllPossibleAssignmentDicts = newFactor.getAllPossibleAssignmentDicts()
    #print newAllPossibleAssignmentDicts
    "set initial value of probability"
    probInit = 1
    #probInit = 0
    
    "loop through all the possibiliets and generate new probability "
    for currentPossible in newAllPossibleAssignmentDicts:
        prob = probInit
        #print factors
        "looping through all factors to do"
        for i in range(0, len(factors)):
            currentFactor = factors[i]
            #print currentFactor
            prob = prob * currentFactor.getProbability(currentPossible)
        #print prob
        newFactor.setProbability(currentPossible, prob)

    #print  newFactor
    return newFactor

    #util.raiseNotDefined()


def eliminateWithCallTracking(callTrackingList=None):

    def eliminate(factor, eliminationVariable):
        """
        Question 4: Your eliminate implementation 

        Input factor is a single factor.
        Input eliminationVariable is the variable to eliminate from factor.
        eliminationVariable must be an unconditioned variable in factor.
        
        You should calculate the set of unconditioned variables and conditioned 
        variables for the factor obtained by eliminating the variable
        eliminationVariable.

        Return a new factor where all of the rows mentioning
        eliminationVariable are summed with rows that match
        assignments on the other variables.

        Useful functions:
        Factor.getAllPossibleAssignmentDicts
        Factor.getProbability
        Factor.setProbability
        Factor.unconditionedVariables
        Factor.conditionedVariables
        Factor.variableDomainsDict
        """
        # autograder tracking -- don't remove
        if not (callTrackingList is None):
            callTrackingList.append(('eliminate', eliminationVariable))

        # typecheck portion
        if eliminationVariable not in factor.unconditionedVariables():
            print "Factor failed eliminate typecheck: ", factor
            raise ValueError, ("Elimination variable is not an unconditioned variable " \
                            + "in this factor\n" + 
                            "eliminationVariable: " + str(eliminationVariable) + \
                            "\nunconditionedVariables:" + str(factor.unconditionedVariables()))
        
        if len(factor.unconditionedVariables()) == 1:
            print "Factor failed eliminate typecheck: ", factor
            raise ValueError, ("Factor has only one unconditioned variable, so you " \
                    + "can't eliminate \nthat variable.\n" + \
                    "eliminationVariable:" + str(eliminationVariable) + "\n" +\
                    "unconditionedVariables: " + str(factor.unconditionedVariables()))

        "*** YOUR CODE HERE ***"
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
        #util.raiseNotDefined()
        #temp = factor.getAllPossibleAssignmentDicts()
        #print temp
        
        variableDomainsDict = factor.variableDomainsDict()
                
        conditionedFinal = factor.conditionedVariables()
        unconditionedTemp = factor.unconditionedVariables()

        unconditionedFinal = []
        for val in unconditionedTemp:
            if val != eliminationVariable:
                unconditionedFinal.append(val)
        
        #print unconditionedFinal
        newFactor = Factor(unconditionedFinal, conditionedFinal, variableDomainsDict)
        print newFactor

        keepDomain = newFactor.getAllPossibleAssignmentDicts()
	removeDomain = variableDomainsDict[eliminationVariable]
        
        
    	
        prob = 0
    	probList = []
        for keep in keepDomain:
            for remove in removeDomain:
                tempAssignment = {}
                tempAssignment = keep
                tempAssignment[eliminationVariable] = remove
                
                tempAssignmentProb = factor.getProbability(tempAssignment)
                prob = prob + tempAssignmentProb
            probList.append(prob)
            prob = 0

        i = 0
        for keep in keepDomain:
            newFactor.setProbability(keep, probList[i])
            i=i+1
        return newFactor


    return eliminate

eliminate = eliminateWithCallTracking()


def normalize(factor):
    """
    Question 5: Your normalize implementation 

    Input factor is a single factor.

    The set of conditioned variables for the normalized factor consists 
    of the input factor's conditioned variables as well as any of the 
    input factor's unconditioned variables with exactly one entry in their 
    domain.  Since there is only one entry in that variable's domain, we 
    can either assume it was assigned as evidence to have only one variable 
    in its domain, or it only had one entry in its domain to begin with.
    This blurs the distinction between evidence assignments and variables 
    with single value domains, but that is alright since we have to assign 
    variables that only have one value in their domain to that single value.

    Return a new factor where the sum of the all the probabilities in the table is 1.
    This should be a new factor, not a modification of this factor in place.

    If the sum of probabilities in the input factor is 0,
    you should return None.

    This is intended to be used at the end of a probabilistic inference query.
    Because of this, all variables that have more than one element in their 
    domain are assumed to be unconditioned.
    There are more general implementations of normalize, but we will only 
    implement this version.

    Useful functions:
    Factor.getAllPossibleAssignmentDicts
    Factor.getProbability
    Factor.setProbability
    Factor.unconditionedVariables
    Factor.conditionedVariables
    Factor.variableDomainsDict
    """

    # typecheck portion
    variableDomainsDict = factor.variableDomainsDict()
    for conditionedVariable in factor.conditionedVariables():
        if len(variableDomainsDict[conditionedVariable]) > 1:
            print "Factor failed normalize typecheck: ", factor
            raise ValueError, ("The factor to be normalized must have only one " + \
                            "assignment of the \n" + "conditional variables, " + \
                            "so that total probability will sum to 1\n" + 
                            str(factor))

    "*** YOUR CODE HERE ***"
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
    print ""
    print ""
    #util.raiseNotDefined()
    #print factor
    sumDenominator = 0
    "set the two temp variables for inital factor"
    unconditionedTemp = factor.unconditionedVariables()
    conditionedTemp = factor.conditionedVariables()
    #print unconditionedTemp
    #print conditionedTemp
    
    "move single-entry values in uncontitionedtemp to conditionedTemp"
    for var in unconditionedTemp:
        if len(variableDomainsDict[var]) == 1:
            if var not in conditionedTemp:
                conditionedTemp.add(var)
    "generate new list for unconditioned and put all unconditionedTemp values except those were moved"
    unconditionedFinal = []
    for var in unconditionedTemp: 
        if var not in conditionedTemp:
            unconditionedFinal.append(var) 
    "generate conditionedFinal from conditionedTemp"
    conditionedFinal = []
    for var in conditionedTemp:
    	conditionedFinal.append(var)
    
    #print unconditionedFinal
    #print conditionedFinal
    
    "get initial assignemtn to do prob summation"
    initialAssignment = factor.getAllPossibleAssignmentDicts()
    
    "do prob summation"
    sumDenominator = 0
    for i in range(0, len(initialAssignment)):
        currentFactorVal = initialAssignment[i]
        sumDenominator = sumDenominator + factor.getProbability(currentFactorVal)
   
    "make new factor with the new unconditioned and conditioned values and get assigments"
    newFactor = Factor(unconditionedFinal, conditionedFinal, variableDomainsDict)
    newAssignment = newFactor.getAllPossibleAssignmentDicts()
    
    "loop through all new assignments and divide the problem by the summation and set them back to 'newFactor' "
    for newFactorElem in newAssignment:
        prob = factor.getProbability(newFactorElem)
        newProb = prob / sumDenominator
        newFactor.setProbability(newFactorElem, newProb)

    #print newFactor
    return newFactor
    
    

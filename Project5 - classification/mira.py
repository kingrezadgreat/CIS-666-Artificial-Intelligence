# mira.py
# -------
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


# Mira implementation
import util
PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.legalLabels = legalLabels
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        self.features = trainingData[0].keys() # this could be useful for your code later...

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        """
        This method sets self.weights using MIRA.  Train the classifier for each value of C in Cgrid,
        then store the weights that give the best accuracy on the validationData.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        representing a vector of values.
        """
        "*** YOUR CODE HERE ***"
        """FUNCTIONALITY DESCRIPTION
        this function follows the same rules for perceptron. The only difference 
        would be at the time of tau calculation and taking minimum. 
        
        liek perceptron, MIRA loops through iterations and then loops for each 
        trainign data. each training data is saved into "dataSet" and each label is
        saved into "trainingLabel". A maxScoreVal if -inf is set which helps finding
        the maximumvalue for score. Once maximum score is found it is saved and if its
        value is larger than the "maxScoreVal", then its values is saved into 
        "maxScoreVal" and its label is saved into "maxScoreLabel". 
        
        Now it is time to evaluate the predicted label (maxScoreLabel) with actual 
        label (trainingLabel). if they are the same --> no problem. otherwise, tau has
        to be calculated and applied to dataSet.
        
        Thus a new set called "dataSetTau" is made which will eventually multiplied by 
        tay and used as "tau*f":
        	wy=wy+/-tau*f     
        
        tauTemp as a temp value for tau is calculated. if its value is larger tan "c"
        then c is returned. Otherwise "tauTemp" is terurned. This is a way t minimize
        between "c" and "tauTemp".
        
        once tau is calculated, it is applied to "tau*f ":
        
        	for key, value in dataSetTau.items():
        		dataSetTau[key] = value * tau
        
        and finally weights are adjusted
           
        """
        for c in Cgrid:
           # import weight list for each value of c in Cgrid
           weightList = self.weights
           
           # nowo iterate through max iterations
           for iteration in range(self.max_iterations):
              for i in range(0, len(trainingData)):

                 # importing trainigData as well as training labels and labelSets
                 dataSet = trainingData[i]
                 trainingLabel = trainingLabels[i]
                 maxScoreVal = -9999
                 labelSet = self.legalLabels
                 
                 # finding maximum score and saving its label in "maxScoreLabel"
                 for ii in range(0,len(labelSet)):
                    currentLabel = labelSet[ii]
                    score = dataSet * weightList[currentLabel]
                    if score > maxScoreVal:
                       maxScoreVal = score
                       maxScoreLabel = currentLabel
                    
                 # if the predicted and actual labels are not equal then do:   
                 if maxScoreLabel != trainingLabel:
		    # dataSetTau is a copy of dataSet and eventually multiplied by calculated tau
                    dataSetTau = dataSet.copy()
                    tauTemp=((weightList[maxScoreLabel]-weightList[trainingLabel])*dataSet+1.0)/(2.0*(dataSet*dataSet))
                    
                    # minimizing (c,tauTemp)
                    if c>tauTemp:
                       tau = tauTemp
                    else:
                       tau = c
                    
                    #multiplying tau by elements of "dataSetTau" to generate tau*f  
                    for key, value in dataSetTau.items():
                       dataSetTau[key] = value * tau
                    
                    #adjusting weights
                    weightList[trainingLabel] = weightList[trainingLabel] + dataSetTau
                    weightList[maxScoreLabel] = weightList[maxScoreLabel] - dataSetTau
        
        # updating weights  
        self.weights = weightList                
    

    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses



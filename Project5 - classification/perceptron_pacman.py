# perceptron_pacman.py
# --------------------
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


# Perceptron implementation for apprenticeship learning
import util
from perceptron import PerceptronClassifier
from pacman import GameState

PRINT = True


class PerceptronClassifierPacman(PerceptronClassifier):
    def __init__(self, legalLabels, maxIterations):
        PerceptronClassifier.__init__(self, legalLabels, maxIterations)
        self.weights = util.Counter()

    def classify(self, data ):
        """
        Data contains a list of (datum, legal moves)
        
        Datum is a Counter representing the features of each GameState.
        legalMoves is a list of legal moves for that GameState.
        """
        guesses = []
        for datum, legalMoves in data:
            #print legalMoves
            #raw_input()
            vectors = util.Counter()
            for l in legalMoves:
                vectors[l] = self.weights * datum[l] #changed from datum to datum[l]
            guesses.append(vectors.argMax())
        return guesses


    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        self.features = trainingData[0][0]['Stop'].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.

        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            for i in range(len(trainingData)):
                "*** YOUR CODE HERE ***"
                """FUNCTIONALITY DESCRIPTION
                for this function i tried to use my old percepron but there
                are errors related to labels. thus i decided to use the classify 
                function instead.
                
                this function takes the "dataSet" as input to "self.classify" and 
                saves the prediction. 
                
                if prediction and actual label are not the same, the key of dataSet 
                is extracted and both values of "dataSetTraining" and "dataSetPrediction"
                are extracted subsequently. 
                
                and then weights are adjusted. 
                """

 
                dataSet = trainingData[i]
                classifySet = self.classify([dataSet])
                prediction = classifySet[0]
                trainingLabel = trainingLabels[i]
 
                if prediction != trainingLabel:
                   key, label = dataSet

                   dataSetTraining = key[trainingLabel]
                   dataSetPrediction = key[prediction]
                   
                   self.weights = self.weights + dataSetTraining
                   self.weights = self.weights - dataSetPrediction
               
                
                """
                # util.raiseNotDefined()



          	# all legal label sets
          	labelSet = ['West', 'Stop', 'East', 'North', 'South']
          	print labelSet
          	print len(self.weights)
          	raw_input()

          	
          	# maximum value used to capture the weight label with maximum score"
          	maxScoreVal = -9999
          	
          	# dataSet and traininglabels          	
          	dataSet = trainingData[i]
          	trainingLabel = trainingLabels[i]
          	#print trainingLabel
          	#raw_input()
          	
          	# now loop for all elements of label set which has 10 elements
           	for ii in range(0,len(labelSet)):
           	   # obtain current label from labelSet
           	   currentLabel = labelSet[ii]
           	   # compute score value
             	   score = dataSet * self.weights[currentLabel]
              	   # if score> maxScoreVal --> we have to save new values
              	   if score > maxScoreVal:
              	      maxScoreVal = score
                      maxScoreLabel = currentLabel
                
                # if the predicted labe (maxScoreLabel) is not equal to the actual label (trainingLabel), then adjusy
          	if maxScoreLabel != trainingLabel:
                    
                   self.weights[trainingLabel] = self.weights[trainingLabel] + dataSet
                   self.weights[maxScoreLabel] = self.weights[maxScoreLabel] - dataSet
                
                

                
                
                """                 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

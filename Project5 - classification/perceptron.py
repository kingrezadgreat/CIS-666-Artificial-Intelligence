# perceptron.py
# -------------
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


# Perceptron implementation
import util
PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels);
        self.weights = weights;

    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """

        self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.

        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            for i in range(len(trainingData)):
                "*** YOUR CODE HERE ***"
                """FUNCTIONALITY DESCRIPTION
                this fucntion loops for all "i" in range of training data
                and for each data set "dataSet = trainingData[i]" it finds
                the best weights.
                
                it sets a maxScoreVal to a minimum such that in each loop
                it gets initialized. then it loops through all labelSet which has
                10 elements and does the following operation:
                
                	score(f,y)=sigma(fi * wi)
                
                this function is take from the classify function too which is:
                
                	for l in self.legalLabels:
                		vectors[l] = self.weights[l] * datum
                
                this fucntion multiply weights by ys and sum them into score.
                if score is larger than the initilized "maxScoreVal", then
                "maxScoreVal" is updated by "score" and "currentLabel" is
                updated by "maxScoreLabel". This operation saves the score and
                label with maximum score. 
                
                Now if the "maxScoreLabel" is the same as the "trainingLabel"
                weights are good. this means that weights of that traingin data 
                were set to the right value which predicts the right label.                
                otherwise weights has to be adjusted according to thefollwoing rule:
               		wy=wy+f
                	wyprime=wyprime-f
                
                this means that if the predicted labe (maxScoreLabel) is not equal 
                to the actual label (trainingLabel), then we have to adjust weights
                
          	"""
          	# all legal label sets
          	labelSet = self.legalLabels
          	
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

                
                    #util.raiseNotDefined()
                
                

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


    def findHighWeightFeatures(self, label):
        """
        Returns a list of the 100 features with the greatest weight for some label
        """
        featuresWeights = []

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

        return featuresWeights

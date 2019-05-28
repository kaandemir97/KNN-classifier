from Classifier import classif
from PriorityQueue import PriQue
from Neighbour import Nb
import numpy as np

class nearestNeighbour:
    def __init__(self, trainingList, testList, k):
        self.Ytrain = trainingList
        self.Ytest = testList
        self.Classifier = list() #This is the results list containing final classifier
        self.Neighbours = list()
        self.k = k
        return

    def run(self, k):
        #Stage 1: Finding k-most near neighbours yi of xi
        for stest in self.Ytest:
            Query = PriQue(k, stest.classs)
            for strain in self.Ytrain:
                yi = Nb(strain.classs, self.EuclideanDistance(stest,strain))
                Query.add(yi)
            self.Neighbours.append(Query)
        #Stage 2: Results computation
        for Query in self.Neighbours:
            prediction = Query.getPrediction()
            true = Query.stest
            self.Classifier.append(classif(prediction, true))

        return

    #Write to csv in format | Prediction    True-label      Correct: true/false |
    #With final %accuracy at last line

    def printres(self):
        accuracy = 0
        filename = "results" + "_" +str(self.k) +".csv"
        with open(filename, "w") as fp:
            for res in self.Classifier:
                if res.correct:
                    accuracy+=1
                fp.write("Prediction: "+res.prediction+", True Label: "+res.true+",     Correct: "+str(res.correct)+"\n")
            accuracy = accuracy/len(self.Classifier)*100
            fp.write("Overall Accuracy: "+str(accuracy)+"%")
            fp.close()
        return

    #Euclidean distance basen on sum of the abs() differences between all parameters of each observed test vector and training vector, ^2. Final Result squared.

    def EuclideanDistance(self, train, test):
        ed = 0
        ed += ((train.sl-test.sl)**2)
        ed += ((train.sw-test.sw)**2)
        ed += ((train.pl-test.pl)**2)
        ed += ((train.pw-test.pw)**2)
        ed = np.sqrt(ed)
        return ed

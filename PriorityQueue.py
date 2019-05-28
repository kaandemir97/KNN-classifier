import numpy as np
from Neighbour import Nb

class PriQue:
    def __init__(self, k, stest):
        self.k = k
        self.Neighbours = np.full(self.k, None)
        self.stest = stest
        return
        #Implement fully functional priority queue wrapper of length k with values judged on smallest EuclideanDistance
        #Add
        #BubbleDown

    def add(self, Nbour):
        #Base case first 5 comparisons
        for i in range(self.k):
            if self.Neighbours[i] == None:
                self.Neighbours[i] = Nbour
                self.bubbleDown()
                return
        #Now we start adding only neighbours less than biggest value
        if Nbour.distance<self.Neighbours[self.k-1].distance:
            self.Neighbours[self.k-1]=Nbour
            self.bubbleDown()
            return
        return

    #Smallest value always sinks down
    def bubbleDown(self):
        for i in reversed(range(1,self.k)):
            if self.Neighbours[i]==None:
                continue
            #SWAP
            if self.Neighbours[i].distance<self.Neighbours[i-1].distance:
                self.Neighbours[i], self.Neighbours[i-1] = self.Neighbours[i-1], self.Neighbours[i]
        return

    #Counts frequencies of final NB in self.Neighbours. Prediction is made using argmax() - the most frequent type of label in the nearest neighbour queue

    def getPrediction(self):
        labels = np.array(['Iris-setosa','Iris-versicolor','Iris-virginica'])
        count = np.array([0,0,0])
        for Nbour in self.Neighbours:
            if Nbour.strain == labels[0]:
                count[0]+=1
            elif Nbour.strain == labels[1]:
                count[1]+=1
            elif Nbour.strain == labels[2]:
                count[2]+=1
        prediction = labels[np.argmax(count)]

        return prediction

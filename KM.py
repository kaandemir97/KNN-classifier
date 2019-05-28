from Cluster import clust
import numpy as np
import random

class kmeans:

    #Hard-coded number of clusters = 3

    def __init__(self, data):
        self.data = data

        #Randomly select 3 initial clusters from data

        rands = []
        randomNum = random.randint(0,len(data))
        rands.append(randomNum)
        while len(rands)<3:
            randomNum = random.randint(0,len(data))
            for i in range(len(rands)):
                if rands[i]==randomNum:
                    break
                elif i < len(rands)-1:
                    continue
                else:
                    rands.append(randomNum)
                    break

        #Initial clusters

        c1 = data[rands[0]]
        c2 = data[rands[1]]
        c3 = data[rands[2]]

        c11 = clust(c1.sl,c1.sw,c1.pl,c1.pw)
        c22 = clust(c2.sl,c2.sw,c2.pl,c2.pw)
        c33 = clust(c3.sl,c3.sw,c3.pl,c3.pw)

        self.clusters = [c11, c22, c33]

        return

    def run(self):
        iteration = 0
        while True:
            iteration+=1
            print("Iteration: "+str(iteration))
            for x in self.data:
                cluster = None
                for ci in self.clusters:
                    if cluster == None:
                        cluster = ci
                    elif self.EuclideanDistance(cluster,x) > self.EuclideanDistance(ci,x):
                        cluster = ci
                #Sets closest cluster to x
                x.setCluster(cluster)
            #Calculate centroids, and compare with self.clusters. If passes convergence check, break loop and present results
            centroids, group1, group2, group3 = self.calculateCentroid()
            converged = True
            #Checks convergence of each cluster with previous version, distance difference measured at 10e-4
            for i in range(len(self.clusters)):
                if self.EuclideanDistance(self.clusters[i],centroids[i]) > 10e-6:
                    converged = False
            if converged:
                print("\n")
                break
            self.clusters = centroids
            #Updates clusters to centroids after iteration

        self.printres(group1, group2, group3)

        return

    #Euclidean distance basen on sum of the abs() differences between all parameters of each observed test vector and training vector, ^2. Final Result squared.

    def EuclideanDistance(self, cluster, x):
        ed = 0
        ed += ((cluster.sl-x.sl)**2)
        ed += ((cluster.sw-x.sw)**2)
        ed += ((cluster.pl-x.pl)**2)
        ed += ((cluster.pw-x.pw)**2)
        ed = np.sqrt(ed)
        return ed

    def calculateCentroid(self):
        group1 = list()
        group2 = list()
        group3 = list()
        centroids = [None,None,None]
        for x in self.data:
            if x.getCluster() == self.clusters[0]:
                group1.append(x)
            elif x.getCluster() == self.clusters[1]:
                group2.append(x)
            else:
                group3.append(x)
        centroids[0] = self.calculateMeans(group1)
        centroids[1] = self.calculateMeans(group2)
        centroids[2] = self.calculateMeans(group3)
        return centroids, group1, group2, group3

    def calculateMeans(self,group):
        sum_sl = 0
        sum_sw = 0
        sum_pl = 0
        sum_pw = 0
        for x in group:
            sum_sl+=x.sl
            sum_sw+=x.sw
            sum_pl+=x.pl
            sum_pw+=x.pw
        #Sum of all dimensions of a group assigned to cluster Ci, divided by the cardinality of the group (new mean)
        sum_sl = sum_sl/len(group)
        sum_sw = sum_sw/len(group)
        sum_pl = sum_pl/len(group)
        sum_pw = sum_pw/len(group)
        centroidi = clust(sum_sl,sum_sw,sum_pl,sum_pw)
        return centroidi

    def printres(self, group1, group2, group3):
        accuracy = 0
        filename = "results_kmeans.csv"
        with open(filename, "w") as fp:
            fp.write("Cluster 1\n")
            for x in group1:
                fp.write("True Label: "+x.classs+"\n")
            fp.write("Cluster 2\n")
            for x in group2:
                fp.write("True Label: "+x.classs+"\n")
            fp.write("Cluster 3\n")
            for x in group3:
                fp.write("True Label: "+x.classs+"\n")
            fp.close()
        return

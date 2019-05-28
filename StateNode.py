class SN:
    def __init__(self, line, cluster = None):
        # sepal length in cm
        self.sl = float(line[0])
        # sepal width in cm
        self.sw = float(line[1])
        # petal length in cm
        self.pl = float(line[2])
        # petal width in cm
        self.pw = float(line[3])
        self.classs = line [4]
        #For kmeans
        self.cluster = cluster
        return
    def getValues(self):
        return self.sl, self.sw, self.pl, self.pw, self.classs

    #For kmeans
    def getCluster(self):
        return self.cluster

    def setCluster(self, replacement):
        self.cluster = replacement
        return

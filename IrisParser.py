from StateNode import SN

class txtParser:

    def __init__(self, training_set, test_set):

        #Constructor

        self.trainingList = list()
        self.testList = list()
        self.populateList(training_set,self.trainingList)
        self.populateList(test_set,self.testList)

    #Fill list with StateNode (wrapper for data) classes

    def populateList(self, file, list):
        with open(file) as fp:
            for line in fp:
                if len(line) < 5:
                    continue
                list.append(self.lineParser(line))
        return

    #Parse line by splitting spaces

    def lineParser(self, line):
        line = line.split()
        lineNode = SN(line)
        return lineNode

    def returnLists(self):
        return self.trainingList, self.testList

class kmeansParser:

    #Constructor

    def __init__(self, data):
        self.data = list()
        self.populateList(data, self.data)

    #Fill list with StateNode (wrapper for data) classes

    def populateList(self, file, list):
        with open(file) as fp:
            for line in fp:
                if len(line) < 5:
                    continue
                list.append(self.lineParser(line))
        return

    #Parse line by splitting spaces

    def lineParser(self, line):
        line = line.split()
        lineNode = SN(line)
        return lineNode

    def returnList(self):
        return self.data

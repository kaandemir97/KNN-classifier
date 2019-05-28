import sys
from IrisParser import txtParser
from KNN import nearestNeighbour

def main(argv):

    if len(argv) != 3:
        print("Invalid function call: main.py <k> <training_set.txt> <test_set.txt>")
        return

    k = int(sys.argv[1])
    training_set = sys.argv[2]
    test_set = sys.argv[3]

    ps = txtParser(training_set, test_set)
    trainingList, testList = ps.returnLists()

    knnTest = nearestNeighbour(trainingList, testList, k)
    knnTest.run(k)

    knnTest.printres()

    return

if __name__ == "__main__":
    main(sys.argv[1:])

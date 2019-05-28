from IrisParser import kmeansParser
from Cluster import clust
from KM import kmeans
import sys

def main(argv):
    if len(argv)!=1:
        print("Invalid function call: kmeans.py <dataset.txt>")
        return

    dataSet = sys.argv[1]
    data = kmeansParser(dataSet)
    data = data.returnList()
    KM = kmeans(data)
    KM.run()

    return

if __name__ == "__main__":
    main(sys.argv[1:])

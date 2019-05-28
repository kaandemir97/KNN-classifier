COMP 307 Assignment 1 Part 1
Code can be executed in terminal (linux/KDE) by invoking
python main.py <k> <training-data.txt> <test-data.txt>
<k> is the specified number of neighbours to run the algorithm on
K-means can be launched by invoking
python kmeans.py <dataset.txt>

There is no console output

Sample output:
Program outputs a results_<k>.csv file and results_kmeans.csv file in the root
directory. The csv for results_1 should look like this:

Prediction:	Iris-setosa		True	Label:	Iris-setosa
Prediction:	Iris-setosa		True	Label:	Iris-setosa
Prediction:	Iris-setosa		True	Label:	Iris-setosa
Prediction:	Iris-setosa		True	Label:	Iris-setosa
.
.
.
Prediction:	Iris-virginica		True	Label:	Iris-virginica
Prediction:	Iris-virginica		True	Label:	Iris-virginica
Prediction:	Iris-virginica		True	Label:	Iris-virginica
Prediction:	Iris-virginica		True	Label:	Iris-virginica
Overall	Accuracy:	94.66666666666667%

results_kmeans.csv should look like this:

Cluster	1
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
True	Label:	Iris-virginica
.
.
.
Cluster	2
True	Label:	Iris-setosa
True	Label:	Iris-setosa
True	Label:	Iris-setosa
True	Label:	Iris-setosa
True	Label:	Iris-setosa
.
.
.
Cluster	3
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
True	Label:	Iris-versicolor
.
.
.

###END README###

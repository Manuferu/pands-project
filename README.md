# pands-project content
# author :  Manuel Fernandez
This folder contains a description and script information about Iris flower dataset [1] [2]

## Introduction to Iris flower dataset and previous works

Iris flower dataset is a multivariate dataset firstly introduced by Dr. Ronald Fisher [2]. It can be called Anderson's Iris Data set due Dr. Edgar Anderson's usage of the data to quantify morphologic variation of the three species within [3]. The data shows four attributes (sepal length, sepal width , petal length and petal width) on three different species of the Iris flower. Dr Fisher managed to demonstrate the discriminant analysis, which consisted in given four mesurments to correctly classify a flower. It has been widely accepted in literature as the beginning of predictors creation [4] [5] [6].

Throughout the years, other authors had used the dataset to develop they works. Patryk S. Hoey, analysed the dataset using two different statistical methods, to make a concrete dataset prediction [4] [5]. Vitaly Borovinsky used the dataset to compare three different neural networks, where he found out a better performance on multilayer perceptron than radial basis function network and probabilistic neural network [7]. Dutta D., Roy A. and Choudhury K. demonstrate that the adaptation of neural networks wights using Particle Swarm Optimization (PSO) performed better than Artificail Neural Networks (ANN) solution [8].

## My Script

The script is breakdown in three parts:

### Part 1: summary of each variable and output to a single text file

Within the part 1 one, the script analyse the dataset and creates an output summary of all three classes with their attributes. To do this kind of processes, I have used Python's Pandas library [9], well known to be an effective Data Science tool. Pandas has shown its powerful and useful classes to handle this kind of operations among to give a good cost-efficient performance. To create a description of each class, the scripts uses a Pandas function called describe, which is very handle and quite complete to create some important statistical outputs of a dataframe. After running this part, the script generates an output called "summary_variables.csv" that can be found in the repository.

### Part 2: histogram of each of variables

In the part 2, I have analysed the data through a histagram analysis. Interesting to see teh pattern how diverse are the pattern of all four variables, specially the pattern of petal width, which shows a total random shape in the histogram distribution. The script makes an histagram of each four variables of the dataset (sepal_length, sepal_width, petal_length, petal_width). To do this part, I have used Python's matplotlib [10]. Matplotlib is a very useful and so intuitive library specialized in data visualization.

### Part 3: scatter plot of each pair of variables

In teh part 3, I have performed a scatter plot of each pair of variables. To do that, I have used again the library matplotlib [10] with the function scatter. As a result, the script creates 4 outputs of scatter plots showing the distribution with the comparasion of all variables between each other in plots of two components.


## Bibliography:

-[1] http://archive.ics.uci.edu/ml/datasets/Iris

-[2] Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2), 179-188.

-[3] https://osf.io/u4kb7/

-[4] Hoey, P. S. (2004). Statistical Analysis of the Iris Flower Dataset. University of Massachusetts At Lowell, Massachusetts.

-[5] Abdulkadir, R. A., Imam, K. A., & Jibril, M. B. (2017). Simulation of back propagation neural network for iris flower classification. American Journal of Engineering Research,  6(1),# 200-205.

-[6] Devasena, C. L., Sumathi, T., Gomathi, V. V., & Hemalatha, M. (2011). Effectiveness evaluation of rule based classifiers for the classification of iris data set. Bonfring International Journal of Man Machine Interface, 1(Special Issue Inaugural Special Issue), 05-09.

-[7] V. Borovinskiy, "Classification of Iris data set," University of Ljubljana, Ljubljana, 2009.

-[8] D. Dutta, A. Roy and K. Choudhury, "Training Artificial Neural Network using Particle Swarm Optimization Algorithm," International Journal of Advanced Research in Computer Science and Software Engineering, vol. 3, no. 3, pp. 430-434, 2013

-[9] https://pandas.pydata.org/

- [10] https://matplotlib.org/

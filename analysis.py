# Author: Manuel Fernandez
# analysis.py: script that analyses the iris dataset. This script was my final project assignment for the subject Programming and Scripting under the High Superior Diploma of Science in computer science (Data Analytics)

# import libraries to use further
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Open Iris dataset using panas library (this is considering iris dataset is saved in the same workspace than the script)

df = pd.read_csv("iris.csv")

#plt.scatter(df['sepal_length'], df['sepal_width'])
#####################################################################################################################################################
####### Part 1: outputs a summary of each variable toa  single text file ############################################################################
#####################################################################################################################################################

#Selection of the rows per each different class using panda's set index and .loc methods
### step 1: divide the dataset per each class

df.set_index("class",inplace=True)
setosa = df.loc['Iris-setosa'] # dataset only with setosa data
versicolor = df.loc['Iris-versicolor'] # dataset only with versicolor data
virginica = df.loc['Iris-virginica'] # dataset only with virginica data

### Step 2: Convert each division into a data frame

s = pd.DataFrame(setosa)
v = pd.DataFrame(versicolor)
vi = pd.DataFrame(virginica)

#### Step 3: produce some statistics for each class and column by using pandas function describe

descs = s.describe() #describe for setosa dataframe
descv = v.describe() #describe for versicolor dataframe
descvi = vi.describe() # describe for virginica dataframe

#### Step 4 Merge all three dataframes to buid up one dataframe with teh data of all species.I have merged first two and then the result with the third one

dfi = descs.merge(descv, how="inner", left_index=True, right_index=True)
dfall = dfi.merge(descvi, how="inner", left_index=True, right_index=True)

#### Step 5 Change the column names to put it more understandable to know which column is refearing to what of the three species. In order to do that
#### I have added is the name of the specie at the begining of each column.

dfall.columns = ['setosa_sepal_length', 'setosa_sepal_width','setosa_petal_length', 'setosa_petal_width','versicolor_sepal_length', 'versicolor_sepal_width','versicolor_petal_length', 'versicolor_petal_width','virginica_sepal_length', 'virginica_sepal_width','virginica_petal_length', 'virginica_petal_width']

### As a final stage, as requested by the guidelines of the project, I print it in .csv format
dfall.to_csv('summary_variables.csv')

#####################################################################################################################################################
####### Part 2:  make an histogram of each variable to png files ##################################################################################
#####################################################################################################################################################

# I have created a function to create histograms. The user has to define the dataset and the column interesting in to representate

def histograms (dataframe,column):
    plt.title(column+" histogram for all dataset")
    plt.hist(dataframe[column])
    plt.xlabel(column)
    plt.ylabel("number of cases")
    plt.savefig(column+"_histogram.png")
    return plt.clf()

#histogram for column Sepal length
histsl = histograms(df,'sepal_length')

#histogram for column sepal width
histsw = histograms(df,'sepal_width')

#histogram for column petal length
histpl = histograms(df,'petal_length')

#histogram for column petal width 
histpw = histograms(df,'petal_width') 

#####################################################################################################################################################
####### Part 3:  make scattered plot by pair of variables ###########################################################################################
#####################################################################################################################################################

#I have created a function to automatically do the scatter plots just by in the variable putting dataframe and teh columns you want to scatter plot. In addition, since I have divided previously the data set in
# 3 datasets each one for each class, I have added to the scatter all of the other datasets, with different marker and simbology. This helps to deeply understand the influence of each specie 
# in the overall result.  
# For this part I have checked the site written by Adam Murphy to get inspired (https://blog.finxter.com/matplotlib-scatter-plot/)

def scatter (dataframe,dataframe2,dataframe3, dataframe4,column1,column2,label1,label2,label3,label4):
    plt.title("distribution of"+ column1 + " and " + column2 + " measurments")
    plt.scatter(dataframe[column1],dataframe[column2],c='black',edgecolors="black",label=label1)
    plt.scatter(dataframe2[column1], dataframe2[column2],c='g',marker='+',label=label2)
    plt.scatter(dataframe3[column1], dataframe3[column2],c='r',marker='^',label=label3)
    plt.scatter(dataframe4[column1], dataframe4[column2],c='b',marker='*',label=label4)
    plt.legend(loc='upper left')
    plt.savefig("distribution_"+column1+ "_"+column2+".png")
    return plt.clf()
#scatter 1: scatter comparing sepal_length and sepal_width overall and for each specie. Also include the label I want to see in the legend
scatslw = scatter(df,s,v,vi,'sepal_length','sepal_width','All classes', 'Iris-setosa', 'Iris-versicolor','Iris-virginica')

# Scatter 2 petal length vs petal width

scatplw = scatter(df,s,v,vi,'petal_length','petal_width','All classes', 'Iris-setosa', 'Iris-versicolor','Iris-virginica')

# Scatter 3 sepal length vs petal length
scatslpl = scatter(df,s,v,vi,'sepal_length','petal_length','All classes', 'Iris-setosa', 'Iris-versicolor','Iris-virginica')

# Scatter 4 sepal width vs petal width
scatswpw = scatter(df,s,v,vi,'sepal_width','petal_width','All classes', 'Iris-setosa', 'Iris-versicolor','Iris-virginica')


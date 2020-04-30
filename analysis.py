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

# Histogram 1: sepal length of all dataset
#set the title of the histogram
plt.title("Sepal length histogram for all dataset")
#get the column called "sepal_length" from Iris flower dataset
plt.hist(df['sepal_length'])
# write the x label
plt.xlabel('Sepal lenght ')
# write the y label
plt.ylabel("Number of cases per length")
# save the histogram within our workspace
plt.savefig("Sepal_length_histogram.png")
#close the plot
plt.clf()

# Histogram 2: sepal width of all dataset
#set the title of the histogram
plt.title("Sepal length histogram for all dataset")
#get the column called "sepal_width" from Iris flower dataset
plt.hist(df['sepal_width'])
# write the x label
plt.xlabel('Sepal width ')
# write the y label
plt.ylabel("Number of cases per length")
# save the histogram within our workspace
plt.savefig("Sepal_width_histogram.png")
#close the plot
plt.clf()

# Histogram 3: Petal length of all dataset
#set the title of the histogram
plt.title("Petal length histogram for all dataset")
#get the column called "petal_length" from Iris flower dataset
plt.hist(df['petal_length'])
# write the x label
plt.xlabel('petal length ')
# write the y label
plt.ylabel("Number of cases per length")
# save the histogram within our workspace
plt.savefig("petal_length_histogram.png")
#close the plot
plt.clf()

# Histogram 4: petal width of all dataset
#set the title of the histogram
plt.title("Petal width histogram for all dataset")
#get the column called "petal_width" from Iris flower dataset
plt.hist(df['petal_width'])
# write the x label
plt.xlabel('petal width ')
# write the y label
plt.ylabel("Number of cases per length")
# save the histogram within our workspace
plt.savefig("petal_width_histogram.png")
#close the plot
plt.clf()

#####################################################################################################################################################
####### Part 3:  make scattered plot by pair of variables ###########################################################################################
#####################################################################################################################################################

# Scatter 1 Sepal length vs sepal width

plt.title("distribution of sepal length and width measurments")
plt.scatter(df['sepal_length'],df['sepal_width'],c="red", edgecolors="black")
plt.savefig("distribution_sepal_length_width.png")
#plt.show()
plt.clf()

# Scatter 2 petal length vs petal width

plt.title("distribution of petal length and width measurments")
plt.scatter(df['petal_length'],df['petal_width'],c="black", edgecolors="black")
plt.savefig("distribution_petal_length_width.png")
#plt.show()
plt.clf()

# Scatter 3 sepal length vs petal length

plt.title("distribution of petal length and sepal length measurments")
plt.scatter(df['petal_length'],df['sepal_length'],c="green", edgecolors="black")
plt.savefig("distribution_sepal_petal_length.png")
#plt.show()
plt.clf()

# Scatter 4 sepal width vs petal width

plt.title("distribution of sepal width and petal width measurments")
plt.scatter(df['sepal_width'],df['petal_width'],c="blue", edgecolors="black")
plt.savefig("distribution_sepal_petal_width.png")
#plt.show()
plt.clf()
# Author: Manuel Fernandez
# analysis.py: script that analyses the iris dataset. This script was my final project assignment for the subject Programming and Scripting under the High Superior Diploma of Science in computer science (Data Analytics)

# import libraries to use further
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


#Open Iris dataset using panas library (this is considering iris dataset is saved in the same workspace than the script)
df = pd.read_csv("iris.csv")

#plt.scatter(df['sepal_length'], df['sepal_width'])
####################################################################################################################################################
####### a) First part of the script: outputs a summary of each variable toa  single text file #########################################################
#####################################################################################################################################################

#Selection of the rows per each different class using panda's set index and .loc methods
### step 1: divide the dataset per each class
df.set_index("class",inplace=True)
setosa = df.loc['Iris-setosa']
versicolor = df.loc['Iris-versicolor']
virginica = df.loc['Iris-virginica']
#Save all titles in a list
L = np.array([["setosa","versicolor","virginica"]])
### Step 2: Convert each division into a data frame
s = pd.DataFrame(setosa)
v = pd.DataFrame(versicolor)
vi = pd.DataFrame(virginica)
#### Step 3: produce some statistics for each class and column
#mean 
ms = s.mean()
mv = v.mean()
mvi = vi.mean()
#standard deviation
stds= s.std()
stdv=v.std()
stdvi= vi.std()
#median 
mes = s.median()
mev = v.median()
mevi = vi.median()


print(L[0])
#row1 = ['Setosa','Versicolor', 'Virginica']
#ow2 = [ms,mv,mvi]
np.savetxt('data.csv', L[0], delimiter=",")

#print(virginica)

#print ("Given Dataframe: \n", d)
#make a selection by specie
#Iris-setosa

#setosa = d[d['class'] = "Iris-setosa"]
#print(setosa)




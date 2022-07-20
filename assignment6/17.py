#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tqdm.autonotebook import tqdm
import warnings
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
    



# In[2]:


df = pd.read_csv("./spambase.data")
y = df.iloc[:,-1:]
x = df.iloc[:,:57]

df.describe()


# In[3]:


x = StandardScaler().fit_transform(x)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
C_values_for_fitting = [0.00005, 0.0005, 0.005, 0.05, 0.5, 5, 50, 500, 5000, 50000]
Linear_test , Quadratic_test , RBF_test = [] , [] , []
kernals = ['linear', 'poly', 'rbf']


warnings.filterwarnings('ignore')
FinalTable = []
print('C', 'Linear', 'Quadratic', 'RBF')

# In[4]:


for C_ in tqdm(C_values_for_fitting, leave=False, position=0):
    
    
    accuracies = []
    test_list = []
    
    
    for ker in tqdm(kernals, leave=False, position=0):
        
        if(ker == "poly"):
            classifier = SVC(C=C_, kernel=ker ,degree = 2 , max_iter=1e6)
        else:
            classifier = SVC(C=C_, kernel=ker, max_iter=1e6)
        classifier.fit(x_train, y_train)
        accuracy_train,accuracy_test = accuracy_score(y_train, classifier.predict(x_train)),accuracy_score(y_test, classifier.predict(x_test))
        accuracies.append((accuracy_train,accuracy_test))
        test_list.append(accuracy_test)
        
    Linear_test.append(test_list[0])
    Quadratic_test.append(test_list[1])
    RBF_test.append(test_list[2])
    

    FinalTable.append((C_, accuracies[0], accuracies[1], accuracies[2]))


# In[7]:

for i in FinalTable:
    print(*i)

# print(FinalTable)


# In[6]:


p = [*range(0,10,1)]
plt.plot(p, Linear_test, label = "Linear")
plt.plot(p, Quadratic_test, label = "Quadratic")
plt.plot(p, RBF_test, label = "RBF")

plt.xlabel("C vlaue")
plt.ylabel("Number of New States Visited")
plt.title("Diff vlaue")
# plt.ylim(0 , 1)
plt.margins(0)
plt.legend()
plt.savefig('image.png')

sys.exit(0)



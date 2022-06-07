# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 14:17:31 2021

@author: Kalyani
Greetings of the day, everybody!!
Here's my project titled: "Disaster Prediction on the basis of Rainfall"
under the guidance of: "ib@se Technologies"


"""

#-------------------------importing libraries and classes----------------------------------
import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn import model_selection,neighbors
classif = neighbors.KNeighborsClassifier()
from sklearn.model_selection import train_test_split

#---defining function which will give prediction for keral's rainfall...
def predictk(df):
    '''--1.1--------------------Data loading and prerprocessing of Kerala----------------------------------- '''
    #Read the data present in dataset
    data = pd.read_csv('kerala.csv')
    
    #missing values
    data = data.dropna()
    
    #dropping unwanted columns in order to get proper output in less amount of inputs
    data = data.drop(['JAN', 'FEB', 'MAR', 'APR', 'MAY','SEP', 'DEC'], axis = 1)
    
    #Now let's seperate the data which we are gonna use for prediction(independant variables)
    x = data.iloc[:,2:7]
    #Now seperate the flood label from the dataset(dependant variable)
    y = data.iloc[:, -1]
    
    
    #graphs for the 5 months of monsoon on kerala
    c = data[['JUN','JUL','AUG', '0V']]
    c.hist()
 
    
    '''  I have previously changed dataset values of dependant-variable into 1 and 0.
    So, we don't need this step anymore....
    '#Data might be widely distributed so let's scale it between 0 and 1
    minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
    minmax.fit(x).transform(x)
    '''
    
    
    #Let's divide the dataset into 2 sets:train and test in ratio (4:1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    
    #-1.2------------------------applying KNN classifier-------------------------------------------------
    classif.fit(x_train,y_train)
    #print("Accuracy on Testing dataset:",classif.score(x_test, y_test))
    
    #-1.3-----------------------predicting for 1.1 dataset: Keral: Subdivision.--------------------------
    #Let's predict chances of flood
    y_predict = classif.predict(x_test)
    #-1.4-----------------------------------accuracy of model------------------------------------
    #to find accuracy of our model....
    knn_accuracy = cross_val_score(classif,x_test,y_test,cv=3,scoring='accuracy',n_jobs=-1)
    #print("Accuracy of model 1: ", knn_accuracy.mean()*100)
    
    pr = classif.predict(df)
    #print("Prediction: ", pr)
    return(pr)


def predictInd(df):
    #--2.1--------------------------Preprocessing the dataset of all India--------------------------------
    dindia = pd.read_csv('allindia_dataset.csv')
    dindia = dindia.dropna()
    dindia = dindia.drop(['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'DEC', 'OCT', 'NOV', 'ANN'], axis = 1)
    #independant variable
    x1 = dindia.iloc[:, 1: 5]
    #dependant variable
    y1 = dindia.iloc[:, -1]
        
    #graphs for the 4 months of monsoon
    t = dindia[['JUN','JUL','AUG','SEP']]
    t.hist()
    plt.show()
        
    #splitting into train_test dataset...
    x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.2)
        
    #-2.2-----------------------applying KNN classifier to all indiadataset-------------------------------
    classif.fit(x1_train, y1_train)
    print("Score of All india dataset: -", classif.score(x1_test, y1_test))
        
    #-2.3-----------------predicting for 2.1 dataset: All India Rainfall: Yearly record.-----------------
    y1_predict = classif.predict(x1_test)
    
    #-2.4--------------------------------accuracy of model---------------------------------------------
    #to find accuracy of model....
    accuracy = cross_val_score(classif, x1_test, y1_test, cv = 3, scoring = 'accuracy', n_jobs = -1)
    print("Accuracy of model 2: ", accuracy.mean())

    pr = classif.predict(df)
    #print("prediction: ", pr)
    return(pr)

    
   












'''
-----------------------------------of testing dataset-------------------------------------
print('predicted chances of flood')
print(y_predict)

#Actual chances of flood
print("actual values of floods:")
print(y_test)
'''


'''
#----------------for 47th row :- it is 1 that is flood chances of flood---------------------
ip = x.iloc[47:48, :] 
print(classif.predict(ip))

ip = x.iloc[48:49, :]    
#taking out a row from a dataframe @allindia_dataset.csv
#print(classif.predict_proba(ip))
print(classif.predict(ip))


print("Chance of Flood in Year 2018:")
if(classif.predict(ip) == 1):
    print("Beware.. the flood will come")
elif(classif.predict(ip) == 0):
    print(classif.predict_proba(ip))
    print("Be rest at ease, there are no chances of flood")
'''  
    
    
    

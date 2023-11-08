# -*- coding: utf-8 -*-
"""diabetes_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RT5FgbLxETBA6ctjdvm9ZohQ8iLbjcuT

importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis"""

# loading the diabetes dataset to pandas DataFrame

diabetes_dataset = pd.read_csv('diabetes.csv')
diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.info()

# getting the statistical meacures of the data

diabetes_dataset.describe()

diabetes_dataset.max()

diabetes_dataset[diabetes_dataset['Pregnancies'] == 17]

diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-Diabetic

1 --> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# Separeting the data and the labels
X = diabetes_dataset.drop(columns='Outcome',axis=1)
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""Data Standadization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

"""Train TEst Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Training the model"""

classifier = svm.SVC(kernel= 'linear')

# training the Support Vector Machine(svm) classifier
classifier.fit(X_train,Y_train)

"""MOdel Evaluation

Accuracy Score
"""

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the training data : ',training_data_accuracy)

# accuracy score of test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy score of the test data is : ',test_data_accuracy)

"""### Making a Predictive System"""

input_data = (5,166,72,19,175,25.8,0.587,51)

# change input_data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardized the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)


prediction = classifier.predict(std_data)
print(prediction)

if (prediction == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')


# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:33:33 2024

@author: sanni
"""
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open("C:/final year project/multiple-disease-prediction/model/heart_disease_model.sav", 'rb'))

# Define the input data
input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)

# Convert input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we're predicting for a single instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make prediction
prediction = loaded_model.predict(input_data_reshaped)

# Output the prediction result
print("Prediction:", prediction)

if prediction[0] == 0:
    print('The Person does not have Heart Disease')
else:
    print('The Person has Heart Disease')

  

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:54:09 2024

@author: sanni
"""

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open("C:/final year project/multiple-disease-prediction/model/heart_disease_model.sav", 'rb'))


#create a function for prediction
def heart_disease_prediction(input_data):
   # Define the input data
   input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)

   # Convert input data to a numpy array
   input_data_as_numpy_array = np.asarray(input_data)

   # Reshape the array as we're predicting for a single instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

   # Make prediction
   prediction = loaded_model.predict(input_data_reshaped)

   # Output the prediction result
   print(prediction)

   if prediction[0] == 0:
       return 'The Person does not have Heart Disease'
   else:
       return 'The Person has Heart Disease'
   
    
   
def main():
    
    #title
    
    st.title('Heart Disease prediction')
    
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal

    age = st.text_input('Age of the person')
    
    sex = st.text_input('Sex of the person')
    
    cp = st.text_input('cp of the person')
    
    trestbps = st.text_input('trestbps of the person')
    
    chol = st.text_input('chol of the person')
    
    fbs = st.text_input('fbs of the person')
    
    restecg = st.text_input('restecg of the person')
    
    thalach = st.text_input('thalach of the person')
    
    exang = st.text_input('exang of the person')
    
    oldpeak = st.text_input('oldpeak of the person')
    
    slope = st.text_input('slope of the person')
    
    ca = st.text_input('ca of the person')
    
    thal = st.text_input('thal of the person')
    
    
    #code for prediction
    diagnosis = ''
    
    #creating a button
    
    if st.button('Heart Disease Prediction Test Result'):
         diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
 
    st.success(diagnosis)

    

if __name__ == '__main__':
    main()
    
    
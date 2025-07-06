# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:05:39 2024

@author: sanni
"""

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open("C:/final year project/multiple-disease-prediction/model/parkinsons_model.sav", 'rb'))

def parkinson_prediction(input_data):
    
    input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

    # changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
      return "The Person does not have Parkinsons Disease"

    else:
      return "The Person has Parkinsons"
  

def main():
    
    st.title("Parkinson Prediction Webapp")
    
    #name	MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	MDVP:Shimmer(dB)	Shimmer:APQ3	Shimmer:APQ5	MDVP:APQ	Shimmer:DDA	NHR	HNR	status	RPDE	DFA	spread1	spread2	D2	PPE
    fo = st.text_input('MDVP:Fo(Hz)')

    fhi = st.text_input('MDVP:Fhi(Hz)')

    flo = st.text_input('MDVP:Flo(Hz)')

    Jitter_percent = st.text_input('MDVP:Jitter(%)')

    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    RAP = st.text_input('MDVP:RAP')

    PPQ = st.text_input('MDVP:PPQ')

    DDP = st.text_input('Jitter:DDP')

    Shimmer = st.text_input('MDVP:Shimmer')

    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    APQ3 = st.text_input('Shimmer:APQ3')

    APQ5 = st.text_input('Shimmer:APQ5')

    APQ = st.text_input('MDVP:APQ')

    DDA = st.text_input('Shimmer:DDA')

    NHR = st.text_input('NHR')

    HNR = st.text_input('HNR')

    RPDE = st.text_input('RPDE')

    DFA = st.text_input('DFA')

    spread1 = st.text_input('spread1')

    spread2 = st.text_input('spread2')

    D2 = st.text_input('D2')

    PPE = st.text_input('PPE')
   
    
    #code for prediction
    diagnosis = ''
    
    #creating a button
    
    if st.button('Parkinson Test Result'):
         diagnosis = parkinson_prediction([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])
 
    st.success(diagnosis)

    

if __name__ == '__main__':
    main()
    
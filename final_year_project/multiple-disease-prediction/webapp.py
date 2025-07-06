# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:35:38 2024

@author: sanni
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")











    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/model/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/model/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(f'{working_dir}/model/breast_cancer_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction' ,
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')
    
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    with st.expander("ℹ️ Detailed Input Descriptions"):
        st.markdown("""
        - **Number of Pregnancies:** Number of times the person has been pregnant.
        - **Glucose Level:** Plasma glucose concentration (mg/dL) measured 2 hours after a glucose intake.
        - **Blood Pressure:** Diastolic blood pressure (mm Hg).
        - **Skin Thickness:** Triceps skinfold thickness (mm).
        - **Insulin Level:** 2-Hour serum insulin (mu U/ml).
        - **BMI:** Body Mass Index (weight in kg/(height in m)^2).
        - **Diabetes Pedigree Function:** A function that scores the likelihood of diabetes based on family history.
        - **Age:** Age of the person (years).
        """)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    
    

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
    with st.expander("ℹ️ Detailed Input Descriptions"):
        st.markdown("""
        - **Age:** Age of the person (years).
        - **Sex:** 1 = Male, 0 = Female.
        - **Chest Pain types:** 0 = Typical angina, 1 = Atypical angina, 2 = Non-anginal pain, 3 = Asymptomatic.
        - **Resting Blood Pressure:** Resting blood pressure (mm Hg).
        - **Serum Cholesterol:** Serum cholesterol in mg/dL.
        - **Fasting Blood Sugar:** 1 if fasting blood sugar > 120 mg/dL, 0 otherwise.
        - **Resting ECG:** 0 = Normal, 1 = Having ST-T wave abnormality, 2 = Showing probable or definite left ventricular hypertrophy.
        - **Maximum Heart Rate:** Achieved maximum heart rate.
        - **Exercise Induced Angina:** 1 = Yes, 0 = No.
        - **Oldpeak:** ST depression induced by exercise relative to rest.
        - **Slope:** Slope of the peak exercise ST segment (0-2).
        - **CA:** Number of major vessels (0-3) colored by fluoroscopy.
        - **Thal:** 0 = Normal, 1 = Fixed defect, 2 = Reversible defect.
        """)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    with st.expander("ℹ️ Detailed Input Descriptions"):
        st.markdown("""
        - **MDVP:Fo(Hz):** Average vocal fundamental frequency.
        - **MDVP:Fhi(Hz):** Maximum vocal fundamental frequency.
        - **MDVP:Flo(Hz):** Minimum vocal fundamental frequency.
        - **MDVP:Jitter(%):** Variation in fundamental frequency as a percentage.
        - **MDVP:Jitter(Abs):** Absolute variation in fundamental frequency.
        - **MDVP:RAP:** Relative Amplitude Perturbation.
        - **MDVP:PPQ:** Five-point Period Perturbation Quotient.
        - **Jitter:DDP:** Average absolute difference of differences between consecutive periods.
        - **MDVP:Shimmer:** Variation in amplitude as a percentage.
        - **MDVP:Shimmer(dB):** Variation in amplitude in decibels.
        - **Shimmer:APQ3:** Three-point Amplitude Perturbation Quotient.
        - **Shimmer:APQ5:** Five-point Amplitude Perturbation Quotient.
        - **MDVP:APQ:** Amplitude Perturbation Quotient.
        - **Shimmer:DDA:** Average absolute difference of differences between consecutive amplitudes.
        - **NHR:** Noise-to-Harmonics Ratio.
        - **HNR:** Harmonics-to-Noise Ratio.
        - **RPDE:** Recurrence period density entropy.
        - **DFA:** Detrended fluctuation analysis.
        - **Spread1:** Nonlinear measure of fundamental frequency variation.
        - **Spread2:** Nonlinear measure of amplitude variation.
        - **D2:** Nonlinear dynamical complexity measure.
        - **PPE:** Pitch period entropy.
        """)


#Breast Cancer Prediction Page
if selected == "Breast Cancer Prediction":
    
    #radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,
   

    # page title
    st.title("Breast Cancer Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        radius_mean = st.text_input('Radius of Lobes')

    with col2:
       texture_mean= st.text_input('Mean of Surface Texture')

    with col3:
       perimeter_mean = st.text_input('Outer Perimeter of Lobes')

    with col4:
        area_mean = st.text_input('Mean Area of Lobes')

    with col5:
        smoothness_mean = st.text_input('Mean of Smoothness Levels')

    with col1:
        compactness_mean = st.text_input('Mean of Compactness')

    with col2:
        concavity_mean = st.text_input('Mean of Concavity')

    with col3:
        concave_points_mean= st.text_input('Mean of Cocave Points')

    with col4:
        symmetry_mean = st.text_input('Mean of Symmetry')

 #concave points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,
 #compactness_se,concavity_se,concave points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,
 
 
 
    with col5:
        fractal_dimension_mean = st.text_input('Mean of Fractal Dimension')

    with col1:
        radius_se = st.text_input('SE of Radius')

    with col2:
        texture_se = st.text_input('SE of Texture')

    with col3:
        perimeter_se = st.text_input('Perimeter of SE')

    with col4:
        area_se = st.text_input('Area of SE')

    with col5:
        smoothness_se = st.text_input('SE of Smoothness')

    with col1:
        compactness_se = st.text_input('SE of compactness')

    with col2:
        concavity_se = st.text_input('SE of concavity')

    with col3:
        concave_points_se = st.text_input('SE of concave points')

    with col4:
        symmetry_se = st.text_input('SE of symmetry')

    with col5:
        fractal_dimension_se = st.text_input('SE of Fractal Dimension')

    with col1:
        radius_worst = st.text_input('Worst Radius')

    with col2:
        texture_worst = st.text_input('Worst Texture')
        
        #perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave points_worst,symmetry_worst,fractal_dimension_worst
    
    with col3:
        perimeter_worst = st.text_input('Worst Permimeter')

    with col4:
        area_worst = st.text_input('Worst Area')

    with col5:
        smoothness_worst = st.text_input('Worst Smoothness')

    with col1:
        compactness_worst = st.text_input('Worse Compactness')

    with col2:
        concavity_worst = st.text_input('Worst Concavity')

    with col3:
        concave_points_worst = st.text_input('Worst Concave Points')

    with col4:
        symmetry_worst = st.text_input('Worst Symmetry')

    with col5:
        fractal_dimension_worst = st.text_input('Worst Fractal Dimension')




    # code for Prediction
    breast_cancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):

        user_input = [radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,
                      concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,
                      perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,
                      radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,
                      concave_points_worst,symmetry_worst,fractal_dimension_worst]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_cancer_model.predict([user_input])

        if breast_cancer_prediction[0] == 'M':
            parkinsons_diagnosis = "The person has Breast Cancer"
        else:
            parkinsons_diagnosis = "The person have Balign tumour"


    st.success(breast_cancer_diagnosis)
    
    # Information box
    with st.expander("ℹ️ Detailed Input Descriptions"):
        st.markdown("""
        - **Radius Mean:** Mean of distances from the center to points on the perimeter.
        - **Texture Mean:** Mean of gray-level intensity variations.
        - **Perimeter Mean:** Mean of tumor perimeter lengths.
        - **Area Mean:** Mean of the tumor area.
        - **Smoothness Mean:** Mean of local variation in radius lengths.
        - **Compactness Mean:** Mean of (perimeter² / area - 1.0).
        - **Concavity Mean:** Mean of severity of concave portions of the contour.
        - **Concave Points Mean:** Mean of the number of concave portions of the contour.
        - **Symmetry Mean:** Mean symmetry of the tumor shape.
        - **Fractal Dimension Mean:** Mean of coastline approximation (1 - fractal dimension).
        - **Radius SE:** Standard error of the radius.
        - **Texture SE:** Standard error of the texture.
        - **Perimeter SE:** Standard error of the perimeter.
        - **Area SE:** Standard error of the area.
        - **Smoothness SE:** Standard error of smoothness.
        - **Compactness SE:** Standard error of compactness.
        - **Concavity SE:** Standard error of concavity.
        - **Concave Points SE:** Standard error of concave points.
        - **Symmetry SE:** Standard error of symmetry.
        - **Fractal Dimension SE:** Standard error of fractal dimension.
        - **Worst Radius:** Largest value of the radius.
        - **Worst Texture:** Largest value of texture.
        - **Worst Perimeter:** Largest value of the perimeter.
        - **Worst Area:** Largest value of the area.
        - **Worst Smoothness:** Largest value of smoothness.
        - **Worst Compactness:** Largest value of compactness.
        - **Worst Concavity:** Largest value of concavity.
        - **Worst Concave Points:** Largest value of concave points.
        - **Worst Symmetry:** Largest value of symmetry.
        - **Worst Fractal Dimension:** Largest value of fractal dimension.
        """)

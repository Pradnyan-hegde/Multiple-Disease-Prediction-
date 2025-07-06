import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

import json


from user_management import create_account, login, logout



# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/model/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/model/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(f'{working_dir}/model/breast_cancer_model_lg.sav', 'rb'))

liver_model = pickle.load(open(f'{working_dir}/model/liverdisease_model_rf.sav', 'rb'))


# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")



# Custom CSS for minimalist design
def apply_custom_css():
    st.markdown("""
    <style>
        /* Body background */
        body {
            background-color: #000000;
            font-family: Arial, sans-serif;
        }

        /* Sidebar container background */
        [data-testid="stSidebar"] {
            background-color: #000000 !important; /* Force black background */
        }

        /* Buttons */
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 0.5em 1em;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }

        /* Input fields */
        .stTextInput input {
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 0.5em;
            font-size: 16px;
            width: 100%;
        }

        /* Navigation bar styling */
        .nav-bar {
            background-color: #000000;
            padding: 1em;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)
    
# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = None
    
# Redirect logic based on authentication status
if st.session_state["authenticated"]:
    selected = "Prediction"  # Redirect to prediction options if logged in

else:
    selected = "Home"
    

# Apply custom CSS
apply_custom_css()

# Navigation bar conditionally displayed
if selected != "Prediction":
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=["Home", "Create Account", "Login", "About Us"],
            icons=["house", "key", "person-plus", "info-circle"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#000000"},
                "icon": {"color": "blue", "font-size": "25px"},
                "nav-link": {
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#333333",
                    "color": "#ffffff",
                },
                "nav-link-selected": {"background-color": "#007bff", "color": "white"},
            },
        )




# Pages
if selected == "Home":
    st.title("Welcome to the Home Page")
    st.write("Navigate through the app using the sidebar.")
    st.image("C:\\final year project\Home.png", use_column_width=True)

    st.image("C:\\final year project\Services.png", use_column_width=True)    

elif selected == "Login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state["authenticated"] = True
            st.session_state["current_user"] = username
            st.success(f"Welcome, {username}!")
            
        else:
            st.error("Invalid username or password.")

elif selected == "Create Account":
    st.title("Create Account")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        if create_account(new_username, new_password):
            st.success("Account created successfully! You can now log in.")
        else:
            st.error("Username already exists.")

elif selected == "About Us":
    st.title("About Us")
    st.write("""
    Welcome to our website! This application is designed to provide a seamless user authentication experience. 
    The Disease Prediction System analyzes user-provided health data using advanced machine learning algorithms to predict the likelihood of diseases like diabetes, heart disease, Parkinson's, breast cancer and Liver disease, providing accurate risk assessments for early intervention.' 
    We value simplicity, security, and user satisfaction.
    """)
    st.image("C:\\final year project\About.png", use_column_width=True)
    st.image("C:\\final year project\Projects.png", use_column_width=True)
    st.image("C:\\final year project\Contact.png", use_column_width=True)

    

else:
    # Logged-in state
    st.write(f"Logged in as: {st.session_state['current_user']}")
    if st.button("Logout"):
        st.session_state["authenticated"], st.session_state["current_user"] = logout()
        st.success("Logged out successfully.")
        
if selected == "Prediction":
    st.title("Disease Prediction")
    # Sidebar menu for disease prediction       
    # Sidebar menu for navigation
    with st.sidebar:
        selected = option_menu(
            "Prediction Options",
            ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction", "Breast Cancer Prediction", "Liver Disease Prediction"],
            menu_icon="hospital-fill",
            icons=["activity", "heart", "person", "gender-female", "shield-plus"],
            default_index=0,
            orientation="vertical"  # Sidebar is vertical by default
        )

    # Main content area based on the selected option
    if selected == "Diabetes Prediction":
        st.title("Diabetes Prediction using ML")
        # Include your existing code for diabetes prediction here
        
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

            if diab_prediction[0] == 0:
                diab_diagnosis = "Good news! You are not diabetic. 😊 Keep up the healthy lifestyle!"
            else:
                diab_diagnosis = "Unfortunately, you are diabetic. 😔 It's important to consult a healthcare provider for further steps."

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
        
        
        
    elif selected == "Heart Disease Prediction":
        st.title("Heart Disease Prediction using ML")
        # Include your existing code for heart disease prediction here
        
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
            thal = st.text_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect')

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction

        if st.button('Heart Disease Test Result'):

            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'Based on the analysis, it appears you may have heart disease. 😔 It’s important to consult with a healthcare provider for further evaluation and guidance.'
            else:
                heart_diagnosis = "Good news! Based on the analysis, there are no indications of heart disease. 😊 However, it's always a good idea to maintain a healthy lifestyle and keep up with regular check-ups."

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
            - **Thal:** 1 = Normal, 2 = Fixed defect, 3 = Reversible defect.
            """)
        
        
        
        
    elif selected == "Parkinsons Prediction":
        st.title("Parkinson's Disease Prediction using ML")
        # Include your existing code for Parkinson's prediction here
        
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
                parkinsons_diagnosis = "Based on the analysis, it appears you may have Parkinson's disease. 😔 It is important to consult a healthcare provider for further evaluation and personalized guidance."
            else:
                parkinsons_diagnosis = "Great news! Based on the analysis, there are no indications of Parkinson's disease. 😊 However, regular check-ups and maintaining a healthy lifestyle are always beneficial."

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
        
        
     
        
    elif selected == "Breast Cancer Prediction":
        st.title("Breast Cancer Prediction using ML")
        # Include your existing code for breast cancer prediction here

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
                breast_cancer_diagnosis = "Based on the analysis, it appears that you may have malignant breast cancer. 😔 We strongly recommend consulting with a healthcare provider for further evaluation and personalized care."
            else:
                breast_cancer_diagnosis = "The results suggest that you have a benign tumor. 😊 However, it's important to follow up with your healthcare provider for regular monitoring and care."


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
            
            
        
    elif selected == "Liver Disease Prediction":
        st.title("Liver Disease Prediction using ML")
        # Include your existing code for diabetes prediction here
        
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age of the patient')
     
        with col2:
            Bilirubin = st.text_input('Total Bilirubin')

        with col3:
            direct_bili = st.text_input('Direct Bilirubin')

        with col1:
            AAphos = st.text_input('Alkphos Alkaline Phosphotasel')

        with col2:
            Sgpt = st.text_input('Sgpt Alamine Aminotransferase')

        with col3:
            sgot = st.text_input('Sgot Aspartate Aminotransferase')

        with col1:
            prot = st.text_input('Total Protiens')
            
        with col2:
            alb = st.text_input('ALB Albumin')

        with col3:
            ag = st.text_input('A/G Ratio Albumin and Globulin Ratio')

        
        


        # code for Prediction
        liver_diagnosis = ''

        # creating a button for Prediction

        if st.button('Liver Test Result'):

            user_input = [age, Bilirubin, direct_bili, AAphos, Sgpt, sgot, prot, alb, ag]
            

            user_input = [float(x) for x in user_input]

            liver_prediction = liver_model.predict([user_input])

            if liver_prediction[0] == 2:
                liver_diagnosis = 'Based on the results, it appears the person does not have liver disease.'
            else:
                liver_diagnosis = 'Based on the results, it suggests the person may have liver disease.'

        st.success(liver_diagnosis)
        
        with st.expander("ℹ️ Detailed Input Descriptions"):
            st.markdown("""
            - **Age of the Patient:** The age of the individual undergoing evaluation.
            - **Total Bilirubin:** Total amount of bilirubin in the blood; elevated levels may indicate liver dysfunction.
            - **Direct Bilirubin:** Portion of bilirubin that is directly processed by the liver; high levels suggest liver or bile duct issues.
            - **Alkaline Phosphatase (AAphos):** Enzyme linked to the bile ducts; increased levels may indicate blockage or liver disease.
            - **SGPT (Alanine Aminotransferase):** Enzyme found in the liver; elevated levels often indicate liver damage.
            - **SGOT (Aspartate Aminotransferase):** Enzyme found in the liver and other tissues; high levels can suggest liver or heart damage.
            - **Total Proteins (Prot):** Total amount of proteins in the blood, including albumin and globulin; low levels may reflect liver issues.
            - **Albumin (Alb):** Protein made by the liver; lower levels may indicate liver dysfunction.
            - **A/G Ratio (Albumin and Globulin Ratio):** Ratio of albumin to globulin proteins; abnormal values can indicate liver or kidney disease.
            """)
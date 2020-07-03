import streamlit as st
import numpy as np
import pandas as pd
import pickle
import time
import os
from sklearn.externals import joblib 


st.title('Heart Disease Diagnosis Assistant')
st.markdown('This application is meant to assist doctors in diagnosing, if a patient has a **_Heart_ _Disease_ _or_ not** using few details about their health')

model = joblib.load('./SVMClassifier.pkl')  
  
st.markdown('Please **Enter _the_ _below_ details** to know the results -')

age = st.text_input(label='Age')

gender_ls = ['Male', 'Female']
sex = st.selectbox('Gender', gender_ls)

cp_ls = ['Typical Angina', 'Atypical Angina', 'Non-anginal pain', 'Asymptomatic']
cp = st.selectbox('Chest pain Type', cp_ls)

restbp = st.slider('Resting Blood Pressure', 0, 220, 130)

chol = st.slider('Serum Cholestoral in mg/dl', 0, 600, 246)

fbs_ls = ['fasting blood sugar > 120 mg/dl', 'fasting blood sugar < 120 mg/dl']
fbs = st.selectbox('Fasting Blood Sugar (>126 mg/dL signals diabetes)', fbs_ls)


restecg_ls = ['Nothing to Note', 'ST-T Wave abnormality', 'Left Ventricular Hypertrophy']
restecg = st.selectbox('Resting ECG(Electrocardiographic)', restecg_ls)

thalach = st.slider('Maximum Heart Rate Achieved (Thalach)', 0, 250, 100)

exang_ls = ['Yes', 'No']
exang = st.selectbox('Exercise Induced Angina', exang_ls)

oldpeak = st.text_input(label= 'Oldpeak: ST Depression induced by exercise relative to rest')

slope_ls = ['Unslopping: Better heart rate with exercise', 'Flatsloping: Minimal change', 'Downslopings: Signs of unhealthy heart']
slope = st.selectbox('Slope of Peak exercise ST Segment', slope_ls)

ca_ls = [0, 1, 2, 3, 4]
ca = st.selectbox('Number of Major vessels colored by flourosopy', ca_ls)

thal_ls = ['Normal:1', 'Normal:3', 'Fixed defect:6', 'Reversable defect:7']
thal = st.selectbox('Thalium Stress result', thal_ls)

pred = ''
pred = model.predict([[0,1,1,1,1,1,1,1,1,1,1, 0]])

if st.button('Check Diagnosis'):
    with st.spinner('Running the Diagnostic.. '):
        time.sleep(2)
    st.header('The patient {}'.format(str(pred)))


import streamlit as st
import joblib
m=joblib.load("heartdis.joblib")
st.title("Heart Disease Prediction App")
age=st.number_input("Enter your age")
cigs=st.number_input("Enter the number of ciggirates consumed in a day")
totchol=st.number_input("Enter your total cholestrol")
sysbp=st.number_input("Enter your systolic blood pressure")
diabp=st.number_input("Enter your diastolic blood pressure")
bmi=st.number_input("Enter your body mass index")
heartrate=st.number_input("Enter your heart rate")
glucose=st.number_input("Enter your glucose level")
if st.button("Predict"):
    prediction=m.predict([[age,cigs,totchol,sysbp,diabp,bmi,heartrate,glucose]])
    if prediction[0]==1:
        st.write("You might have a heart disease")
    else:
        st.write("You might not have heart disease") 

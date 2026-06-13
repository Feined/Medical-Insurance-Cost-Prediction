import streamlit as st
import pickle
import numpy as np

with open('random_forest.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Medical Insurance Cost Prediction")

age = st.number_input("Age", min_value=18, max_value=100)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)
children = st.number_input("Children", min_value=0, max_value=10)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict"):

    sex_male = 1 if sex == "Male" else 0
    smoker_yes = 1 if smoker == "Yes" else 0

    region_northwest = 1 if region == "northwest" else 0
    region_southeast = 1 if region == "southeast" else 0
    region_southwest = 1 if region == "southwest" else 0

    features = np.array([[age,
                          bmi,
                          children,
                          sex_male,
                          smoker_yes,
                          region_northwest,
                          region_southeast,
                          region_southwest]])

    prediction = model.predict(features)

    st.success(f"Predicted Insurance Cost: ${prediction[0]:,.2f}")
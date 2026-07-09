import streamlit as st
import requests

st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Employee Salary Prediction System")

st.write("Enter employee details below.")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=70,
    value=30
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education Level",
    [
        "Bachelor's",
        "Master's",
        "PhD"
    ]
)

job = st.text_input(
    "Job Title",
    "Data Scientist"
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=5
)

API_URL = "https://salary-mlops-fdp.onrender.com/predict"

if st.button("Predict Salary"):

    employee = {
        "Age": age,
        "Gender": gender,
        "Education_Level": education,
        "Job_Title": job,
        "Years_of_Experience": experience
    }

    try:

        response = requests.post(
            API_URL,
            json=employee
        )

        if response.status_code == 200:

            prediction = response.json()

            st.success(
                f"Predicted Salary : ₹ {prediction['Predicted Salary']:,.2f}"
            )

        else:

            st.error(response.text)

    except Exception as e:

        st.error(e)

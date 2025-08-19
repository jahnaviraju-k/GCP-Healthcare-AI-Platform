import streamlit as st
import pandas as pd
import requests

st.title("🏥 Healthcare AI Dashboard on GCP")

menu = st.sidebar.radio("Select Feature", ["Patient Risk Prediction", "Claims Fraud Analysis"])

if menu == "Patient Risk Prediction":
    st.subheader("Predict Readmission Risk")
    age = st.slider("Age", 20, 100, 50)
    los = st.slider("Length of Stay", 1, 20, 5)
    diabetes = st.selectbox("Diabetes", [0, 1])
    hypertension = st.selectbox("Hypertension", [0, 1])

    if st.button("Predict"):
        payload = {"age": age, "length_of_stay": los, "diabetes": diabetes, "hypertension": hypertension}
        response = requests.post("http://localhost:8080/predict", json=payload)
        st.write(response.json())

elif menu == "Claims Fraud Analysis":
    st.subheader("Fraudulent Claims (Synthetic)")
    df = pd.read_csv("../data/claims.csv")
    st.dataframe(df)

import streamlit as st
from model import predict_marks

st.set_page_config(page_title="Student Marks Predictor")

st.title("📚 Student Marks Prediction App")
st.write("Predict marks based on study hours using Machine Learning")

hours = st.slider("Select study hours:", 0, 10, 1)

if st.button("Predict Marks"):
    marks = predict_marks(hours)
    st.success(f"📈 Predicted Marks: {marks:.2f}")


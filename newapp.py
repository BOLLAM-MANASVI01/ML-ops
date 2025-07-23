import streamlit as st
import requests
st.title("🎓 Student Pass/Fail Predictor")
st.write("Enter marks for 3 subjects to predict whether the student will Pass or Fail")
mark1 = st.number_input("Math Marks", min_value=0,max_value=100,value=50)
mark2 = st.number_input("Science Marks", min_value=0,max_value=100,value=50)
mark3 = st.number_input("English Marks", min_value=0,max_value=100,value=50)
features = [mark1,mark2,mark3]
if st.button("predict"):
    response = requests.post('http://127.0.0.1:8000/predict', json={'features':features})#this url is give the response
    if response.status_code == 200:
        prediction = response.json().get('prediction')
        st.write(f"The model prediction",{'pass' if prediction == 1 else 'fail'})
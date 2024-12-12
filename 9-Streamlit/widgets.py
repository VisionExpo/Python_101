import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")


name = st.text_input("Enter your name:")

age = st.slider("Select your age:",1,100,25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"Your selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name" : ["john", "jane", "jake", "jill"],
    "Age" : [28, 24, 35, 40],
    "City" : ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)

import streamlit as st

import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name")


#creating a slider
age = st.slider("Select your age:",0,100,25)#MIN IS 25 

st.write(f"Your age is {age}.")

#select box 
options= ["python","java","c++","javascript"]
choice =st.selectbox("Choose your favourite language:",options)
st.write(f"Your selected {choice}.")


if name:
    st.write(f"Hello,{name}")

#lets use the dataFrame,py dict,converted into pandas dataFrame
data = {
    "Name":["John","Jane","Jake","Jill"],
    "Age":[25,30,35,40],
    "City":["New York","Los Angeles","Chicago","Houston"]
}

df =pd.DataFrame(data)
df.to_csv("sampledata.csv")# saves that DataFrame to disk as a CSV file in the same folder.
st.write(df)

# To create a file upload button
uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
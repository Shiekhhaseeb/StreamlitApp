import streamlit as st
import pandas as pd
import numpy as np

st.title("My first Streamlit App")

with st.sidebar:
    st.write("Sidebar")
    st.write("This app is a demo of Streamlit")

st.header("This is a header with divider",divider="rainbow")

st.markdown("This is st.markdown")

st.subheader("st.columns")

col1 ,col2 = st.columns(2)
with col1:
    x=st.slider("Choose an x value",1,10)#range is from 1 to 10
with col2:
    st.write("The value of :blue[***x***] is:",x)

df = pd.DataFrame(np.random.default_rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.subheader("st.area_chart")
st.area_chart(df)


name = st.text_input("Enter your name here: ")

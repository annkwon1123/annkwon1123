import streamlit as st
import numpy as np
import pandas as pd

st.write(""" 
#BOOL-BIRD
accident-data.
""")

df = pd.read_csv("output.csv")
x = st.slider('x') # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.write(df)
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is App Buils a Machine Learning Model! ')

with st.expander('Data'):
  st.write('**Raw data**)
  df=pd.read_csv('https://raw.githubusercontent.com/sohamglobal/datasets/main/Flipkart_Mobiles.csv')
  df
  

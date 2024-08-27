import streamlit as st
import pandas as pd

st.title('📱 Mobiles Data Analysis')

st.info('This is App use a Machine Learning Model to analysize the given data ')

with st.expander('Data'):
  st.write('**Raw data**')
  df= pd.read_csv('https://raw.githubusercontent.com/sohamglobal/datasets/main/Flipkart_Mobiles.csv')
  df
  st.write('**X**')
  X = df.drop('Brand', axis=1)
  X
  st.write('**Y**')
  Y= df.Brand
  Y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x= 'Color' , y='Storage', color='Brand')

# Data preparations
with st.sidebar:
  st.header('Input Features')
  brand= st.selectbox('Brand', ('OPPO','SAMSUNG','ASUS','LG','realme','GIONEE','Apple','HTC','IQOO'))
  storage= st.selectbox('Storage', ('8 GB','32 GB','64 GB','128 GB','256 GB','512 GB'))
  rating= st.slider('Rating', 3.6, 4.9, 4.5 )
  
  

  
  

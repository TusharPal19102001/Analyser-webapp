# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:42:22 2023

@author: Lenovo
"""
#importing libraries
import streamlit as st
import pandas as pd
import seaborn as sns


st.title("Data Analysis")      #title for webapp
st.subheader("Data Analysis using Python & Streamlit")

#section to upload dataset int the web app
# Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
    data=pd.read_csv(upload)


# Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        
        
#  Check DataType of Each Column
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        



# Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    data_shape=st.radio("What Dimension Do You Want To Check?",('Rows',
                                                                'Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

#  Find Null Values in The Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!!,No Missing Values")
        

#Find Duplicate Values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
    
if st.button('Save DataFrame'):
    open('data_streamlit.csv','w').write(data.to_csv())
    st.text("Saved To local Drive")

        
#about section
if st.button("About app"):
    st.text("Built with streamlit")
    st.text("Thanks to streamlit")
    
#made by whom
if st.checkbox("made bY"):
    st.success("Tushar Pal")
import streamlit as st
import numpy as np
import pandas as pd

st.title("Mavericks Graphical Insights Model")

"""# Mavericks Test Run"""

############################################
############## UPLOAD A FILE ###############
############################################

uploaded_file = st.file_uploader("Upload your Dataset", type = 'csv')
data = pd.read_csv(uploaded_file)

if uploaded_file is not None:
    # col1, col2 = st.columns([1,1])

    # with col1:
    st.info("CSV Uploaded Successfully")
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

    st.info("Summary Statistics")
    st.write(data.describe())

    st.info("Number of Nulls in Each Column")
    st.write(data.isnull().sum())

############################################
################ INPUT QUERY ###############
############################################

# with container:
with st.form(key="my_form", clear_on_submit=True):
    user_input = st.text_input("Query:", placeholder="What would you like to know about your data?", key='input')
    submit_button = st.form_submit_button(label="chat")


############################################
################ ACCURE API ################
############################################

import requests 
url = 'https://6xz1owomvn04h0-80.proxy.runpod.net/query' 
headers = {     
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoic2Fuc2FyaSIsImV4cCI6MTc5NjMxMDQ0NH0.FgFpk64W54Uoai0mEv8rZdQtOgaBC7j_pa2Bd7VLJjE',     
    'Content-Type': 'application/json'
} 
data = {
    "org": "Accure__demo", 
    "question": "what is solar system?"
} 
response = requests.post(url, headers=headers, json=data) 
print(response.status_code)
print(response.json())







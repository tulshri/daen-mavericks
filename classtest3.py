import streamlit as st
import numpy as np
import pandas as pd
import re

st.title("Mavericks Graphical Insights Model")

"""# Mavericks Test Run"""

############################################
############## UPLOAD A FILE ###############
############################################

uploaded_file = st.file_uploader("Upload your Dataset", type = 'csv')

if uploaded_file is not None:
    # col1, col2 = st.columns([1,1])

    # with col1:
    st.info("CSV Uploaded Successfully")
    data = pd.read_csv(uploaded_file)
    # snapshot = data.head(5).to_string()
    st.dataframe(data)

    # st.info("Summary Statistics")
    # st.write(data.describe())

    # st.info("Number of Nulls in Each Column")
    # st.write(data.isnull().sum())

    snapshot = data.head(40).to_string()

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
    def query(payload):
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    output = query({
        "org": "Accure__demo", 
        "question": f"For the following partial dataset \n {snapshot} \n in the csv file, can you answer the following query: {user_input}? ?"
    })
    output['generated_text']

############################################
####### HUGGING FACE CODE LLAMA API ########
############################################

# import requests
# API_URL = "https://api-inference.huggingface.co/models/codellama/CodeLlama-34b-Instruct-hf"
# headers = {"Authorization": "Bearer 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"}
# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
# output = query({
#     "inputs": f"For the following snapshot \n {column_names} \n in the csv file, can you write a python script for the following query: {user_input}?",
#     "num_tokens": 1000,
#     "stop": "\n\n"
# })
# output
# python_code = re.findall(r"```(.*?)```", output[0]['generated_text'], re.DOTALL)
# python_code

# output = query({
#     "org": "Accure__demo", 
#     "question": f"For the following snapshot of the data \n {snapshot} \n can you write a python script for the total number of cases in the health district of Fairfax and Prince William? "
# })
# output


############################################
############### TO DO LIST #################
############################################

# include csv file in the user-uploaded variable
# ensure the csv file is not None
# prompt engineering - tuning the question 
# extracting the python code, removing extra language
# converting python code to visualization via library (lida, pandas, plotly)
# make sure the code references the correct dataset




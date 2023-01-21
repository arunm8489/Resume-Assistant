import re
import os 
import spacy
import pickle
import pandas as pd
from utils import *
import streamlit as st
import shutil

NER_MODEL = spacy.load(r"models/ner-model") #load the best model
XGB_MODEL = load_pkl(r"models/xgboost-model/xgb_model.pkl")
TOP_300_SKILLS = load_pkl(r"models/top_300_skills.pkl")
JD_SKILLS = load_pkl(r"models/jd_skills.pkl")



def predict_label(text):
   """
   predict label and probability from text
   """

   out = NER_MODEL(text)
   predicted_skills = list(out.ents)
  
   skills = [p.text.lower() for p in predicted_skills]
   out_vec,col_names = generate_one_hot_vec(skills,TOP_300_SKILLS)
   sim = similarity_jd(skills,JD_SKILLS)
   d = [sim] + out_vec

   sample_x = pd.DataFrame([d],columns=['similarity'] + col_names)
   sample_y_pred = XGB_MODEL.predict(sample_x)
   pred_prob = XGB_MODEL.predict_proba(sample_x)[:,1]
   return sample_y_pred[0],pred_prob[0]

def save_file(pdf_file,file_name):

    if not os.path.exists('tmp'):
        os.makedirs('tmp')

    full_path = os.path.join('tmp',file_name)
    with open(full_path, 'wb') as f: 
        f.write(pdf_file.getvalue())
        print(f'{file_name} saved succesfuly')
        return full_path 

st.title('Resume shortlisting Assistant')

with st.form(key="Form :", clear_on_submit = True):
    Files = st.file_uploader(label = "Upload Pic", type=["pdf","docx"],accept_multiple_files=True)
    Submit = st.form_submit_button(label='Submit')


if Submit :
    st.text(" ")
    st.markdown("**File Uploaded Successfully. Calculating results....**")
    data = []
    for i in range(len(Files)):
        pdf_file = Files[i]
        file_name = pdf_file.name
        pdf_file_path = save_file(pdf_file,file_name)
        text = convert_pdf_to_text(file_path=pdf_file_path)
        label,prob = predict_label(text)
        label = 'Yes' if label == 1 else 'No'
        data.append((file_name,label,prob))
        # os.remove(pdf_file_path)
    
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')

    df = pd.DataFrame(data,columns=['file name','Shortlisted','Probability'])
    df = df.sort_values(by=['Probability'],ascending=False)


    ## color dataframe
    def highlight_shortlisted(s):
        return ['background-color: LightGreen']*len(s) if s.Shortlisted == 'Yes' else ['background-color: LightCoral']*len(s)
    st.text(" ")
    st.text(" ")
    st.dataframe(df.style.apply(highlight_shortlisted, axis=1), width=10000)
    st.text(" ")

 






    


    

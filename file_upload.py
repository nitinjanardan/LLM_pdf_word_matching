import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import PyPDF2
import re
import openai
from openai import OpenAI
import os 
import json 
from dotenv import load_dotenv, dotenv_values, find_dotenv

# load dotenv file
load_dotenv()
# fetching open ai key
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# fetching model name 
model_name = os.getenv("COMPLETIONS_MODEL")
def pdf_upload(file) -> str:
    pdf_file = file.name

    pdf_reader = PyPDF2.PdfReader(file)
    # Extract the content
    content = " "
    for page in range(len(pdf_reader.pages)):
        content += pdf_reader.pages[page].extract_text()
    # Display the content
    return content
    
def pdf_and_question(pdf_read,question) -> str:
     client = OpenAI()
     pdf_read= pdf_read.lower()
     question = question.lower()
     ques = question.split("\n")
     
     qna_dict = dict()
     for i in range(0,len(ques)):
        response = client.chat.completions.create(model=model_name,
     messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'The following is the context followed by a question.\n{pdf_read}\n\nQuestion: {ques} \nPlease answer the question based on the context.'},
        {"role": "user", "content": f'Output should be word to word match if the {ques} is a word to word match. If the answer is of low confidence then give the output as "Data Not Available"'}
    ])
        res_message =response.choices[0].message.content
        qna_dict.update({ques[i]:res_message})
     json_qna = json.dumps(qna_dict)
     st.write(json_qna)




import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import PyPDF2
import re
def pdf_upload(file):
    pdf_file = file.name

    pdf_reader = PyPDF2.PdfReader(file)
    # Extract the content
    content = " "
    for page in range(len(pdf_reader.pages)):
        content += pdf_reader.pages[page].extract_text()
    # Display the content
    return content
    
def pdf_and_question(pdf_read,question):
    st.write(pdf_read)
    st.write(question)


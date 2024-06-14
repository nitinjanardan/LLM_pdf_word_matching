import streamlit as st
import time 
import file_upload as fp

st.title("PDF word Matcher")
form = st.form("Basic")
file_upload = form.file_uploader("Upload PDF", type=["pdf"])
question = form.text_area(label ="Enter your Question",  placeholder="Please provide each questions in separate line")
submit = form.form_submit_button("Upload")
    # vlaidating the form.
if submit:
    if file_upload is None or question =="":
        alert = st.warning("Please upload a file and question 💀💀")
        # time.sleep(3)
        # alert.empty()
    else:
        # st.write(file_upload)
        pdf_read = fp.pdf_upload(file_upload)
        # with st.spinner("uploading........"):
            # time.sleep(3)
        # st.write(pdf_read)
        # placeholder = st.empty()
        # time.sleep(5)
        # placeholder.empty()
        pdf_que = fp.pdf_and_question(pdf_read,question)
        # time.sleep(4)
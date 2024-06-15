PDF Question Answering System
This repository contains a Python script that extracts answers to specific questions from a given PDF content using OpenAI's GPT-3.5 API. The script finds exact matches for questions in the PDF content and leverages the API to generate responses based on the context.

--Features
PDF Content Processing: Converts PDF content to lowercase and splits it into meaningful segments.
OpenAI GPT-3.5 Integration: Uses OpenAI's gpt-3.5-turbo-0125 API to generate responses based on the context from the PDF.
Exact Match Handling: Prioritizes exact word-to-word matches to ensure accurate responses.
Fallback Mechanism: Returns "Data Not Available" if the confidence level is low.

--Requirements
Python 3.7+
streamlit library
openai library

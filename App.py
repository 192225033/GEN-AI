import streamlit as st
import google.generativeai as genai

st.title("HI THERE ! IT'S DHARSHAN HERE")

genai.configure(api_key="AIzaSyB3DAt1cg0yAnKMk00Rn_FU8IApOXi8u2E")

text=st.text_input("Enter your question") 

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click Here"):
    response = chat.send_message(text)
    st.write(response.text)
import streamlit as st
st.title("User details form")
name = st.text_input("Enter Your Name")
age = st.text_input("Enter your age")
if st.button("Submit"):
  st.write("Name", name)
  st.write("Age", age)

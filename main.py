# pip install streamlit
# pip install openai

# Streamlit is a library that allowds data scientists to build simple POC (Proof of concept) applications very quickly, you do not have to use frontend frameworks such as react.js etc., this library will do the job
import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "American"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-", item)

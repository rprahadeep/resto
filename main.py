import streamlit as st
import langchain_helper as chain

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Mexican", "Italian", "American", "Arabian", "Japanese", "Korean"))

if cuisine:
  response = chain.generate_restaurantname_items(cuisine)

  st.header(response['restaurant_name'].strip())

  menu_items = response['menu_items'].strip().split(",")

  st.write("**Menu Items**")

  for item in menu_items:
    st.write("-",item)

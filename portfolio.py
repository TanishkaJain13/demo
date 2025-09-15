import streamlit as st
from views import about_me
# --- PAGE SETUP ---
st.set_page_config(page_title="Portfolio", page_icon=":material/account_circle:")

st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made by Tanishka")

st.title("Welcome to My Portfolio")
st.write("Use the sidebar to navigate through the projects.")


with st.expander("About Me"):
    about_me.display()
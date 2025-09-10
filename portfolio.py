import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Portfolio", page_icon=":material/account_circle:")

# --- SHARED ON ALL PAGES ---
st.logo("assets/codingisfun_logo.png")
st.sidebar.text("Made with ❤️ by Taani")

# --- MAIN CONTENT (Landing Page) ---
st.title("Welcome to My Portfolio")
st.write("Use the sidebar to navigate through the projects.")

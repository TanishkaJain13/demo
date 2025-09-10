import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    # contact_form()
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    message = st.text_area("Your Message")
    submit_button = st.button("Submit")

    if submit_button:
        st.success("Your message has been successfully sent!")

# --- HERO SECTION ---
col1, col2 = st.columns(2,gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile_image.png",width=230)
with col2:
    st.title("Sven Alchemy", anchor=False)
    st.write("Data Analyst, asisting enterprises by supporting data-driven decision making.")

    if st.button("✉️Contact Me"):
        show_contact_form()

# --- EXPERIENCE AND QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor= False)
st.write(
    """
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team player and displaying a strong sense of initiative on tasks"""
)


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programing : Python (Pandas, Numpy), SQL, VBA
    - Data Visualization: PowerBI, Tableau, MS Excel, Plotly, Matplotlib, Seaborn
    - Databases: Postgres, MySQL
    """
)
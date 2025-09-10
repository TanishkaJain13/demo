# ------------------- This .py file is not in use right now ----------------------------

import streamlit as st
import re
import requests

# use webhooks for no code tool to process the message for automating the whole process like forwarding the message to an email account or saving to a database now to trigger that automation flow.
WEBHOOK_URL = ""

def is_valid_email(email):
    #basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.")
                st.stop()
            
            if not name:
                st.error("Please provide your name.")
                st.stop()
            
            if not email:
                st.error("Please provide your email address.")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address.")
                st.stop()

            if not message:
                st.error("Please provide a message.")
                st.stop()


            #Prepare data payload and send it to tje specified webhook url
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL,json=data)

            if response.status_code == 200:
                st.success("Your message has been sent successfully!")
            else:
                st.error("There was an error sending your message.")
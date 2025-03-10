import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pathlib import Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
st.title("Contact us")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
time = datetime.now()

def send_email(subject, body, to_email):
    from_email = "remydushimimana24@gmail.com"  # replace with your email
    password = "eauylksllnkenjva"  # replace with your email password

    # Create the email headers and body
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # replace with your SMTP server and port
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

st.subheader("Get in touch with us here")
with st.form(key="user_form_info"):
    with st.container():
        first_name = st.text_input("**your First_name:**")
        last_name = st.text_input("**your Last_name:**")
        email = st.text_input("**Your Email:**")
        message = st.text_area("**Your message:**")
        submit = st.form_submit_button(label="Submit")
    
    if submit:
        if not first_name or not last_name:
            st.write("Please fill in all the Name fields!")
        elif not email:
            st.write("Please fill in the Email field!")
        elif not message:
            st.write("Please fill in the Message field!")
        else:
            subject = f"New message from {first_name} {last_name}"
            body = f"Name: {first_name} {last_name}\nEmail: {email}\nMessage: {message}"
            to_email = "your_email@example.com"  # replace with your receiving email address

            if send_email(subject, body, to_email):
                st.success("Your message has been sent successfully!")
                st.balloons()
            else:
                st.error("There was an error sending your message.")


st.divider()
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        kigali_coords = [-1.9536, 30.0636]
        st.subheader("Map Location")
        map_data = pd.DataFrame(
            np.random.randn(100, 2) / [50, 50] + kigali_coords,
            columns= ["LON", "lat"]
        )     
        st.map(map_data)
    with col2:
         st.subheader("You can find us on")
         st.write("**Number**:  " " +250 795 057 383")
         st.write("**Email**:  "  " remydushimimana24@gmail.com")
         st.write("**Street**: " " KN250 / Nyamirambo")
st.markdown(f"""
<div style='text-align: center; font-size: small;'>
    © {time:%Y} RemyMadeIt All rights reserved
</div>
""", unsafe_allow_html=True)         

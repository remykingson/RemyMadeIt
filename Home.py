import streamlit as st
import os
from datetime import datetime
import pandas as pd
import numpy as np
import time
from pathlib import Path

current_dir = Path(__file__).parent if"__file__" in locals() else Path.cwd()
image_file = current_dir / "static" / "me.JPG"

# page title

st.set_page_config(page_title="RemyMadeIt | Home")

# hiding the html tags inoder to appers to our screen 

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
Time = datetime.now()
# sessions to check whether the user is exists or not 
if "step" not in st.session_state:
      st.session_state.step = 1
if "info" not in st.session_state:
      st.session_state.info = {}

def go_to_step1():
      st.session_state.step = 1

def go_to_step2(name):
      st.session_state.info["name"] = name
      st.session_state.step = 2      
if st.session_state.step == 1:
      st.title("Welcom To Remy Made It's Blog")
      st.caption("We gland to see you here!") 
      name = st.text_input("**Enter your Name Please  :**")
      submit = st.button("Submit",key="unique")
      if submit:
            if not name:
                  st.write("Please fill the empty field to continue!!")
            else:
                  st.success("You've successfully submitted ! you can continue now!!")
                  st.balloons()
                  st.button(label="Continue", on_click=go_to_step2, args=(name,))
       
# if user successfully submitted to our blog then continue to view our pages
 
elif st.session_state.step == 2:
      @st.cache_data
      def Loading_data():     
            time.sleep(10)          
      data = Loading_data()
      st.write(data)
      with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.button("Back", on_click=go_to_step1())
            with col2:
                  st.subheader(f"**Welcome**   {st.session_state.info.get("name")}")
      st.divider()
      st.title("Our Services")
      st.write("At **RemyMadeIt**, we are dedicated to providing exceptional services that cater to your unique needs. Based in Kigali, Rwanda, we specialize in a wide range of solutions to help you achieve your goals with efficiency and creativity.")
      with st.container(border= True):
            col1, col2 = st.columns(2)
            with col1:
                  st.subheader("Graphic Design")
                  st.write("We offer you the best graphic design that enhance user  experience and effectively convey brand messages. Whether it's designing logos, crafting marketing materials, or developing intuitive UI/UX designs, I strive to deliver high-quality work that exceeds expectations.")
            with col2:
                  tab3, tab1, tab4, tab2 = st.tabs( {"PhotoManipulation", "PostDesign", "Logos", "Branding"})
                  with tab1:
                      st.image(os.path.join(os.getcwd(), "static","bro.jpg"))
                  with tab2:
                      st.image(os.path.join(os.getcwd(), "static","chi.jpg"))
                  with tab3:
                      st.image(os.path.join(os.getcwd(), "static","Logo.jpg"))
                  with tab4:
                      st.image(os.path.join(os.getcwd(), "static","visit.jpg"))
      with st.container(border= True):
            col1, col2 = st.columns(2)
            with col1:
                  tab1, tab2 = st.tabs( { "Designing UI/UX", "Website-Design / System-Design"})
                  with tab1:
                      st.write("As a UI/UX designer, I focus on creating intuitive and engaging user interfaces that provide a seamless experience. I believe that great design is not only about looks but also about how it works. I employ user-centered design principles to ensure that the interfaces I create are easy to use, efficient, and accessible. By conducting user research, creating wireframes, and iterating on designs based on feedback, I aim to build products that users love.")                      
                  with tab2:
                      st.write("Website Designer As a website designer, I focus on creating visually stunning and highly functional websites that cater to the needs of my clients and their users. I work on everything from layout and visual elements to user interface (UI) and user experience (UX) design. My approach is to ensure that each website not only looks great but also provides an intuitive and engaging experience. By combining modern design principles with innovative techniques, I build websites that are both aesthetically pleasing and easy to navigate.")
                      
            with col2:
                  st.subheader("Website Development")
                  st.write("Developer I specialize in building responsive, user-friendly websites and applications. My expertise includes HTML, CSS, JavaScript, and various frameworks and libraries. I'm dedicated to writing clean, efficient code and always strive to stay updated with the latest industry trends and technologies. Whether it's developing a sleek website or a complex web application, I aim to deliver solutions that are both functional and visually appealing.")
                
      with st.container():
            st.title("About Me")
            st.write("As a developer, I specialize in creating engaging, user-friendly websites and applications. My expertise spans HTML, CSS, JavaScript, and various frameworks and libraries. I am passionate about writing clean, efficient code and continually expanding my knowledge to stay on the cutting edge of technology.")
            st.write("In addition to development, I excel in graphic design. I create visually stunning graphics that enhance user experience and effectively convey brand messages. Whether it's designing logos, crafting marketing materials, or developing intuitive UI/UX designs, I strive to deliver high-quality work that exceeds expectations.")
            st.write("My goal is to merge functionality with aesthetics, ensuring that each project not only works seamlessly but also looks fantastic. I love collaborating with others to bring ideas to life and am always excited to take on new challenges.Let's connect and create something amazing together!")
      with st.container(border= True):
            col1, col2 = st.columns(2)
            with col1:
                 st.image(os.path.join(os.getcwd(), "static","me.jpg"))
            with col2:   
                  st.write("I am Dushimimana Remy, a visionary developer, graphic designer, and the Founder & CEO of RemyMadeIt. With two years of experience in software development and a strong foundation in visual aesthetics, I merge technical expertise with creative innovation to craft impactful digital solutions. My passion for design and technology drives me to create seamless, user-centric experiences that stand out in both functionality and aestuser-centrichetics.")
                  
css_file = current_dir / "style" / "home.css"
with open(css_file) as f:
      st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)     
st.markdown(f"""
<div style='text-align: center; font-size: small;'>
      © {Time:%Y} RemyMadeIt All rights reserved
</div>
""", unsafe_allow_html=True)



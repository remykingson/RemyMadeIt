import streamlit as st
import os

st.set_page_config(page_title="RemyMadeIt | Services")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Our Services")
st.write("At **Remy Made It company**, we are dedicated to providing exceptional services that cater to your unique needs. Based in Kigali, Rwanda, we specialize in a wide range of solutions to help you achieve your goals with efficiency and creativity.")
with st.container(border= True):
            col1, col2 = st.columns(2)
            with col1:
                  st.subheader("Graphic Design!")
                  st.write("We offer you the best graphic design that enhanc user  experience and effectively convey brand messages. Whether it's designing logos, crafting marketing materials, or developing intuitive UI/UX designs, I strive to deliver high-quality work that exceeds expectations.")
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
                  tab1, tab2 = st.tabs( {"Designing UI/UX", "Website-Design / System-Design"})
                  with tab1:
                      st.write("UI/UX Designer As a UI/UX designer, I focus on creating intuitive and engaging user interfaces that provide a seamless experience. I believe that great design is not only about looks but also about how it works. I employ user-centered design principles to ensure that the interfaces I create are easy to use, efficient, and accessible. By conducting user research, creating wireframes, and iterating on designs based on feedback, I aim to build products that users love.")
                  with tab2:
                      st.write("Website Designer As a website designer, I focus on creating visually stunning and highly functional websites that cater to the needs of my clients and their users. I work on everything from layout and visual elements to user interface (UI) and user experience (UX) design. My approach is to ensure that each website not only looks great but also provides an intuitive and engaging experience. By combining modern design principles with innovative techniques, I build websites that are both aesthetically pleasing and easy to navigate.")
                      
            with col2:
                  st.subheader("Website Develpment!")
                  st.write("Developer I specialize in building responsive, user-friendly websites and applications. My expertise includes HTML, CSS, JavaScript, and various frameworks and libraries. I'm dedicated to writing clean, efficient code and always strive to stay updated with the latest industry trends and technologies. Whether it's developing a sleek website or a complex web application, I aim to deliver solutions that are both functional and visually appealing.")


st.markdown("""
<div style='text-align: center; font-size: small;'>
    © 2024 All rights reserved by Remy
</div>
""", unsafe_allow_html=True)         

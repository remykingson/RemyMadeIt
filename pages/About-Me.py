import streamlit as st
import os
st.set_page_config(page_title="RemyMadeIt | About-Me")
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
                st.subheader("CEO / FOUNDER")
                st.write("Hello! I'm Dushimimana Remy, and I am a dedicated developer and graphic designer and also CEO and Founder.In fact I been 2years in making a robust background in coding and a keen eye for visual aesthetics, I bring a unique blend of technical prowess and creative innovation to all my projects.")
                    

st.markdown("""
<div style='text-align: center; font-size: small;'>
    © 2024 All rights reserved by Remy
</div>
""", unsafe_allow_html=True)
         

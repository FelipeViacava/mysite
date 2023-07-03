# ----- IMPORTS ----- #
import streamlit as st
from pathlib import Path
from PIL import Image

# ----- PATH SETTINGS ----- #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ----- GENERAL SETTINGS ----- #
PAGE_TITLE = "Felipe Viacava | Digital CV"
PAGE_ICON = ":wave:"
NAME = "Felipe Viacava"
DESCRIPTION = """
Credit Risk Analyst at Santander and Data Science Graduate Student at Insper
São Paulo, Brazil
"""
EMAIL = "felipeviacava1@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/FelipeViacava",
    "Linkedin": "https://linkedin.com/in/FelipeViacava",
}
PROJECTS = {
    "⚽🎮 EA Sports FIFA player suggestion system using Shiny Apps": "https://felipeviacava.shinyapps.io/Scout-Buddy/"    
}

# ----- STREAMLIT PAGE CONFIGURATION ----- #
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)
st.title("Hello, stranger!")

# ----- STYLING AND ASSETS ---- #
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)
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
Credit Risk Analyst at Santander and Data Science Graduate Student at Insper. \n
São Paulo, Brazil
"""
EMAIL = "felipeviacava1@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/FelipeViacava",
    "Linkedin": "https://linkedin.com/in/FelipeViacava",
}

# ----- CV AND PORTFOLIO ----- #
PROJECTS = {
    "⚽🎮 EA Sports FIFA player suggestion system using Shiny Apps": "https://felipeviacava.shinyapps.io/Scout-Buddy/"    
}
WORK_EXPERIENCE = [
    {
        "company": "Santander Brasil",
        "position": "Risk Analyst I",
        "span": "Feb/23 - Present",
        "desc": "Using big data to support decision making on the bank's retail credit policies."
    },
    {
        "company": "Claro Brasil",
        "position": "Data Analyst",
        "span": "May/22 - Nov/22",
        "desc": "Implementing data quality routines in the company's internal website along with front and back end developers."
    },
    {
        "company": "Blue Media Services",
        "position": "Assistant Data Scientist",
        "span": "Apr/21 - Jan/22",
        "desc": "Data analysis to support decision making along with Machine Learning model building and evaluation."
    }
]
SCHOOLS_ATTENDED = [
    {
        "school": "Insper - Triple Accredited Business School (AACSB, AMBA, EQUIS)",
        "span": "Oct/22 - Mar/24",
        "degree": "Advanced Program in Data Science and Decision Making (postgraduate)"
    },
    {
        "school": "Insper - Triple Accredited Business School (AACSB, AMBA, EQUIS)",
        "span": "Jan/16 - Dec/21",
        "degree": "Mechanical Engineering (B.Sc)"
    }
]
CERTIFICATES = [
    {
        "company": "Stanford",
        "title": "Machine Learning",
        "desc": "80 hour-long online course about the fundamentals of Machine Learning algorithms.",
        "span": "Aug/21",
        "link": "https://coursera.org/share/fb3add734f44f45afb3895ad84f2ff46"
    }
]
HARD_SKILLS = [
    {
        "name": "Python",
        "desc": """
            Solid work and academic experience using Python for Machine Learning, 
            Data Analysis and Numerical Optimization using Scikit-learn, Pandas, PySpark and Seaborn.
            Web App development using Streamlit and Flask.
        """
    },
    {
        "name": "R programming",
        "desc": """
            Academic experience with data analysis and Machine Learning using tidymodels, tidyverse and ggplot2.
        """
    },
    {
        "name": "SQL and Excel",
        "desc": """
            Solid work experience using SQL to extract summarized datasets for further analysis with Excel
            (or Python if PySpark is not available)
        """
    },
    {
        "name": "Git",
        "desc": "Code sharing and version control with Git (using Github and Bash)"
    },
    {
        "name": "Languages",
        "desc": "Portuguese (mother tongue), English (advanced) and Spanish (beginner)"
    }
]

# ----- STREAMLIT PAGE CONFIGURATION ----- #
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title(PAGE_TITLE)

# ----- STYLING AND ASSETS ---- #
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ----- HERO SECTION ----- #
col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume (PT-BR)",
        data=PDFbyte,
        file_name="application/octet-stream"
    )
    st.write(EMAIL)

# ----- SOCIAL LINKS ----- #
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ----- CV ----- #
st.write("#")
# work experience
st.subheader("Work experience")
for work in WORK_EXPERIENCE:
    st.write(
        f"""
        - {work["company"]} | {work["position"]} | {work["span"]} \n
            {work["desc"]}
        """
    )
# schools attended
st.subheader("Schools Attended")
for school in SCHOOLS_ATTENDED:
    st.write(
        f"""
        - {school["school"]} | {school["span"]} \n
            {school["degree"]}
        """
    )
# certificates
st.subheader("Certificates")
for certificate in CERTIFICATES:
    st.write(
        f"""
        - [{certificate["company"]}]({certificate["link"]}) | {certificate["span"]} \n
            {certificate["desc"]}
        """
    )
# hard skills
st.subheader("Hard Skills")
for skill in HARD_SKILLS:
    st.write(
        f"""
        - {skill["name"]} \n
            {skill["desc"]}
        """
    )
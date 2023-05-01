import base64

import streamlit as st

from pdfmaker import PDFMaker
from resume import Resume

st.set_page_config(page_title="Resume Maker", page_icon=":sunglasses:")
st.title('Make your resume')
st.write("Use AI to generate your own resume. Answer the following questions to provide us with some information")


def validate_input(*args):
    for arg in args:
        if not arg:
            return False
    return True


def download_pdf():
    with open('output.pdf', 'rb') as f:
        pdf_bytes = f.read()
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="example.pdf">Download PDF file</a>'
    return href


with st.form(key='background'):
    name = st.text_input('*Your name',
                         placeholder='Name')
    contact = st.text_area('*How to contact you',
                           placeholder='Email, Tel, LinkedIn ...')
    education = st.text_area('*What is your education background',
                             placeholder='Degree, School, Major, Duration, Courses, GPA, ...')
    skills = st.text_area('*Do you have any skills',
                          placeholder='Programming languages, Frameworks ...')
    experience = st.text_area('*What is your work experience',
                              placeholder='Company, Title, Duration, Description, ...')
    projects = st.text_area('*Do you have any projects',
                            placeholder='Project name, Role, Duration, Description, ...')
    job = st.text_area('*Your applied job and qualifications',
                       placeholder='Responsibility, Minimum qualifications, Preferred qualifications, ...')
    run_button = st.form_submit_button(label='Generate')

    if run_button:
        if validate_input(name, contact, education, skills, experience, projects, job):

            resume = Resume(name=name,
                            contact=contact,
                            education=education,
                            skills=skills,
                            experience=experience,
                            projects=projects,
                            job=job)
            latex_code = resume.run()

            pdf_maker = PDFMaker()
            if pdf_maker.run(latex_code):
                st.markdown(download_pdf(), unsafe_allow_html=True)
            else:
                st.error("Error occurred when generating PDF. Retry it.")
        else:
            st.error("Please enter all required information.")

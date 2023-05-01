import openai

import config


class Resume:

    def __init__(self, name, contact, education, skills, experience, projects, job):
        self.api_key = config.GPT_API_KEY
        self.model_engine = "text-davinci-003"
        self.name = name
        self.contact = contact
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.job = job

    def construct_prompt(self):
        return 'I am applying a job and you are a resume expert. I want you to generate an excellent, retouched ' \
               'and professional resume with provided information. \n This resume needs to be highly tailored ' \
               'to the job description. For every my experience or project you need to touch it up and add more ' \
               'details to make the content with no less than 3 bullet points. Each bullet point needs to be written ' \
               'in a professional and informative way with no less than 15 words. \n ' \
               'Reply me with a script of well-formatted, strictly one-page long latex code of your retouched resume. ' \
               'Do not use package fontspec, use default font only. Don not reply justifications of your answer or any ' \
               'introduction or summary. \n\n' \
               'This is the description of the job, you need to make my resume meet the expectations: \n ' \
               f'{self.job} \n \n ' \
               'Here is my basic information, add more details: \n \n' \
               f'Name: {self.name} \n ' \
               f'Contact Information: {self.contact} \n ' \
               f'Education background: {self.education} \n ' \
               f'Skills: {self.skills} \n ' \
               f'Experience: {self.experience} \n ' \
               f'Projects: {self.projects} \n \n '


    def run(self):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model=self.model_engine,
            prompt=self.construct_prompt(),
            max_tokens=3000,
            temperature=0
        )
        generated_text = response["choices"][0]["text"]

        print(generated_text)

        return generated_text

import openai


class Resume:

    def __init__(self, name, contact, education, skills, experience, projects, job):
        self.api_key = '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'
        self.model_engine = "text-davinci-003"
        self.name = name
        self.contact = contact
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.job = job

    def construct_prompt(self):
        return 'I am applying a job now and you are a resume expert. I want you to generate an excellent, retouched ' \
               'and professional resume with provided information. This resume needs to be highly tailored ' \
               'to the job description. So for every experience or project item you need to use more ' \
               'details to expand my information with no less than 3 bullet points to meet the expectations of the ' \
               'job. Each bullet point needs to be written in a professional and informative way ' \
               'This is the description of the job (don’t put it into resume): \n ' \
               f'{self.job} \n \n ' \
               'Here is something about me: \n \n' \
               f'Name: {self.name} \n ' \
               f'Contact Information: {self.contact} \n ' \
               f'Education background: {self.education} \n ' \
               f'Skills: {self.skills} \n ' \
               f'Experience: {self.experience} \n ' \
               f'Projects: {self.projects} \n \n ' \
               'Do not use package fontspec, use default font only. Please remember only reply me with the whole ' \
               'well-formatted one-page long latex code. Don not reply justifications of your answer or any ' \
               'introduction or summary.'

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

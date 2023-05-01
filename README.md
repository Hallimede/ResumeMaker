# ResumeMaker

## Introduction

This application can automatically generate a resume pdf document based on the user's profile and the description of the target job. It requires users to fill in their basic information, as well as a job description, and then a generated resume can be downloaded.

## Background

Nowadays, people often use Chat-GPT to help embellish their resumes. However, there are often problems such as incomplete description of necessary information, mismatch between resume and target position, and the generated text still needs to be typeset by yourself. Therefore, a one-stop platform to gather user information, adapt to the requirement of target positions and automatically generate formatted resume documents need to be created.

## Code Structure

- main.py
  
    Run the streamlit application and accept information input from the user

- resume.py

    Construct request prompt and call OpenAI API to get latex code

- pdfmaker.py
    
    Call LaTeX.Online API to generate pdf document

## Lessons

- Prompt is important when using OpenAI API (or any other language model) because it provides the model with context and guidance on what task to perform or what output to generate. So be as specific as we can. My designed prompt contains four parts:

  - Instruction: generate an excellent, retouched and professional resume

  - Input Data: name, contact, education, skills, experience, projects, job

  - Context: I am applying a job now, and you are a resume expert

  - Output Indicator: well-formatted, strictly one-page long latex code
  

- Do not expose API keys


## Example

![img.png](img.png)

Example generated resume:
[example.pdf](example.pdf)



## Run the Application

```bash
$ cd ResumeMaker
```

Create a virtual environment and activate it:

```bash
$ python3 -m venv env
$ source env/bin/activate
```

Install the modules necessary to run this application:
```bash
$ pip install -r requirements.txt
```

Run the application and open link in browser
```bash
$ streamlit run main.py
```


## Reference

[^1] https://platform.openai.com/docs/api-reference/completions

[^2] https://github.com/aslushnikov/latex-online#latex-online-
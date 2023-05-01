# ResumeMaker

## Introduction

This application can automatically generate a resume pdf document based on the user's profile and the description of the target job. It requires users to fill in their basic information, as well as a job description, and then a generated resume can be downloaded.

## Background

Nowadays, people often use Chat-GPT to help embellish their resumes. However, there are often problems such as incomplete description of necessary information, mismatch between resume and target position, and the generated text still needs to be typeset by yourself. Therefore, a one-stop platform to gather user information, adapt to the requirement of target positions and automatically generate formatted resume documents need to be created.






## How to run the application

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



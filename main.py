# This is a sample Python script.


import requests

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess

def print_hi(name):


    # Define the LaTeX code
    latex_code = r"""
    """

    # Define the URL of the API endpoint
    api_url = 'https://latexonline.cc/compile'

    # Define the request parameters
    params = {
        # 'content': latex_code,
        'format': 'pdf',
        'engine': 'pdflatex',
    }

    # Send the HTTP POST request to the API endpoint
    response = requests.post(api_url, data=params)

    # Save the PDF file to disk
    with open('document.pdf', 'wb') as f:
        f.write(response.content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    print('Hi')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

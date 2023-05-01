import requests
import urllib.parse

class PDFMaker:

    def __init__(self):
        self.url = 'https://latexonline.cc/compile'

    def run(self, latex_code):

        api_url = f'{self.url}?text={urllib.parse.quote(latex_code)}'

        response = requests.get(api_url)

        if response.status_code == 200:
            with open("output.pdf", "wb") as f:
                f.write(response.content)
            print("PDF downloaded successfully!")
            return True
        else:
            print(f"Failed to download PDF: {response.text}")
            return False

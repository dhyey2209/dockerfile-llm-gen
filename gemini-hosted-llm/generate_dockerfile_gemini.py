import google.generativeai as genai
import os

# Paste your API key here
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"

# Set up the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash') 

PROMPT = """
Generate ONLY an optimal Dockerfile for {language} following industry best practices. Do not provide any description
Include:
- A suitable base image
- Install all necessary dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)


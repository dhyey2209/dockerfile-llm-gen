import ollama

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
    response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': PROMPT.format(language=language)}])
    return response['message']['content']

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
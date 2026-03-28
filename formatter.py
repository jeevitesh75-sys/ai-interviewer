import re

def format_output(text):
    questions = []
    answers = []

    pattern = r"Q\d+:\s*(.*?)\s*Answer:\s*(.*?)(?=Q\d+:|$)"

    matches = re.findall(pattern, text, re.DOTALL)

    for q, a in matches:
        questions.append(q.strip())
        answers.append(a.strip() if a.strip() else "No answer provided")

    return questions, answers
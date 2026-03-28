def format_output(text):
    questions = []
    answers = []

    lines = text.split("\n")

    for line in lines:
        if line.strip().startswith("Q"):
            if "Answer:" in line:
                q, a = line.split("Answer:")
                questions.append(q.strip())
                answers.append(a.strip())
            else:
                questions.append(line.strip())

    return questions, answers
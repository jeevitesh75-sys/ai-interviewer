def format_output(text):
    questions = []
    answers = []

    parts = text.split("Q")

    for part in parts:
        part = part.strip()
        if part == "":
            continue

        if "Answer:" in part:
            q, a = part.split("Answer:", 1)

            q = "Q" + q.strip()
            a = a.strip()

            questions.append(q)
            answers.append(a)

    return questions, answers
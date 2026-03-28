def build_prompt(role, num_q, difficulty, one_line, one_word, coding):
    return f"""
Generate EXACTLY {num_q} interview questions for {role}.

Difficulty: {difficulty}

Distribution:
- {one_line}% One-line questions
- {one_word}% One-word questions
- {coding}% Coding questions

IMPORTANT:
- Coding questions MUST ask to write code
- EVERY question MUST have a COMPLETE answer
- DO NOT leave any answer empty

STRICT FORMAT:

Q1: Question here
Answer: Full answer here

Q2: Question here
Answer: Full answer here

Continue till Q{num_q}

DO NOT skip answers.
"""
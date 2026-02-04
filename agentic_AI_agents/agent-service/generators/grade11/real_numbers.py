import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Real Numbers
    Question Types:
    - identify (number classification)
    - solve (rational / irrational evaluation)
    - verify (true / false statements)
    - concept (theory-based)
    - application (simple reasoning)
    """

    qtype = random.choice(
        ["identify", "solve", "verify", "concept", "application"]
    )

    # ------------------------------------------------
    # IDENTIFY: Number classification
    # ------------------------------------------------
    if qtype == "identify":
        question = "Which of the following is an irrational number?"

        correct = random.choice(["√2", "√5", "π"])
        wrongs = ["3/4", "0.25", "7"]

    # ------------------------------------------------
    # SOLVE: Evaluate expression
    # ------------------------------------------------
    elif qtype == "solve":
        question = "Evaluate √49."

        correct = "7"
        wrongs = ["-7", "49", "√7"]

    # ------------------------------------------------
    # VERIFY: True / False
    # ------------------------------------------------
    elif qtype == "verify":
        question = "Is 0.333... a rational number?"

        correct = "True"
        wrongs = ["False", "Cannot be determined", "Irrational"]

    # ------------------------------------------------
    # CONCEPT: Theory-based question
    # ------------------------------------------------
    elif qtype == "concept":
        question = "Which of the following best describes a real number?"

        correct = "Any number that can be represented on the number line"
        wrongs = [
            "Only positive numbers",
            "Only integers",
            "Only rational numbers"
        ]

    # ------------------------------------------------
    # APPLICATION: Reasoning
    # ------------------------------------------------
    else:
        question = (
            "A square has a side length of 2 cm. "
            "Which type of number represents the length of its diagonal?"
        )

        correct = "Irrational number"
        wrongs = [
            "Natural number",
            "Whole number",
            "Rational number"
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Real Numbers",
        "needs_image": False
    }

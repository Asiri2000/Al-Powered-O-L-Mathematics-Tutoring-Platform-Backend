import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["basic", "power", "concept"])

    # ---- BASIC LOG ----
    if qtype == "basic":
        correct = "2"
        options, ans = shuffle_options(
            correct,
            ["1", "4", "10"]
        )
        question = "Find the value of log₁₀ 100."

    # ---- POWER LAW ----
    elif qtype == "power":
        correct = "3"
        options, ans = shuffle_options(
            correct,
            ["6", "1", "9"]
        )
        question = "Find the value of log₂ 8."

    # ---- CONCEPT ----
    else:
        correct = "Multiplication becomes addition"
        options, ans = shuffle_options(
            correct,
            [
                "Addition becomes multiplication",
                "Division becomes multiplication",
                "Powers are removed"
            ]
        )
        question = "According to logarithm laws, what happens when two numbers are multiplied?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Logarithms",
        "needs_image": False
    }

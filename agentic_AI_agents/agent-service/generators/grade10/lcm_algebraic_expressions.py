import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["simple", "with_coeff", "concept"])

    # ---- SIMPLE ----
    if qtype == "simple":
        correct = "2x²y"
        options, ans = shuffle_options(
            correct,
            ["x²y", "2xy", "x²y²"]
        )
        question = "Find the LCM of 2x²y and xy."

    # ---- WITH COEFFICIENTS ----
    elif qtype == "with_coeff":
        correct = "6x²y"
        options, ans = shuffle_options(
            correct,
            ["3x²y", "6xy", "2x²y"]
        )
        question = "Find the LCM of 3xy and 2x²y."

    # ---- CONCEPT ----
    else:
        correct = "Highest powers of all variables"
        options, ans = shuffle_options(
            correct,
            [
                "Lowest powers of variables",
                "Sum of powers",
                "Difference of powers"
            ]
        )
        question = "When finding the LCM of algebraic expressions, which powers of variables are taken?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Least Common Multiple of Algebraic Expressions",
        "needs_image": False
    }

import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["simplify", "multiply", "concept"])

    # ---- SIMPLIFY ----
    if qtype == "simplify":
        correct = "3/2"
        options, ans = shuffle_options(
            correct,
            ["2/3", "5/2", "3"]
        )
        question = "Simplify (3x / 4y) × (2y / x)."

    # ---- MULTIPLICATION ----
    elif qtype == "multiply":
        correct = "x/2"
        options, ans = shuffle_options(
            correct,
            ["2/x", "x", "1/2"]
        )
        question = "Simplify (x / 4) × (2 / 1)."

    # ---- CONCEPT ----
    else:
        correct = "Factorisation"
        options, ans = shuffle_options(
            correct,
            ["Expansion", "Substitution", "Elimination"]
        )
        question = "Which method is mainly used to simplify algebraic fractions?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Algebraic Fractions",
        "needs_image": False
    }

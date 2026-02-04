import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["notation", "elements", "concept"])

    # ---- SET NOTATION ----
    if qtype == "notation":
        correct = "{1, 2, 3}"
        options, ans = shuffle_options(
            correct,
            ["{1, 2}", "{2, 3, 4}", "{1, 3}"]
        )
        question = "Which of the following represents the set of natural numbers less than 4?"

    # ---- ELEMENT MEMBERSHIP ----
    elif qtype == "elements":
        correct = "3 ∈ A"
        options, ans = shuffle_options(
            correct,
            ["5 ∈ A", "6 ∈ A", "7 ∈ A"]
        )
        question = "If A = {1, 2, 3, 4}, which of the following is true?"

    # ---- CONCEPT ----
    else:
        correct = "A set with no elements"
        options, ans = shuffle_options(
            correct,
            ["A set with one element", "An infinite set", "A universal set"]
        )
        question = "What is an empty set?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Sets",
        "needs_image": False
    }

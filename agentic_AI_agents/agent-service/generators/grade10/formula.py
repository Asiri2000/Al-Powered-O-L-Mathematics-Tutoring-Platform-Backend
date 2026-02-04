import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["substitution", "rearrange", "concept"])

    # ---- SUBSTITUTION ----
    if qtype == "substitution":
        correct = "20"
        options, ans = shuffle_options(
            correct,
            ["10", "40", "5"]
        )
        question = "Using the formula A = l × w, find A when l = 5 and w = 4."

    # ---- REARRANGEMENT ----
    elif qtype == "rearrange":
        correct = "v = u + at"
        options, ans = shuffle_options(
            correct,
            ["u = v + at", "a = v + ut", "t = u + va"]
        )
        question = "Which is the correct formula for final velocity?"

    # ---- CONCEPT ----
    else:
        correct = "Rearrange the formula"
        options, ans = shuffle_options(
            correct,
            ["Change the numbers", "Guess the value", "Remove variables"]
        )
        question = "What should be done to find a required variable in a formula?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Formula",
        "needs_image": False
    }

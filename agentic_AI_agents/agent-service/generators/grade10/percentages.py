import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["percentage_of", "increase", "concept"])

    # ---- FIND PERCENTAGE ----
    if qtype == "percentage_of":
        correct = "20"
        options, ans = shuffle_options(
            correct,
            ["25", "15", "30"]
        )
        question = "Find 20% of 100."

    # ---- INCREASE ----
    elif qtype == "increase":
        correct = "120"
        options, ans = shuffle_options(
            correct,
            ["110", "130", "100"]
        )
        question = "Increase 100 by 20%."

    # ---- CONCEPT ----
    else:
        correct = "Divide by 100"
        options, ans = shuffle_options(
            correct,
            ["Multiply by 100", "Subtract from 100", "Add 100"]
        )
        question = "To convert a percentage into a fraction, what must be done?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Percentages",
        "needs_image": False
    }

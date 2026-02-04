import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["property", "angle", "concept"])

    # ---- PROPERTY ----
    if qtype == "property":
        correct = "Opposite sides are equal"
        options, ans = shuffle_options(
            correct,
            [
                "All sides are unequal",
                "Adjacent sides are equal",
                "Only one pair of sides equal"
            ]
        )
        question = "Which of the following is a property of a parallelogram?"

    # ---- ANGLE ----
    elif qtype == "angle":
        correct = "60°"
        options, ans = shuffle_options(
            correct,
            ["120°", "30°", "90°"]
        )
        question = "If one angle of a parallelogram is 120°, find the adjacent angle."

    # ---- CONCEPT ----
    else:
        correct = "Both pairs of opposite sides are parallel"
        options, ans = shuffle_options(
            correct,
            [
                "All sides are equal",
                "Diagonals are perpendicular",
                "Only one pair of sides parallel"
            ]
        )
        question = "Which condition is used to identify a parallelogram?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Parallelograms",
        "needs_image": True
    }

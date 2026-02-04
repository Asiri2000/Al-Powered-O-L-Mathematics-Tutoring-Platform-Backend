import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["tool", "perpendicular", "concept"])

    # ---- TOOL ----
    if qtype == "tool":
        correct = "Compass"
        options, ans = shuffle_options(
            correct,
            ["Protractor", "Ruler only", "Divider"]
        )
        question = "Which instrument is used to draw arcs in geometric constructions?"

    # ---- PERPENDICULAR ----
    elif qtype == "perpendicular":
        correct = "A right angle"
        options, ans = shuffle_options(
            correct,
            ["An obtuse angle", "An acute angle", "A straight angle"]
        )
        question = "What type of angle is formed when constructing a perpendicular line?"

    # ---- CONCEPT ----
    else:
        correct = "Accuracy"
        options, ans = shuffle_options(
            correct,
            [
                "Speed",
                "Guessing",
                "Measurement by eye"
            ]
        )
        question = "Why is accuracy important in geometric constructions?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Constructions",
        "needs_image": True
    }

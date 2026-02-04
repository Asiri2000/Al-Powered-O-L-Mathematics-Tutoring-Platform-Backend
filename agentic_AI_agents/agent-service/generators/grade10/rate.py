import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["speed", "unit", "concept"])

    # ---- SPEED ----
    if qtype == "speed":
        correct = "60 km/h"
        options, ans = shuffle_options(
            correct,
            ["30 km/h", "120 km/h", "90 km/h"]
        )
        question = "A car travels 120 km in 2 hours. Find its speed."

    # ---- UNIT ----
    elif qtype == "unit":
        correct = "km/h"
        options, ans = shuffle_options(
            correct,
            ["km", "h", "m²"]
        )
        question = "What is the unit of speed?"

    # ---- CONCEPT ----
    else:
        correct = "Distance ÷ Time"
        options, ans = shuffle_options(
            correct,
            ["Time ÷ Distance", "Distance × Time", "Speed × Time"]
        )
        question = "How is speed calculated?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Rate",
        "needs_image": False
    }

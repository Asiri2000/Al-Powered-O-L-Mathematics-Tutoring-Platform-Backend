import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["coordinates", "slope", "concept"])

    # ---- COORDINATES ----
    if qtype == "coordinates":
        correct = "(2,4)"
        options, ans = shuffle_options(
            correct,
            ["(4,2)", "(2,2)", "(1,4)"]
        )
        question = "State the coordinates of the point where x = 2 on the graph y = 2x."

    # ---- SLOPE ----
    elif qtype == "slope":
        correct = "2"
        options, ans = shuffle_options(
            correct,
            ["1", "4", "0"]
        )
        question = "What is the gradient of the straight line y = 2x?"

    # ---- CONCEPT ----
    else:
        correct = "y-intercept"
        options, ans = shuffle_options(
            correct,
            ["Gradient", "Slope", "Origin"]
        )
        question = "What is the point where a graph cuts the y-axis called?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Graphs",
        "needs_image": True
    }

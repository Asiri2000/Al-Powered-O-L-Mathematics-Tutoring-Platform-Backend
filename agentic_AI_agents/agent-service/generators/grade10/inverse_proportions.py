import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    x1 = random.randint(2, 6)
    y1 = random.randint(12, 24)
    x2 = random.randint(3, 8)

    y2 = (x1 * y1) // x2

    correct = str(y2)

    options, ans = shuffle_options(
        correct,
        [str(y1), str(x2 * y1), str(y1 // x2)]
    )

    return {
        "question": f"If x and y are inversely proportional, and x = {x1} when y = {y1}, find y when x = {x2}.",
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Inverse Proportions",
        "needs_image": False
    }

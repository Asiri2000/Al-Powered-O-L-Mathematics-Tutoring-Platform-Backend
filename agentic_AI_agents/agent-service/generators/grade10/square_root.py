import random
import math
from generators.utils.shuffle import shuffle_options

def generate(difficulty: int = 3):
    while True:
        number = random.randint(10, 99)
        if int(math.sqrt(number)) ** 2 != number:
            break

    correct_value = round(math.sqrt(number), 2)
    correct = f"{correct_value:.2f}"

    wrongs = set()
    while len(wrongs) < 3:
        variation = round(correct_value + random.uniform(-0.8, 0.8), 2)
        if variation > 0 and f"{variation:.2f}" != correct:
            wrongs.add(f"{variation:.2f}")

    options, answer = shuffle_options(correct, list(wrongs))

    return {
        "question": f"Find the square root of {number}, correct to two decimal places.",
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Square Root",
        "needs_image": False
    }

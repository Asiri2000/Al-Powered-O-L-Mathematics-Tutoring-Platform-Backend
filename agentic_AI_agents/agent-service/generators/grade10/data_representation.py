import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    values = [random.randint(5, 20) for _ in range(4)]
    correct = str(max(values))

    options, ans = shuffle_options(
        correct,
        [str(min(values)), str(sum(values)), str(values[0])]
    )

    return {
        "question": f"The number of students in four classes are {values}. Which class has the highest number of students?",
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Data Representation",
        "needs_image": True
    }

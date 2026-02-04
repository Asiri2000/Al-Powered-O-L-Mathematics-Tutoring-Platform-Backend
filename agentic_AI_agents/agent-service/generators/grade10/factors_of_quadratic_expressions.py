import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    a = random.randint(1, 4)
    b = random.randint(1, 5)

    correct = f"(x + {a})(x + {b})"

    options, ans = shuffle_options(
        correct,
        [
            f"(x + {a+b})(x)",
            f"(x + {a})(x - {b})",
            f"x² + {a+b}x"
        ]
    )

    return {
        "question": f"Factorize x² + {a+b}x + {a*b}.",
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Factors of Quadratic Expressions",
        "needs_image": False
    }

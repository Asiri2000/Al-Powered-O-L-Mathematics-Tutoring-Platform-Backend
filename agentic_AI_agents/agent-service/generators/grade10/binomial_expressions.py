import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice([
        "expand",
        "identify_terms",
        "coefficient",
        "evaluate"
    ])

    a = random.randint(1, 5)
    b = random.randint(1, 5)
    x = "x"

    # -------- EXPANSION --------
    if qtype == "expand":
        correct = f"{x}² + {2*b}{x} + {b*b}"
        options, ans = shuffle_options(
            correct,
            [
                f"{x}² + {b}{x} + {b}",
                f"{x}² + {b*b}",
                f"{2*b}{x} + {b*b}"
            ]
        )
        question = f"Expand ({x} + {b})²."

    # -------- IDENTIFY TERMS --------
    elif qtype == "identify_terms":
        correct = "3"
        options, ans = shuffle_options(correct, ["2", "1", "4"])
        question = "How many terms are there in the expression x² + 3x + 2?"

    # -------- COEFFICIENT --------
    elif qtype == "coefficient":
        correct = "3"
        options, ans = shuffle_options(correct, ["2", "1", "4"])
        question = "Find the coefficient of x in the expression 2x² + 3x + 5."

    # -------- EVALUATION --------
    else:
        correct = str((a + b) ** 2)
        options, ans = shuffle_options(
            correct,
            [str(a*a + b*b), str(a + b), str(2*a*b)]
        )
        question = f"Find the value of (x + {b})² when x = {a}."

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Binomial Expressions",
        "needs_image": False
    }

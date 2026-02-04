import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Indices and Logarithms

    Question Types:
    - evaluate_indices
    - simplify_indices
    - logarithm_value
    - logarithm_law
    - concept
    """

    qtype = random.choice(
        [
            "evaluate_indices",
            "simplify_indices",
            "logarithm_value",
            "logarithm_law",
            "concept",
        ]
    )

    # ------------------------------------------------
    # EVALUATE INDICES
    # ------------------------------------------------
    if qtype == "evaluate_indices":
        base = random.randint(2, 4)
        a = random.randint(2, 4)
        b = random.randint(1, 3)

        question = f"Evaluate {base}^{a} × {base}^{b}."

        correct = str(base ** (a + b))
        wrongs = [
            str(base ** a + base ** b),
            str(base ** (a * b)),
            str(base ** (a - b) if a > b else base ** (b - a)),
        ]

    # ------------------------------------------------
    # SIMPLIFY INDICES
    # ------------------------------------------------
    elif qtype == "simplify_indices":
        base = random.randint(2, 5)
        a = random.randint(3, 6)
        b = random.randint(1, 3)

        question = f"Simplify {base}^{a} ÷ {base}^{b}."

        correct = f"{base}^{a - b}"
        wrongs = [
            f"{base}^{a + b}",
            f"{base}^{a * b}",
            f"{base}^{b - a}",
        ]

    # ------------------------------------------------
    # LOGARITHM VALUE
    # ------------------------------------------------
    elif qtype == "logarithm_value":
        question = "Find the value of log₁₀1."

        correct = "0"
        wrongs = ["1", "10", "Undefined"]

    # ------------------------------------------------
    # LOGARITHM LAW
    # ------------------------------------------------
    elif qtype == "logarithm_law":
        question = "Which of the following is a correct logarithmic law?"

        correct = "log(ab) = log a + log b"
        wrongs = [
            "log(a + b) = log a + log b",
            "log(a − b) = log a − log b",
            "log(ab) = log a × log b",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = "What is the meaning of a negative index?"

        correct = "It represents the reciprocal of the base"
        wrongs = [
            "It makes the value zero",
            "It removes the base",
            "It makes the number negative",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Indices and Logarithms",
        "needs_image": False
    }

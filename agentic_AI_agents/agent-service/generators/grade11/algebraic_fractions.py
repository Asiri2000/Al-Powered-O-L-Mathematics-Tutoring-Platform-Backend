import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Algebraic Fractions

    Question Types:
    - simplify
    - identify_restriction
    - evaluate
    - concept
    - application
    """

    qtype = random.choice(
        [
            "simplify",
            "identify_restriction",
            "evaluate",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # SIMPLIFY ALGEBRAIC FRACTION
    # ------------------------------------------------
    if qtype == "simplify":
        question = "Simplify (x² − 9) / (x + 3)."

        correct = "x − 3"
        wrongs = [
            "x + 3",
            "x² − 3",
            "x² + 3",
        ]

    # ------------------------------------------------
    # IDENTIFY RESTRICTION
    # ------------------------------------------------
    elif qtype == "identify_restriction":
        question = "For what value of x is the expression 1 / (x − 4) undefined?"

        correct = "x = 4"
        wrongs = [
            "x = −4",
            "x = 0",
            "x = 1",
        ]

    # ------------------------------------------------
    # EVALUATE FRACTION
    # ------------------------------------------------
    elif qtype == "evaluate":
        x_val = random.randint(1, 5)

        question = f"Evaluate (x + 2) / (x + 1) when x = {x_val}."

        correct_value = round((x_val + 2) / (x_val + 1), 2)
        correct = str(correct_value)

        wrongs = [
            str(round((x_val + 1) / (x_val + 2), 2)),
            str(round((x_val + 2) / x_val, 2)),
            str(round(x_val / (x_val + 1), 2)),
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = "Why are restrictions placed on the variable in algebraic fractions?"

        correct = "To avoid division by zero"
        wrongs = [
            "To simplify the expression",
            "To remove variables",
            "To reduce coefficients",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "The expression (x − 5) / (x − 2) represents the speed of a vehicle. "
            "Why must x ≠ 2?"
        )

        correct = "Because the denominator becomes zero"
        wrongs = [
            "Because the value becomes negative",
            "Because the numerator becomes zero",
            "Because the expression simplifies",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Algebraic Fractions",
        "needs_image": False
    }

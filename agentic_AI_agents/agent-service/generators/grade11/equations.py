import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Equations

    Question Types:
    - solve_linear
    - solve_with_brackets
    - verify_solution
    - identify_solution
    - concept
    """

    qtype = random.choice(
        [
            "solve_linear",
            "solve_with_brackets",
            "verify_solution",
            "identify_solution",
            "concept",
        ]
    )

    # ------------------------------------------------
    # SOLVE SIMPLE LINEAR EQUATION
    # ------------------------------------------------
    if qtype == "solve_linear":
        a = random.randint(1, 4)
        x = random.randint(1, 6)
        b = random.randint(0, 6)

        c = a * x + b

        question = f"Solve the equation {a}x + {b} = {c}."

        correct = str(x)
        wrongs = [
            str(x + 1),
            str(x - 1 if x > 1 else x + 2),
            str(c),
        ]

    # ------------------------------------------------
    # SOLVE EQUATION WITH BRACKETS
    # ------------------------------------------------
    elif qtype == "solve_with_brackets":
        x = random.randint(1, 5)
        a = random.randint(2, 4)
        b = random.randint(1, 4)

        question = f"Solve the equation {a}(x + {b}) = {a * (x + b)}."

        correct = str(x)
        wrongs = [
            str(x + b),
            str(a * x),
            str(x - b),
        ]

    # ------------------------------------------------
    # VERIFY A SOLUTION
    # ------------------------------------------------
    elif qtype == "verify_solution":
        a = random.randint(1, 3)
        x = random.randint(1, 5)
        b = random.randint(1, 4)
        c = a * x + b

        test_value = random.choice([x, x + 1])

        question = (
            f"Is x = {test_value} a solution of the equation "
            f"{a}x + {b} = {c}?"
        )

        correct = "True" if test_value == x else "False"
        wrongs = ["Cannot be determined", "0", "Both"]

    # ------------------------------------------------
    # IDENTIFY THE SOLUTION
    # ------------------------------------------------
    elif qtype == "identify_solution":
        x = random.randint(1, 6)
        a = random.randint(1, 4)
        b = random.randint(1, 6)
        c = a * x + b

        question = (
            f"Which of the following is the solution of "
            f"{a}x + {b} = {c}?"
        )

        correct = str(x)
        wrongs = [
            str(x + 2),
            str(x - 1 if x > 1 else x + 3),
            str(b),
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = "What does it mean to solve an equation?"

        correct = "To find the value that makes both sides equal"
        wrongs = [
            "To simplify only the left-hand side",
            "To remove all variables",
            "To rearrange the equation",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Equations",
        "needs_image": False
    }

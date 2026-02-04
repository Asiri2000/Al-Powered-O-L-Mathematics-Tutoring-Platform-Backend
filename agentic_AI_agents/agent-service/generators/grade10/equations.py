import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty=3):
    """
    Generates different types of Grade 10 equation questions:
    - Solve linear equations
    - Verify solutions
    - Identify correct solution
    - Conceptual understanding
    - Simple word problems
    """

    qtype = random.choice(
        ["solve", "verify", "identify", "concept", "word_problem"]
    )

    # -------------------------
    # SOLVE LINEAR EQUATION
    # -------------------------
    if qtype == "solve":
        a = random.randint(1, difficulty + 2)
        x = random.randint(1, 5)
        b = random.randint(0, 5)

        c = a * x + b
        question = f"Solve the equation {a}x + {b} = {c}."

        correct = str(x)
        wrongs = [
            str(x + 1),
            str(x - 1 if x > 1 else x + 2),
            str(x + 2),
        ]

        options, ans = shuffle_options(correct, wrongs)

    # -------------------------
    # VERIFY A SOLUTION
    # -------------------------
    elif qtype == "verify":
        a = random.randint(1, difficulty + 2)
        x = random.randint(1, 5)
        b = random.randint(0, 5)
        c = a * x + b

        test_value = random.choice([x, x + 1])

        question = (
            f"Is x = {test_value} a solution of the equation "
            f"{a}x + {b} = {c}?"
        )

        correct = "True" if test_value == x else "False"
        options, ans = shuffle_options(
            correct,
            ["False", "Cannot be determined", "0"]
        )

    # -------------------------
    # IDENTIFY CORRECT SOLUTION
    # -------------------------
    elif qtype == "identify":
        a = random.randint(1, difficulty + 2)
        x = random.randint(1, 5)
        b = random.randint(0, 5)
        c = a * x + b

        question = (
            f"Which of the following is the solution of "
            f"{a}x + {b} = {c}?"
        )

        correct = str(x)
        wrongs = [
            str(x + 1),
            str(x - 1 if x > 1 else x + 2),
            str(c),
        ]

        options, ans = shuffle_options(correct, wrongs)

    # -------------------------
    # CONCEPTUAL QUESTION
    # -------------------------
    elif qtype == "concept":
        question = "What does it mean to solve an equation?"

        correct = "To find the value that makes both sides equal"
        wrongs = [
            "To simplify only the left-hand side",
            "To remove all variables",
            "To change the equation"
        ]

        options, ans = shuffle_options(correct, wrongs)

    # -------------------------
    # WORD PROBLEM
    # -------------------------
    else:
        x = random.randint(2, 6)
        total = 3 * x + 4

        question = (
            f"A number is multiplied by 3 and then 4 is added to get {total}. "
            f"What is the number?"
        )

        correct = str(x)
        wrongs = [
            str(x + 1),
            str(x - 1),
            str(total),
        ]

        options, ans = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Equations",
        "needs_image": False
    }

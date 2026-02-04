import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Inequalities

    Question Types:
    - solve_simple_inequality
    - identify_solution
    - sign_change_rule
    - number_line_concept
    - application
    """

    qtype = random.choice(
        [
            "solve_simple_inequality",
            "identify_solution",
            "sign_change_rule",
            "number_line_concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # SOLVE SIMPLE INEQUALITY
    # ------------------------------------------------
    if qtype == "solve_simple_inequality":
        x = random.randint(2, 6)
        a = random.randint(1, 4)

        question = f"Solve the inequality {a}x < {a * x}."

        correct = f"x < {x}"
        wrongs = [
            f"x > {x}",
            f"x = {x}",
            f"x ≤ {x}",
        ]

    # ------------------------------------------------
    # IDENTIFY SOLUTION
    # ------------------------------------------------
    elif qtype == "identify_solution":
        question = "Which of the following is a solution of x > 3?"

        correct = "5"
        wrongs = [
            "3",
            "−1",
            "0",
        ]

    # ------------------------------------------------
    # SIGN CHANGE RULE
    # ------------------------------------------------
    elif qtype == "sign_change_rule":
        question = (
            "What happens to an inequality sign when both sides are multiplied "
            "by a negative number?"
        )

        correct = "The inequality sign is reversed"
        wrongs = [
            "The inequality sign remains the same",
            "The inequality disappears",
            "The inequality becomes an equation",
        ]

    # ------------------------------------------------
    # NUMBER LINE CONCEPT
    # ------------------------------------------------
    elif qtype == "number_line_concept":
        question = (
            "Which symbol represents all real numbers greater than or equal to 4?"
        )

        correct = "x ≥ 4"
        wrongs = [
            "x > 4",
            "x ≤ 4",
            "x < 4",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "A student must score more than 50 marks to pass an exam. "
            "Which inequality represents this situation?"
        )

        correct = "Marks > 50"
        wrongs = [
            "Marks ≥ 50",
            "Marks < 50",
            "Marks ≤ 50",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Inequalities",
        "needs_image": False
    }

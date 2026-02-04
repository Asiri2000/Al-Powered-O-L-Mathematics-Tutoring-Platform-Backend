import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Graphs

    Question Types:
    - identify_graph
    - read_coordinate
    - slope_concept
    - equation_of_line
    - interpretation
    """

    qtype = random.choice(
        [
            "identify_graph",
            "read_coordinate",
            "slope_concept",
            "equation_of_line",
            "interpretation",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY GRAPH TYPE
    # ------------------------------------------------
    if qtype == "identify_graph":
        question = "Which of the following represents a straight-line graph?"

        correct = "y = 2x + 3"
        wrongs = [
            "y = x²",
            "y = 1/x",
            "x² + y² = 25",
        ]

    # ------------------------------------------------
    # READ COORDINATE
    # ------------------------------------------------
    elif qtype == "read_coordinate":
        x = random.randint(1, 5)
        y = random.randint(2, 6)

        question = (
            f"If a point on a graph has x-coordinate {x} and y-coordinate {y}, "
            f"how is the point written?"
        )

        correct = f"({x}, {y})"
        wrongs = [
            f"({y}, {x})",
            f"[{x}, {y}]",
            f"{x}, {y}",
        ]

    # ------------------------------------------------
    # SLOPE / GRADIENT CONCEPT
    # ------------------------------------------------
    elif qtype == "slope_concept":
        question = "What does the gradient (slope) of a straight line represent?"

        correct = "The rate of change of y with respect to x"
        wrongs = [
            "The y-intercept",
            "The length of the line",
            "The area under the graph",
        ]

    # ------------------------------------------------
    # EQUATION OF A LINE
    # ------------------------------------------------
    elif qtype == "equation_of_line":
        m = random.choice([1, 2, 3])
        c = random.choice([1, 2, 4])

        question = (
            f"What is the equation of a straight line with gradient {m} "
            f"and y-intercept {c}?"
        )

        correct = f"y = {m}x + {c}"
        wrongs = [
            f"y = {c}x + {m}",
            f"x = {m}y + {c}",
            f"y = {m + c}x",
        ]

    # ------------------------------------------------
    # GRAPH INTERPRETATION
    # ------------------------------------------------
    else:
        question = (
            "If a straight-line graph slopes upwards from left to right, "
            "what can be said about its gradient?"
        )

        correct = "The gradient is positive"
        wrongs = [
            "The gradient is negative",
            "The gradient is zero",
            "The gradient is undefined",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Graphs",
        "needs_image": False
    }

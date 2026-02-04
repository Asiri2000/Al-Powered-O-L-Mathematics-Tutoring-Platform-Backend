import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Cyclic Quadrilaterals

    Question Types:
    - identify_property
    - opposite_angles
    - true_false
    - concept
    - application
    """

    qtype = random.choice(
        [
            "identify_property",
            "opposite_angles",
            "true_false",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY PROPERTY
    # ------------------------------------------------
    if qtype == "identify_property":
        question = (
            "Which of the following is a property of a cyclic quadrilateral?"
        )

        correct = "Opposite angles are supplementary"
        wrongs = [
            "All sides are equal",
            "Diagonals bisect at right angles",
            "All angles are equal",
        ]

    # ------------------------------------------------
    # OPPOSITE ANGLES
    # ------------------------------------------------
    elif qtype == "opposite_angles":
        angle = random.choice([70, 80, 100, 110])

        question = (
            f"In a cyclic quadrilateral, if one angle is {angle}°, "
            f"what is the measure of the opposite angle?"
        )

        correct = f"{180 - angle}°"
        wrongs = [
            f"{angle}°",
            f"{angle / 2}°",
            f"{angle + 20}°",
        ]

    # ------------------------------------------------
    # TRUE / FALSE
    # ------------------------------------------------
    elif qtype == "true_false":
        question = (
            "The sum of opposite angles of a cyclic quadrilateral is 180°."
        )

        correct = "True"
        wrongs = [
            "False",
            "Only for squares",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = (
            "When is a quadrilateral said to be cyclic?"
        )

        correct = "When all its vertices lie on a circle"
        wrongs = [
            "When all sides are equal",
            "When diagonals are equal",
            "When opposite sides are parallel",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "Why are opposite angles of a cyclic quadrilateral supplementary?"
        )

        correct = "They subtend the same arc of the circle"
        wrongs = [
            "They are vertically opposite angles",
            "They are alternate interior angles",
            "They are corresponding angles",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Cyclic Quadrilaterals",
        "needs_image": False
    }

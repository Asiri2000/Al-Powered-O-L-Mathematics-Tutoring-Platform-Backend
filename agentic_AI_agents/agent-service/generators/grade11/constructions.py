import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Constructions
    Mathematical & conceptual questions
    """

    qtype = random.choice(
        ["identify", "true_false", "application", "concept"]
    )

    # ------------------------------------------------
    # IDENTIFY CONSTRUCTION
    # ------------------------------------------------
    if qtype == "identify":
        question = (
            "Which instrument is essential to construct a perpendicular bisector?"
        )

        correct = "Compass"
        wrongs = [
            "Protractor only",
            "Ruler only",
            "Set square",
        ]

    # ------------------------------------------------
    # TRUE / FALSE
    # ------------------------------------------------
    elif qtype == "true_false":
        question = (
            "A perpendicular bisector divides a line segment into two equal parts."
        )

        correct = "True"
        wrongs = [
            "False",
            "Only for horizontal lines",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # APPLICATION
    # ------------------------------------------------
    elif qtype == "application":
        question = (
            "Which construction is used to locate a point equidistant "
            "from two given points?"
        )

        correct = "Perpendicular bisector"
        wrongs = [
            "Angle bisector",
            "Median",
            "Altitude",
        ]

    # ------------------------------------------------
    # CONCEPT
    # ------------------------------------------------
    else:
        question = (
            "Why is a compass used in geometric constructions?"
        )

        correct = "To draw arcs with equal radius"
        wrongs = [
            "To measure angles",
            "To draw straight lines",
            "To calculate area",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Constructions",
        "needs_image": False
    }

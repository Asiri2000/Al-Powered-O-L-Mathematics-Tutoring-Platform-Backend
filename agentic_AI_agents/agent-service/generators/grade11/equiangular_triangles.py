import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Equiangular Triangles

    Question Types:
    - identify_property
    - angle_measure
    - true_false
    - concept
    - application
    """

    qtype = random.choice(
        [
            "identify_property",
            "angle_measure",
            "true_false",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY PROPERTY
    # ------------------------------------------------
    if qtype == "identify_property":
        question = "Which of the following is true for equiangular triangles?"

        correct = "All corresponding angles are equal"
        wrongs = [
            "All sides are equal",
            "They have equal areas only",
            "Only one angle is equal",
        ]

    # ------------------------------------------------
    # ANGLE MEASURE
    # ------------------------------------------------
    elif qtype == "angle_measure":
        question = (
            "If a triangle is equiangular, what is the measure of each angle?"
        )

        correct = "60°"
        wrongs = [
            "45°",
            "90°",
            "30°",
        ]

    # ------------------------------------------------
    # TRUE / FALSE
    # ------------------------------------------------
    elif qtype == "true_false":
        question = (
            "All equilateral triangles are equiangular."
        )

        correct = "True"
        wrongs = [
            "False",
            "Only some are equiangular",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = (
            "If two triangles are equiangular, what can be said about their sides?"
        )

        correct = "Their corresponding sides are proportional"
        wrongs = [
            "Their sides are equal",
            "Their areas are equal",
            "Their sides are parallel",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "Two triangles are equiangular with sides in the ratio 2 : 3. "
            "What is the ratio of their areas?"
        )

        correct = "4 : 9"
        wrongs = [
            "2 : 3",
            "3 : 2",
            "6 : 9",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Equiangular Triangles",
        "needs_image": False
    }

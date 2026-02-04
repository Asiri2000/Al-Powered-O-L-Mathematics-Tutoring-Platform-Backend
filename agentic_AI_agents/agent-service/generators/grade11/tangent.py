import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Tangent to a Circle

    Question Types:
    - tangent_radius_angle
    - equal_tangents
    - find_angle
    - true_false
    - application
    """

    qtype = random.choice(
        [
            "tangent_radius_angle",
            "equal_tangents",
            "find_angle",
            "true_false",
            "application",
        ]
    )

    # ------------------------------------------------
    # TANGENT–RADIUS ANGLE PROPERTY
    # ------------------------------------------------
    if qtype == "tangent_radius_angle":
        question = (
            "The angle between a tangent and the radius at the point of contact is:"
        )

        correct = "90°"
        wrongs = [
            "45°",
            "60°",
            "180°",
        ]

    # ------------------------------------------------
    # EQUAL TANGENTS THEOREM
    # ------------------------------------------------
    elif qtype == "equal_tangents":
        question = (
            "Two tangents are drawn from an external point to a circle. "
            "Which of the following is true?"
        )

        correct = "The lengths of the tangents are equal"
        wrongs = [
            "The angles are unequal",
            "The tangents intersect the circle",
            "The radii are unequal",
        ]

    # ------------------------------------------------
    # FIND ANGLE USING TANGENT PROPERTY
    # ------------------------------------------------
    elif qtype == "find_angle":
        angle = random.choice([30, 40, 50, 60])

        question = (
            f"If a tangent touches a circle at point P and OP is the radius, "
            f"find the angle between OP and the tangent if another angle "
            f"at P is {angle}°."
        )

        correct = "90°"
        wrongs = [
            f"{angle}°",
            f"{180 - angle}°",
            f"{angle / 2}°",
        ]

    # ------------------------------------------------
    # TRUE / FALSE (MATHEMATICAL)
    # ------------------------------------------------
    elif qtype == "true_false":
        question = (
            "The tangents drawn from an external point to a circle "
            "are always equal in length."
        )

        correct = "True"
        wrongs = [
            "False",
            "Only for large circles",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # APPLICATION / CALCULATION
    # ------------------------------------------------
    else:
        radius = random.choice([5, 7, 10])

        question = (
            f"A tangent is drawn to a circle of radius {radius} cm. "
            f"What is the distance between the center of the circle "
            f"and the point of contact?"
        )

        correct = f"{radius} cm"
        wrongs = [
            f"{radius * 2} cm",
            f"{radius / 2} cm",
            f"{radius + 2} cm",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Tangent",
        "needs_image": False
    }

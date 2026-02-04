import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice([
        "angle_at_center",
        "angle_in_semicircle",
        "same_segment",
        "concept"
    ])

    # ---- ANGLE AT CENTER ----
    if qtype == "angle_at_center":
        correct = "Twice the angle at the circumference"
        options, ans = shuffle_options(
            correct,
            [
                "Equal to the angle",
                "Half the angle",
                "Three times the angle"
            ]
        )
        question = "How is the angle at the centre related to the angle at the circumference standing on the same arc?"

    # ---- SEMICIRCLE ----
    elif qtype == "angle_in_semicircle":
        correct = "90°"
        options, ans = shuffle_options(
            correct,
            ["60°", "180°", "45°"]
        )
        question = "What is the angle in a semicircle?"

    # ---- SAME SEGMENT ----
    elif qtype == "same_segment":
        correct = "They are equal"
        options, ans = shuffle_options(
            correct,
            [
                "They are supplementary",
                "They are complementary",
                "They add to 180°"
            ]
        )
        question = "What can be said about angles in the same segment of a circle?"

    # ---- CONCEPT ----
    else:
        correct = "A line joining the centre to the circle"
        options, ans = shuffle_options(
            correct,
            [
                "A chord",
                "A tangent",
                "A diameter only"
            ]
        )
        question = "What is the radius of a circle?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Angles in a Circle",
        "needs_image": True
    }

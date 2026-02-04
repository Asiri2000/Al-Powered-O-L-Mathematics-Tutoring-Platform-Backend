import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Trigonometry

    Question Types:
    - basic_ratio
    - exact_value
    - identity
    - height_distance
    - concept
    """

    qtype = random.choice(
        [
            "basic_ratio",
            "exact_value",
            "identity",
            "height_distance",
            "concept",
        ]
    )

    # ------------------------------------------------
    # BASIC TRIGONOMETRIC RATIO
    # ------------------------------------------------
    if qtype == "basic_ratio":
        question = (
            "In a right-angled triangle, which trigonometric ratio is "
            "defined as opposite / hypotenuse?"
        )

        correct = "Sine"
        wrongs = [
            "Cosine",
            "Tangent",
            "Secant",
        ]

    # ------------------------------------------------
    # EXACT VALUE
    # ------------------------------------------------
    elif qtype == "exact_value":
        angle = random.choice([30, 45, 60])
        values = {
            30: "1/2",
            45: "1/√2",
            60: "√3/2",
        }

        question = f"Find the exact value of sin {angle}°."

        correct = values[angle]
        wrongs = [
            "1",
            "0",
            "√3",
        ]

    # ------------------------------------------------
    # TRIGONOMETRIC IDENTITY
    # ------------------------------------------------
    elif qtype == "identity":
        question = "Which of the following is a correct trigonometric identity?"

        correct = "sin²θ + cos²θ = 1"
        wrongs = [
            "sinθ + cosθ = 1",
            "tanθ = sinθ + cosθ",
            "sin²θ − cos²θ = 1",
        ]

    # ------------------------------------------------
    # HEIGHT AND DISTANCE
    # ------------------------------------------------
    elif qtype == "height_distance":
        question = (
            "A flagstaff stands on top of a building. "
            "The angle of elevation of the top of the flagstaff "
            "from the ground is 45°. What can be said about "
            "the height and the distance from the building?"
        )

        correct = "Height equals distance"
        wrongs = [
            "Height is double the distance",
            "Distance is double the height",
            "They are unrelated",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = "Which angle is used in trigonometric ratios?"

        correct = "Angle in a right-angled triangle"
        wrongs = [
            "Any angle in a triangle",
            "Only obtuse angles",
            "Only acute angles",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Trigonometry",
        "needs_image": False
    }

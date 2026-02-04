import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Volume of Solids

    Question Types:
    - identify_formula
    - calculate_volume
    - true_false
    - concept
    - application
    """

    qtype = random.choice(
        [
            "identify_formula",
            "calculate_volume",
            "true_false",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY FORMULA
    # ------------------------------------------------
    if qtype == "identify_formula":
        question = "Which formula is used to find the volume of a sphere?"

        correct = "4/3 πr³"
        wrongs = [
            "πr²",
            "2πr³",
            "4πr²",
        ]

    # ------------------------------------------------
    # CALCULATE VOLUME
    # ------------------------------------------------
    elif qtype == "calculate_volume":
        r = random.randint(2, 5)

        question = (
            f"Find the volume of a sphere of radius {r} cm. "
            f"(Take π = 22/7)"
        )

        correct_value = round((4 / 3) * (22 / 7) * (r ** 3), 2)
        correct = f"{correct_value} cm³"

        wrongs = [
            f"{round((22 / 7) * r * r, 2)} cm³",
            f"{round((22 / 7) * r * r * r, 2)} cm³",
            f"{round(4 * (22 / 7) * r * r, 2)} cm³",
        ]

    # ------------------------------------------------
    # TRUE / FALSE
    # ------------------------------------------------
    elif qtype == "true_false":
        question = "The volume of a cylinder is given by πr²h."

        correct = "True"
        wrongs = ["False", "Only for cones", "Cannot be determined"]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = "Which of the following changes the volume of a cube?"

        correct = "Length of its side"
        wrongs = [
            "Surface texture",
            "Color of the cube",
            "Orientation of the cube",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        r = random.randint(2, 4)
        h = random.randint(5, 10)

        question = (
            f"A cylindrical water tank has radius {r} m and height {h} m. "
            f"How much water can it hold? (Use π = 22/7)"
        )

        correct_value = round((22 / 7) * r * r * h, 2)
        correct = f"{correct_value} m³"

        wrongs = [
            f"{round((22 / 7) * r * h, 2)} m³",
            f"{round(2 * (22 / 7) * r * h, 2)} m³",
            f"{round((22 / 7) * r * r, 2)} m³",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Volume of Solids",
        "needs_image": False
    }

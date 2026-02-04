import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Surface Area of Solids

    Question Types:
    - identify_formula
    - calculate_surface_area
    - true_false
    - concept
    - application
    """

    qtype = random.choice(
        [
            "identify_formula",
            "calculate_surface_area",
            "true_false",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY FORMULA
    # ------------------------------------------------
    if qtype == "identify_formula":
        question = "Which formula is used to find the curved surface area of a cylinder?"

        correct = "2πrh"
        wrongs = [
            "πr²",
            "2πr(r + h)",
            "πr²h",
        ]

    # ------------------------------------------------
    # CALCULATE SURFACE AREA
    # ------------------------------------------------
    elif qtype == "calculate_surface_area":
        r = random.randint(2, 5)
        h = random.randint(4, 10)

        question = (
            f"Find the curved surface area of a cylinder of radius {r} cm "
            f"and height {h} cm. (Take π = 22/7)"
        )

        correct_value = round(2 * (22 / 7) * r * h, 2)
        correct = f"{correct_value} cm²"

        wrongs = [
            f"{round((22 / 7) * r * r, 2)} cm²",
            f"{round((22 / 7) * r * r * h, 2)} cm²",
            f"{round(2 * (22 / 7) * r * (r + h), 2)} cm²",
        ]

    # ------------------------------------------------
    # TRUE / FALSE
    # ------------------------------------------------
    elif qtype == "true_false":
        question = "The total surface area of a cube of side a is 6a²."

        correct = "True"
        wrongs = ["False", "Cannot be determined", "Only for cuboids"]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = "Which of the following affects the surface area of a sphere?"

        correct = "Radius of the sphere"
        wrongs = [
            "Height of the sphere",
            "Length of the diameter only",
            "Volume of the sphere",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        r = random.randint(3, 6)

        question = (
            f"A spherical balloon has a radius of {r} cm. "
            f"What happens to its surface area if the radius is doubled?"
        )

        correct = "It becomes four times"
        wrongs = [
            "It becomes two times",
            "It becomes eight times",
            "It remains the same",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Surface Area of Solids",
        "needs_image": False
    }

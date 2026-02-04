import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Areas of Plane Figures between Parallel Lines

    Question Types:
    - identify_property
    - equal_areas
    - calculate_area
    - concept
    - application
    """

    qtype = random.choice(
        [
            "identify_property",
            "equal_areas",
            "calculate_area",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY PROPERTY
    # ------------------------------------------------
    if qtype == "identify_property":
        question = (
            "Which of the following plane figures between the same parallels "
            "and on the same base have equal areas?"
        )

        correct = "Parallelograms"
        wrongs = [
            "Triangles only",
            "Circles",
            "Trapeziums only",
        ]

    # ------------------------------------------------
    # EQUAL AREAS CONCEPT
    # ------------------------------------------------
    elif qtype == "equal_areas":
        question = (
            "Two triangles lie between the same parallel lines and have the same base. "
            "What can be said about their areas?"
        )

        correct = "Their areas are equal"
        wrongs = [
            "One has double the area",
            "Their areas depend on shape",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # CALCULATE AREA
    # ------------------------------------------------
    elif qtype == "calculate_area":
        base = random.randint(4, 10)
        height = random.randint(3, 8)

        question = (
            f"Find the area of a parallelogram with base {base} cm "
            f"and height {height} cm."
        )

        correct = f"{base * height} cm²"
        wrongs = [
            f"{base + height} cm²",
            f"{2 * base * height} cm²",
            f"{base * height / 2} cm²",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = (
            "What determines the area of a triangle between two parallel lines?"
        )

        correct = "Base and perpendicular height"
        wrongs = [
            "Length of sides only",
            "Angles of the triangle",
            "Position of the triangle",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "Why do triangles on the same base and between the same parallels "
            "have equal areas?"
        )

        correct = "They have the same base and height"
        wrongs = [
            "They have equal sides",
            "They are congruent",
            "They have equal angles",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Areas of Plane Figures between Parallel Lines",
        "needs_image": False
    }

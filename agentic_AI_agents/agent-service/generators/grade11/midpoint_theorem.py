import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Midpoint Theorem

    Question Types:
    - state_theorem
    - identify_property
    - true_false
    - application
    - concept
    """

    qtype = random.choice(
        [
            "state_theorem",
            "identify_property",
            "true_false",
            "application",
            "concept",
        ]
    )

    # ------------------------------------------------
    # STATE THE THEOREM
    # ------------------------------------------------
    if qtype == "state_theorem":
        question = "What does the midpoint theorem state?"

        correct = (
            "The line joining the midpoints of two sides of a triangle "
            "is parallel to the third side and half of it"
        )
        wrongs = [
            "The line joining any two points is parallel to the base",
            "The midpoint divides the triangle into equal areas",
            "The line joining midpoints is equal to the third side",
        ]

    # ------------------------------------------------
    # IDENTIFY PROPERTY
    # ------------------------------------------------
    elif qtype == "identify_property":
        question = (
            "In a triangle, a line joining the midpoints of two sides is parallel to:"
        )

        correct = "The third side"
        wrongs = [
            "The altitude",
            "The angle bisector",
            "The median",
        ]

    # ------------------------------------------------
    # TRUE / FALSE
    # ------------------------------------------------
    elif qtype == "true_false":
        question = (
            "The line joining the midpoints of two sides of a triangle "
            "is half the length of the third side."
        )

        correct = "True"
        wrongs = [
            "False",
            "Only for equilateral triangles",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    elif qtype == "application":
        base = random.choice([6, 8, 10, 12])

        question = (
            f"In a triangle, the length of the base is {base} cm. "
            f"What is the length of the line joining the midpoints "
            f"of the other two sides?"
        )

        correct = f"{base / 2} cm"
        wrongs = [
            f"{base} cm",
            f"{base * 2} cm",
            f"{base - 2} cm",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = (
            "Why is the line joining the midpoints of two sides of a triangle "
            "parallel to the third side?"
        )

        correct = "Because corresponding angles are equal"
        wrongs = [
            "Because all sides are equal",
            "Because the triangle is isosceles",
            "Because areas are equal",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Mid Point Theorem",
        "needs_image": False
    }

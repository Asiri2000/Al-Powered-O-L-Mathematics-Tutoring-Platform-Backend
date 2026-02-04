import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Matrices

    Question Types:
    - identify_order
    - matrix_addition
    - scalar_multiplication
    - determinant_concept
    - concept
    """

    qtype = random.choice(
        [
            "identify_order",
            "matrix_addition",
            "scalar_multiplication",
            "determinant_concept",
            "concept",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY ORDER OF A MATRIX
    # ------------------------------------------------
    if qtype == "identify_order":
        rows = random.randint(2, 3)
        cols = random.randint(2, 4)

        question = (
            f"What is the order of a matrix with {rows} rows and {cols} columns?"
        )

        correct = f"{rows} × {cols}"
        wrongs = [
            f"{cols} × {rows}",
            f"{rows + cols}",
            f"{rows} + {cols}",
        ]

    # ------------------------------------------------
    # MATRIX ADDITION
    # ------------------------------------------------
    elif qtype == "matrix_addition":
        question = (
            "Which condition must be satisfied to add two matrices?"
        )

        correct = "They must have the same order"
        wrongs = [
            "They must be square matrices",
            "They must have equal determinants",
            "They must have equal entries",
        ]

    # ------------------------------------------------
    # SCALAR MULTIPLICATION
    # ------------------------------------------------
    elif qtype == "scalar_multiplication":
        scalar = random.randint(2, 5)

        question = (
            f"What happens when a matrix is multiplied by a scalar {scalar}?"
        )

        correct = "Each element is multiplied by the scalar"
        wrongs = [
            "Only diagonal elements change",
            "Only rows change",
            "Only columns change",
        ]

    # ------------------------------------------------
    # DETERMINANT CONCEPT
    # ------------------------------------------------
    elif qtype == "determinant_concept":
        question = (
            "For which type of matrix is the determinant defined?"
        )

        correct = "Square matrix"
        wrongs = [
            "Rectangular matrix",
            "Row matrix",
            "Column matrix",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = (
            "Which of the following is a zero matrix?"
        )

        correct = "A matrix with all elements equal to zero"
        wrongs = [
            "A matrix with determinant zero",
            "A matrix with one zero row",
            "A matrix with no rows",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Matrices",
        "needs_image": False
    }

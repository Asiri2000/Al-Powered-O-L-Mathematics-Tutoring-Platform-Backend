import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Geometric Progressions (GP)

    Question Types:
    - identify_gp
    - find_common_ratio
    - find_nth_term
    - concept
    - application
    """

    qtype = random.choice(
        [
            "identify_gp",
            "find_common_ratio",
            "find_nth_term",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY GP
    # ------------------------------------------------
    if qtype == "identify_gp":
        question = "Which of the following is a geometric progression?"

        correct = "2, 4, 8, 16, ..."
        wrongs = [
            "2, 4, 6, 8, ...",
            "1, 4, 9, 16, ...",
            "3, 6, 10, 15, ...",
        ]

    # ------------------------------------------------
    # FIND COMMON RATIO
    # ------------------------------------------------
    elif qtype == "find_common_ratio":
        a = random.choice([2, 3, 5])
        r = random.choice([2, 3, 4])

        question = f"Find the common ratio of the GP: {a}, {a*r}, {a*(r**2)}, ..."

        correct = str(r)
        wrongs = [
            str(a),
            str(r + 1),
            str(a * r),
        ]

    # ------------------------------------------------
    # FIND Nth TERM
    # ------------------------------------------------
    elif qtype == "find_nth_term":
        a = random.choice([2, 3])
        r = random.choice([2, 3])
        n = random.choice([3, 4])

        term = a * (r ** (n - 1))

        question = (
            f"Find the {n}th term of the GP: {a}, {a*r}, {a*(r**2)}, ..."
        )

        correct = str(term)
        wrongs = [
            str(a * (r ** n)),
            str(a * n),
            str(r ** n),
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = "What defines a geometric progression?"

        correct = "Each term is obtained by multiplying the previous term by a constant"
        wrongs = [
            "Each term is obtained by adding a constant",
            "Each term is a square of the previous term",
            "Each term increases by 1",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "A bacteria culture doubles every hour. "
            "Which type of progression represents this growth?"
        )

        correct = "Geometric progression"
        wrongs = [
            "Arithmetic progression",
            "Harmonic progression",
            "Linear progression",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Geometric Progressions",
        "needs_image": False
    }

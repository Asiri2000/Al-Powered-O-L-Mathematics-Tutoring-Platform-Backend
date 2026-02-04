import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Binomial Expressions

    Question Types:
    - expand
    - identify_term
    - simplify
    - concept
    - application
    """

    qtype = random.choice(
        [
            "expand",
            "identify_term",
            "simplify",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # EXPAND BINOMIAL
    # ------------------------------------------------
    if qtype == "expand":
        a = random.randint(1, 3)
        b = random.randint(1, 5)

        question = f"Expand (x + {b})²."

        correct = f"x² + {2*b}x + {b*b}"
        wrongs = [
            f"x² + {b}x + {b}",
            f"x² + {b*b}",
            f"x² + {b}x",
        ]

    # ------------------------------------------------
    # IDENTIFY TERM
    # ------------------------------------------------
    elif qtype == "identify_term":
        question = "What is the middle term in the expansion of (a + b)²?"

        correct = "2ab"
        wrongs = ["a²", "b²", "ab"]

    # ------------------------------------------------
    # SIMPLIFY EXPRESSION
    # ------------------------------------------------
    elif qtype == "simplify":
        question = "Simplify (x + 2)(x + 3)."

        correct = "x² + 5x + 6"
        wrongs = [
            "x² + 6x + 5",
            "x² + 5x",
            "x² + 6",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = "Which identity is used to expand (a + b)²?"

        correct = "(a + b)² = a² + 2ab + b²"
        wrongs = [
            "(a − b)² = a² − 2ab + b²",
            "(a + b)³ = a³ + b³",
            "(a − b)³ = a³ − b³",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "If the side of a square is (x + 3) cm, "
            "what is the area of the square?"
        )

        correct = "x² + 6x + 9"
        wrongs = [
            "x² + 9",
            "x² + 3x + 9",
            "x² + 6x",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Binomial Expressions",
        "needs_image": False
    }

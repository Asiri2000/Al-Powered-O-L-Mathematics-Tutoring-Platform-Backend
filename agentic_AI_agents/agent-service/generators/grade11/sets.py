import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Sets

    Question Types:
    - set_notation
    - cardinality
    - union_intersection
    - complement
    - venn_application
    """

    qtype = random.choice(
        [
            "set_notation",
            "cardinality",
            "union_intersection",
            "complement",
            "venn_application",
        ]
    )

    # ------------------------------------------------
    # SET NOTATION
    # ------------------------------------------------
    if qtype == "set_notation":
        question = "Which notation represents the set of natural numbers?"

        correct = "ℕ"
        wrongs = [
            "ℤ",
            "ℚ",
            "ℝ",
        ]

    # ------------------------------------------------
    # CARDINALITY (n(A))
    # ------------------------------------------------
    elif qtype == "cardinality":
        A = {1, 2, 3, 4, 5}
        question = f"If A = {A}, find n(A)."

        correct = str(len(A))
        wrongs = [
            str(sum(A)),
            str(max(A)),
            str(min(A)),
        ]

    # ------------------------------------------------
    # UNION & INTERSECTION
    # ------------------------------------------------
    elif qtype == "union_intersection":
        A = {1, 2, 3}
        B = {3, 4, 5}

        question = f"If A = {A} and B = {B}, find A ∩ B."

        correct = "{3}"
        wrongs = [
            "{1, 2, 3, 4, 5}",
            "{1, 2}",
            "{4, 5}",
        ]

    # ------------------------------------------------
    # COMPLEMENT OF A SET
    # ------------------------------------------------
    elif qtype == "complement":
        U = {1, 2, 3, 4, 5, 6}
        A = {2, 4, 6}

        question = f"If U = {U} and A = {A}, find A′."

        correct = "{1, 3, 5}"
        wrongs = [
            "{2, 4, 6}",
            "{1, 2, 3}",
            "{4, 5, 6}",
        ]

    # ------------------------------------------------
    # VENN DIAGRAM APPLICATION
    # ------------------------------------------------
    else:
        question = (
            "In a class of 40 students, 25 study Mathematics and 18 study Science. "
            "If 10 study both subjects, how many study neither subject?"
        )

        total = 40
        nM = 25
        nS = 18
        nBoth = 10

        neither = total - (nM + nS - nBoth)

        correct = str(neither)
        wrongs = [
            str(nM + nS),
            str(nBoth),
            str(total - nM),
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Sets",
        "needs_image": False
    }

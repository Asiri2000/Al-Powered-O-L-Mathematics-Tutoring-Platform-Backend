import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Pythagoras's Theorem

    Question Types:
    - find_hypotenuse
    - find_leg
    - verify_right_triangle
    - concept
    - application
    """

    qtype = random.choice(
        [
            "find_hypotenuse",
            "find_leg",
            "verify_right_triangle",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # FIND HYPOTENUSE
    # ------------------------------------------------
    if qtype == "find_hypotenuse":
        a = random.choice([3, 5, 6])
        b = random.choice([4, 12, 8])

        question = (
            f"Find the length of the hypotenuse of a right-angled triangle "
            f"with sides {a} cm and {b} cm."
        )

        correct = f"{int((a*a + b*b) ** 0.5)} cm"
        wrongs = [
            f"{a + b} cm",
            f"{a * b} cm",
            f"{abs(a - b)} cm",
        ]

    # ------------------------------------------------
    # FIND ONE LEG
    # ------------------------------------------------
    elif qtype == "find_leg":
        hyp = random.choice([5, 10, 13])
        leg = random.choice([3, 6, 5])

        question = (
            f"A right-angled triangle has hypotenuse {hyp} cm "
            f"and one side {leg} cm. Find the length of the other side."
        )

        correct = f"{int((hyp*hyp - leg*leg) ** 0.5)} cm"
        wrongs = [
            f"{hyp - leg} cm",
            f"{hyp + leg} cm",
            f"{leg * 2} cm",
        ]

    # ------------------------------------------------
    # VERIFY RIGHT-ANGLED TRIANGLE
    # ------------------------------------------------
    elif qtype == "verify_right_triangle":
        question = (
            "Check whether a triangle with sides 6 cm, 8 cm, and 10 cm "
            "is right-angled."
        )

        correct = "Yes"
        wrongs = [
            "No",
            "Only if angle is 60°",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = (
            "Which of the following correctly states Pythagoras's theorem?"
        )

        correct = "Square of hypotenuse = sum of squares of the other two sides"
        wrongs = [
            "Sum of sides = hypotenuse",
            "Product of sides = hypotenuse",
            "Square of one side = sum of others",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "A ladder 13 m long rests against a wall. "
            "The foot of the ladder is 5 m away from the wall. "
            "How high up the wall does the ladder reach?"
        )

        correct = "12 m"
        wrongs = [
            "8 m",
            "10 m",
            "13 m",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Pythagoras's Theorem",
        "needs_image": False
    }

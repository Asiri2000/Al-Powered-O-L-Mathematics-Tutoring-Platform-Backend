import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Percentages

    Question Types:
    - convert_percentage
    - percentage_of_quantity
    - increase_decrease
    - concept
    - application
    """

    qtype = random.choice(
        [
            "convert_percentage",
            "percentage_of_quantity",
            "increase_decrease",
            "concept",
            "application",
        ]
    )

    # ------------------------------------------------
    # CONVERT PERCENTAGE
    # ------------------------------------------------
    if qtype == "convert_percentage":
        question = "Convert 25% into a fraction."

        correct = "1/4"
        wrongs = [
            "25/100",
            "2/5",
            "1/5",
        ]

    # ------------------------------------------------
    # PERCENTAGE OF A QUANTITY
    # ------------------------------------------------
    elif qtype == "percentage_of_quantity":
        percent = random.choice([10, 20, 25, 40])
        number = random.choice([50, 80, 120, 200])

        question = f"Find {percent}% of {number}."

        correct = str(int((percent / 100) * number))
        wrongs = [
            str(int((percent / 10) * number)),
            str(int((percent / 100) * (number / 2))),
            str(int(number / percent)),
        ]

    # ------------------------------------------------
    # INCREASE / DECREASE
    # ------------------------------------------------
    elif qtype == "increase_decrease":
        value = random.choice([200, 500, 800])
        percent = random.choice([10, 20, 25])

        question = (
            f"A value of Rs. {value} is increased by {percent}%. "
            f"What is the new value?"
        )

        correct = str(int(value + (percent / 100) * value))
        wrongs = [
            str(int(value - (percent / 100) * value)),
            str(int(value * percent)),
            str(value),
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    elif qtype == "concept":
        question = "What does 100% represent?"

        correct = "The whole quantity"
        wrongs = [
            "Half of the quantity",
            "Double the quantity",
            "One part of the quantity",
        ]

    # ------------------------------------------------
    # APPLICATION QUESTION
    # ------------------------------------------------
    else:
        question = (
            "A student scored 72 marks out of 90. "
            "What is the percentage score?"
        )

        correct = "80%"
        wrongs = [
            "72%",
            "90%",
            "75%",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Percentages",
        "needs_image": False
    }

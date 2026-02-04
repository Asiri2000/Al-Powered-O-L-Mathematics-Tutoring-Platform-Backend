import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Probability

    Question Types:
    - basic_probability
    - dice_probability
    - card_probability
    - complement_rule
    - application
    """

    qtype = random.choice(
        [
            "basic_probability",
            "dice_probability",
            "card_probability",
            "complement_rule",
            "application",
        ]
    )

    # ------------------------------------------------
    # BASIC PROBABILITY
    # ------------------------------------------------
    if qtype == "basic_probability":
        question = (
            "A fair coin is tossed once. "
            "What is the probability of getting a head?"
        )

        correct = "1/2"
        wrongs = [
            "1",
            "0",
            "2",
        ]

    # ------------------------------------------------
    # DICE PROBABILITY
    # ------------------------------------------------
    elif qtype == "dice_probability":
        question = (
            "A fair die is thrown once. "
            "What is the probability of getting a number greater than 4?"
        )

        correct = "1/3"
        wrongs = [
            "1/6",
            "1/2",
            "2/3",
        ]

    # ------------------------------------------------
    # CARD PROBABILITY
    # ------------------------------------------------
    elif qtype == "card_probability":
        question = (
            "A card is drawn at random from a standard deck of 52 cards. "
            "What is the probability of getting a heart?"
        )

        correct = "1/4"
        wrongs = [
            "1/13",
            "1/52",
            "1/2",
        ]

    # ------------------------------------------------
    # COMPLEMENT RULE
    # ------------------------------------------------
    elif qtype == "complement_rule":
        question = (
            "If the probability of an event A is 0.35, "
            "what is the probability of not A?"
        )

        correct = "0.65"
        wrongs = [
            "0.35",
            "1.35",
            "0",
        ]

    # ------------------------------------------------
    # APPLICATION / WORD PROBLEM
    # ------------------------------------------------
    else:
        question = (
            "A bag contains 5 red balls and 3 blue balls. "
            "One ball is drawn at random. "
            "What is the probability of getting a blue ball?"
        )

        correct = "3/8"
        wrongs = [
            "5/8",
            "1/3",
            "1/2",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Probability",
        "needs_image": False
    }

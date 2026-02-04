import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Share Market

    Question Types:
    - face_value
    - market_value
    - dividend_calculation
    - gain_loss
    - concept
    """

    qtype = random.choice(
        [
            "face_value",
            "market_value",
            "dividend_calculation",
            "gain_loss",
            "concept",
        ]
    )

    # ------------------------------------------------
    # FACE VALUE
    # ------------------------------------------------
    if qtype == "face_value":
        question = "What is meant by the face value of a share?"

        correct = "The original value of the share"
        wrongs = [
            "The current market price",
            "The selling price",
            "The profit gained",
        ]

    # ------------------------------------------------
    # MARKET VALUE
    # ------------------------------------------------
    elif qtype == "market_value":
        question = "What is meant by the market value of a share?"

        correct = "The price at which the share is bought or sold"
        wrongs = [
            "The value printed on the share",
            "The dividend amount",
            "The total profit",
        ]

    # ------------------------------------------------
    # DIVIDEND CALCULATION
    # ------------------------------------------------
    elif qtype == "dividend_calculation":
        face_value = random.choice([50, 100])
        dividend_percent = random.choice([5, 10, 12])
        shares = random.choice([20, 50, 100])

        question = (
            f"A person owns {shares} shares of face value Rs. {face_value} each "
            f"which pays a dividend of {dividend_percent}%. "
            f"Find the total dividend received."
        )

        dividend_per_share = (dividend_percent / 100) * face_value
        total_dividend = int(dividend_per_share * shares)

        correct = f"Rs. {total_dividend}"
        wrongs = [
            f"Rs. {int(dividend_percent * shares)}",
            f"Rs. {int(face_value * shares)}",
            f"Rs. {int(dividend_percent * face_value)}",
        ]

    # ------------------------------------------------
    # GAIN / LOSS
    # ------------------------------------------------
    elif qtype == "gain_loss":
        face_value = random.choice([50, 100])
        market_value = face_value + random.choice([10, 20, 30])
        shares = random.choice([10, 20, 50])

        question = (
            f"{shares} shares of face value Rs. {face_value} are bought at "
            f"Rs. {market_value} each. "
            f"Is this a gain or a loss?"
        )

        correct = "Loss"
        wrongs = [
            "Gain",
            "No profit or loss",
            "Cannot be determined",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = "Dividend is calculated on which value of a share?"

        correct = "Face value"
        wrongs = [
            "Market value",
            "Selling price",
            "Buying price",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Share Market",
        "needs_image": False
    }

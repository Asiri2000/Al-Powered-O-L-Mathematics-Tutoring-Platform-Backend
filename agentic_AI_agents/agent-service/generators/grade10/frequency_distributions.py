import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["total_frequency", "modal_value", "concept"])

    # ---- TOTAL FREQUENCY ----
    if qtype == "total_frequency":
        freqs = [random.randint(2, 6) for _ in range(4)]
        correct = str(sum(freqs))
        options, ans = shuffle_options(
            correct,
            [str(sum(freqs)-1), str(sum(freqs)+2), str(max(freqs))]
        )
        question = f"Find the total frequency if the frequencies are {freqs}."

    # ---- MODE ----
    elif qtype == "modal_value":
        correct = "The value with highest frequency"
        options, ans = shuffle_options(
            correct,
            [
                "The average value",
                "The middle value",
                "The smallest value"
            ]
        )
        question = "What is the mode of a frequency distribution?"

    # ---- CONCEPT ----
    else:
        correct = "Organizes data systematically"
        options, ans = shuffle_options(
            correct,
            [
                "Finds area",
                "Calculates speed",
                "Solves equations"
            ]
        )
        question = "What is the purpose of a frequency distribution table?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Frequency Distributions",
        "needs_image": False
    }

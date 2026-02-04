import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["nth_term", "common_difference", "concept"])

    a = random.randint(1, 6)
    d = random.randint(2, 6)

    # ---- Nth TERM ----
    if qtype == "nth_term":
        n = random.randint(5, 10)
        correct = str(a + (n - 1) * d)
        options, ans = shuffle_options(
            correct,
            [
                str(a + n * d),
                str(a + (n - 2) * d),
                str(a + (n + 1) * d)
            ]
        )
        question = f"Find the {n}th term of the arithmetic progression {a}, {a+d}, {a+2*d}, ..."

    # ---- COMMON DIFFERENCE ----
    elif qtype == "common_difference":
        correct = str(d)
        options, ans = shuffle_options(
            correct,
            [str(d+1), str(d-1), str(2*d)]
        )
        question = f"Find the common difference of the arithmetic progression {a}, {a+d}, {a+2*d}."

    # ---- CONCEPT ----
    else:
        correct = "Common difference"
        options, ans = shuffle_options(
            correct,
            ["Common ratio", "First term", "Last term"]
        )
        question = "What is the constant difference between consecutive terms of an arithmetic progression called?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Arithmetic Progressions",
        "needs_image": False
    }

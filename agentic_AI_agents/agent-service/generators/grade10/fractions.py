import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty):
    qtype = random.choice([
        "add",
        "subtract",
        "multiply",
        "divide",
        "simplify",
        "mixed_to_improper",
        "improper_to_mixed"
    ])

    # ---------------- ADDITION ----------------
    if qtype == "add":
        a, b = random.randint(1,5), random.randint(2,9)
        c, d = random.randint(1,5), random.randint(2,9)

        correct = f"{a*d + b*c}/{b*d}"
        options, ans = shuffle_options(
            correct,
            [f"{a+c}/{b+d}", f"{a*d}/{b*c}", f"{a+b}/{c+d}"]
        )
        question = f"Find the value of {a}/{b} + {c}/{d}."

    # ---------------- SUBTRACTION ----------------
    elif qtype == "subtract":
        a, b = random.randint(3,7), random.randint(2,9)
        c, d = random.randint(1,5), random.randint(2,9)

        correct = f"{a*d - b*c}/{b*d}"
        options, ans = shuffle_options(
            correct,
            [f"{a-c}/{b-d}", f"{a*d}/{b*c}", f"{a-c}/{b}"]
        )
        question = f"Find the value of {a}/{b} − {c}/{d}."

    # ---------------- MULTIPLICATION ----------------
    elif qtype == "multiply":
        a, b = random.randint(1,5), random.randint(2,7)
        c, d = random.randint(1,5), random.randint(2,7)

        correct = f"{a*c}/{b*d}"
        options, ans = shuffle_options(
            correct,
            [f"{a+c}/{b+d}", f"{a*d}/{b*c}", f"{a+b}/{c+d}"]
        )
        question = f"Find the value of {a}/{b} × {c}/{d}."

    # ---------------- DIVISION ----------------
    elif qtype == "divide":
        a, b = random.randint(1,5), random.randint(2,7)
        c, d = random.randint(1,5), random.randint(2,7)

        correct = f"{a*d}/{b*c}"
        options, ans = shuffle_options(
            correct,
            [f"{a*c}/{b*d}", f"{a+d}/{b+c}", f"{a*b}/{c*d}"]
        )
        question = f"Find the value of {a}/{b} ÷ {c}/{d}."

    # ---------------- SIMPLIFY ----------------
    elif qtype == "simplify":
        base = random.randint(2,6)
        num = base * random.randint(2,4)
        den = base * random.randint(3,6)

        correct = f"{num//base}/{den//base}"
        options, ans = shuffle_options(
            correct,
            [f"{num}/{den}", f"{num//2}/{den//2}", f"{num//3}/{den//3}"]
        )
        question = f"Simplify the fraction {num}/{den}."

    # ---------------- MIXED → IMPROPER ----------------
    elif qtype == "mixed_to_improper":
        whole = random.randint(1,4)
        num = random.randint(1,5)
        den = random.randint(2,7)

        correct = f"{whole*den + num}/{den}"
        options, ans = shuffle_options(
            correct,
            [f"{whole}/{den}", f"{num}/{den}", f"{whole*den}/{num}"]
        )
        question = f"Convert the mixed number {whole} {num}/{den} into an improper fraction."

    # ---------------- IMPROPER → MIXED ----------------
    else:
        den = random.randint(2,7)
        whole = random.randint(1,4)
        num = random.randint(1, den-1)

        improper = whole*den + num
        correct = f"{whole} {num}/{den}"
        options, ans = shuffle_options(
            correct,
            [f"{num}/{den}", f"{whole}/{den}", f"{improper}/{den}"]
        )
        question = f"Convert the improper fraction {improper}/{den} into a mixed number."

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Fractions",
        "needs_image": False
    }

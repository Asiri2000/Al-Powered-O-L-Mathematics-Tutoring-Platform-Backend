import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty):
    shape = random.choice([
        "rectangle",
        "square",
        "triangle",
        "parallelogram",
        "trapezium"
    ])

    # ---------------- RECTANGLE ----------------
    if shape == "rectangle":
        l = random.randint(4, 12)
        w = random.randint(3, 10)
        correct = f"{l * w} cm²"

        options, ans = shuffle_options(
            correct,
            [f"{2*l*w} cm²", f"{l+w} cm²", f"{l*w+w} cm²"]
        )

        question = f"Find the area of a rectangle of length {l} cm and width {w} cm."

    # ---------------- SQUARE ----------------
    elif shape == "square":
        a = random.randint(4, 15)
        correct = f"{a * a} cm²"

        options, ans = shuffle_options(
            correct,
            [f"{4*a} cm²", f"{2*a*a} cm²", f"{a*(a+1)} cm²"]
        )

        question = f"Find the area of a square with side {a} cm."

    # ---------------- TRIANGLE ----------------
    elif shape == "triangle":
        b = random.randint(6, 14)
        h = random.randint(4, 10)
        correct = f"{(b*h)//2} cm²"

        options, ans = shuffle_options(
            correct,
            [f"{b*h} cm²", f"{b+h} cm²", f"{(b*h)//3} cm²"]
        )

        question = f"Find the area of a triangle with base {b} cm and height {h} cm."

    # ---------------- PARALLELOGRAM ----------------
    elif shape == "parallelogram":
        b = random.randint(6, 14)
        h = random.randint(4, 10)
        correct = f"{b*h} cm²"

        options, ans = shuffle_options(
            correct,
            [f"{2*b*h} cm²", f"{b+h} cm²", f"{b*h+h} cm²"]
        )

        question = f"Find the area of a parallelogram with base {b} cm and height {h} cm."

    # ---------------- TRAPEZIUM ----------------
    else:
        a = random.randint(4, 10)
        b = random.randint(6, 14)
        h = random.randint(4, 8)
        correct = f"{((a+b)*h)//2} cm²"

        options, ans = shuffle_options(
            correct,
            [f"{(a+b)*h} cm²", f"{a*b*h} cm²", f"{(a+b)} cm²"]
        )

        question = f"Find the area of a trapezium with parallel sides {a} cm and {b} cm, and height {h} cm."

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Area",
        "needs_image": True  # 🔥 diagrams make sense here
    }

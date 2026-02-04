import random
import math
from generators.utils.shuffle import shuffle_options

def generate(difficulty):
    shape = random.choice([
        "rectangle",
        "square",
        "triangle",
        "parallelogram",
        "trapezium",
        "circle"
    ])

    if shape == "rectangle":
        l = random.randint(6, 14)
        w = random.randint(4, 10)
        correct = f"{2*(l+w)} cm"
        wrongs = [f"{l+w} cm", f"{2*l+w} cm", f"{l+2*w} cm"]
        question = f"Find the perimeter of a rectangle of length {l} cm and width {w} cm."

    elif shape == "square":
        a = random.randint(4, 15)
        correct = f"{4*a} cm"
        wrongs = [f"{a*a} cm", f"{2*a} cm", f"{3*a} cm"]
        question = f"Find the perimeter of a square with side {a} cm."

    elif shape == "triangle":
        a, b, c = random.randint(4,10), random.randint(5,12), random.randint(6,14)
        correct = f"{a+b+c} cm"
        wrongs = [f"{a+b} cm", f"{2*(a+b)} cm", f"{a*b} cm"]
        question = f"Find the perimeter of a triangle with sides {a} cm, {b} cm and {c} cm."

    elif shape == "parallelogram":
        a, b = random.randint(6,14), random.randint(4,10)
        correct = f"{2*(a+b)} cm"
        wrongs = [f"{a+b} cm", f"{a*b} cm", f"{2*a+b} cm"]
        question = f"Find the perimeter of a parallelogram with adjacent sides {a} cm and {b} cm."

    elif shape == "trapezium":
        a, b, c, d = [random.randint(4,12) for _ in range(4)]
        correct = f"{a+b+c+d} cm"
        wrongs = [f"{a+b} cm", f"{2*(a+b)} cm", f"{a*b} cm"]
        question = f"Find the perimeter of a trapezium with sides {a} cm, {b} cm, {c} cm and {d} cm."

    else:  # circle
        r = random.randint(3, 10)
        correct = f"{round(2*math.pi*r,1)} cm"
        wrongs = [
            f"{round(math.pi*r,1)} cm",
            f"{round(math.pi*r*r,1)} cm",
            f"{round(2*r,1)} cm"
        ]
        question = "Find the perimeter (circumference) of a circle of radius {} cm. (Take π = 3.14)".format(r)

    options, ans = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Perimeter",
        "needs_image": True
    }

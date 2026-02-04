import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice([
        "angle_sum",
        "missing_angle",
        "isosceles",
        "equilateral",
        "exterior_angle",
        "right_triangle",
        "classification"
    ])

    # ---------------- ANGLE SUM ----------------
    if qtype == "angle_sum":
        correct = "180°"
        options, ans = shuffle_options(
            correct,
            ["90°", "360°", "270°"]
        )
        question = "Find the sum of the interior angles of a triangle."

    # ---------------- MISSING ANGLE ----------------
    elif qtype == "missing_angle":
        a = random.randint(30, 80)
        b = random.randint(30, 80)
        c = 180 - (a + b)

        correct = f"{c}°"
        options, ans = shuffle_options(
            correct,
            [f"{a}°", f"{b}°", f"{180-c}°"]
        )
        question = f"In a triangle, two angles are {a}° and {b}°. Find the third angle."

    # ---------------- ISOSCELES TRIANGLE ----------------
    elif qtype == "isosceles":
        base = random.randint(30, 60)
        equal = (180 - base) // 2

        correct = f"{equal}°"
        options, ans = shuffle_options(
            correct,
            [f"{base}°", f"{180-base}°", f"{equal+10}°"]
        )
        question = f"In an isosceles triangle, the base angle is {base}°. Find one of the equal angles."

    # ---------------- EQUILATERAL TRIANGLE ----------------
    elif qtype == "equilateral":
        correct = "60°"
        options, ans = shuffle_options(
            correct,
            ["45°", "90°", "120°"]
        )
        question = "Find the measure of each angle of an equilateral triangle."

    # ---------------- EXTERIOR ANGLE ----------------
    elif qtype == "exterior_angle":
        a = random.randint(30, 70)
        b = random.randint(30, 70)
        exterior = a + b

        correct = f"{exterior}°"
        options, ans = shuffle_options(
            correct,
            [f"{180-exterior}°", f"{a}°", f"{b}°"]
        )
        question = f"The two interior opposite angles of a triangle are {a}° and {b}°. Find the exterior angle."

    # ---------------- RIGHT-ANGLED TRIANGLE ----------------
    elif qtype == "right_triangle":
        angle = random.choice([30, 45, 60])
        correct = f"{90-angle}°"

        options, ans = shuffle_options(
            correct,
            [f"{angle}°", "90°", "180°"]
        )
        question = f"In a right-angled triangle, one acute angle is {angle}°. Find the other acute angle."

    # ---------------- CLASSIFICATION ----------------
    else:
        correct = "Isosceles"
        options, ans = shuffle_options(
            correct,
            ["Scalene", "Equilateral", "Right-angled"]
        )
        question = "A triangle has two equal sides. What type of triangle is this?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Triangles",
        "needs_image": True
    }

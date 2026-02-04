import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice([
        "cube_volume",
        "cuboid_surface",
        "cylinder_volume",
        "sphere_surface"
    ])

    # ---- CUBE VOLUME ----
    if qtype == "cube_volume":
        a = random.randint(3, 8)
        correct = f"{a**3} cm³"
        options, ans = shuffle_options(
            correct,
            [f"{6*a*a} cm³", f"{a*a} cm³", f"{3*a} cm³"]
        )
        question = f"Find the volume of a cube of side {a} cm."

    # ---- CUBOID SURFACE AREA ----
    elif qtype == "cuboid_surface":
        l, w, h = random.randint(4, 8), random.randint(3, 6), random.randint(2, 5)
        correct = f"{2*(l*w + l*h + w*h)} cm²"
        options, ans = shuffle_options(
            correct,
            [
                f"{l*w*h} cm²",
                f"{2*(l+w+h)} cm²",
                f"{l*w + w*h + l*h} cm²"
            ]
        )
        question = f"Find the total surface area of a cuboid of length {l} cm, width {w} cm and height {h} cm."

    # ---- CYLINDER VOLUME ----
    elif qtype == "cylinder_volume":
        r = random.randint(3, 6)
        h = random.randint(5, 10)
        correct = f"{round(3.14*r*r*h,2)} cm³"
        options, ans = shuffle_options(
            correct,
            [
                f"{round(2*3.14*r*h,2)} cm³",
                f"{round(3.14*r*r,2)} cm³",
                f"{round(3.14*r*h,2)} cm³"
            ]
        )
        question = f"Find the volume of a cylinder of radius {r} cm and height {h} cm."

    # ---- SPHERE SURFACE AREA ----
    else:
        r = random.randint(3, 7)
        correct = f"{round(4*3.14*r*r,2)} cm²"
        options, ans = shuffle_options(
            correct,
            [
                f"{round(3.14*r*r,2)} cm²",
                f"{round(2*3.14*r*r,2)} cm²",
                f"{round(4*3.14*r,2)} cm²"
            ]
        )
        question = f"Find the surface area of a sphere of radius {r} cm."

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Surface Area and Volume",
        "needs_image": True
    }

import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice([
        "scale_distance",
        "scale_ratio",
        "concept"
    ])

    # ---- DISTANCE ----
    if qtype == "scale_distance":
        map_dist = random.randint(2, 6)
        scale = random.choice([1000, 500, 2000])
        correct = f"{map_dist*scale} cm"
        options, ans = shuffle_options(
            correct,
            [
                f"{map_dist+scale} cm",
                f"{scale} cm",
                f"{map_dist*scale//2} cm"
            ]
        )
        question = f"On a map drawn to a scale of 1 : {scale}, a distance measures {map_dist} cm. Find the actual distance."

    # ---- SCALE RATIO ----
    elif qtype == "scale_ratio":
        correct = "1 : 1000"
        options, ans = shuffle_options(
            correct,
            ["1000 : 1", "1 : 100", "10 : 1"]
        )
        question = "Which scale represents a reduction drawing?"

    # ---- CONCEPT ----
    else:
        correct = "Ratio of drawing to actual object"
        options, ans = shuffle_options(
            correct,
            [
                "Area of diagram",
                "Perimeter of diagram",
                "Volume of object"
            ]
        )
        question = "What does the scale of a diagram represent?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Scale Diagrams",
        "needs_image": True
    }

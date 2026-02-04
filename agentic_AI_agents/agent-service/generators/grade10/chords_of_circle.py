import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["equal_chords", "distance", "concept"])

    # ---- EQUAL CHORDS ----
    if qtype == "equal_chords":
        correct = "They are equidistant from the center"
        options, ans = shuffle_options(
            correct,
            [
                "They form a diameter",
                "They intersect at right angles",
                "They are tangents"
            ]
        )
        question = "What can be said about equal chords of a circle?"

    # ---- DISTANCE ----
    elif qtype == "distance":
        correct = "The longer chord is nearer to the center"
        options, ans = shuffle_options(
            correct,
            [
                "The shorter chord is nearer",
                "Both are equally distant",
                "Distance cannot be compared"
            ]
        )
        question = "Which chord of a circle is nearer to the center?"

    # ---- CONCEPT ----
    else:
        correct = "A line segment joining two points on a circle"
        options, ans = shuffle_options(
            correct,
            [
                "A line touching the circle",
                "A radius",
                "A diameter"
            ]
        )
        question = "What is a chord of a circle?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Chords of a Circle",
        "needs_image": True
    }

import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice(["solve", "sign_change", "concept"])

    # ---- SOLVING ----
    if qtype == "solve":
        x = random.randint(2, 6)
        correct = f"x > {x}"
        options, ans = shuffle_options(
            correct,
            [f"x < {x}", f"x = {x}", f"x ≥ {x}"]
        )
        question = f"Solve the inequality x + {x} > {2*x}."

    # ---- SIGN CHANGE ----
    elif qtype == "sign_change":
        correct = "The inequality sign reverses"
        options, ans = shuffle_options(
            correct,
            [
                "The sign remains same",
                "The inequality disappears",
                "The value becomes zero"
            ]
        )
        question = "What happens to the inequality sign when both sides are multiplied by a negative number?"

    # ---- CONCEPT ----
    else:
        correct = "A range of values"
        options, ans = shuffle_options(
            correct,
            ["A single value", "Only integers", "Only fractions"]
        )
        question = "What does the solution of an inequality represent?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Algebraic Inequalities",
        "needs_image": False
    }

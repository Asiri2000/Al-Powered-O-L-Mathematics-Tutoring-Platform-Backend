import random
from generators.utils.shuffle import shuffle_options

def generate(difficulty=3):
    qtype = random.choice([
        "sss",
        "sas",
        "asa",
        "reason"
    ])

    # -------- SSS --------
    if qtype == "sss":
        correct = "SSS"
        options, ans = shuffle_options(
            correct,
            ["SAS", "ASA", "RHS"]
        )
        question = "Two triangles have three corresponding sides equal. Which congruence rule applies?"

    # -------- SAS --------
    elif qtype == "sas":
        correct = "SAS"
        options, ans = shuffle_options(
            correct,
            ["SSS", "ASA", "RHS"]
        )
        question = "Two sides and the included angle of one triangle are equal to another. Which rule proves congruence?"

    # -------- ASA --------
    elif qtype == "asa":
        correct = "ASA"
        options, ans = shuffle_options(
            correct,
            ["SSS", "SAS", "RHS"]
        )
        question = "Two angles and a side of one triangle are equal to another. Which rule applies?"

    # -------- REASON --------
    else:
        correct = "Corresponding parts are equal"
        options, ans = shuffle_options(
            correct,
            [
                "Vertically opposite angles",
                "Alternate angles",
                "Angles in a straight line"
            ]
        )
        question = "If two triangles are congruent, why are their corresponding sides equal?"

    return {
        "question": question,
        "options": options,
        "correct_answer": ans,
        "difficulty": difficulty,
        "concept": "Congruence of Triangles",
        "needs_image": True
    }

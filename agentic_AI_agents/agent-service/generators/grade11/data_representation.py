import random
from generators.utils.shuffle import shuffle_options


def generate(difficulty: int = 3):
    """
    Grade 11 – Data Representation and Interpretation

    Question Types:
    - identify_chart
    - mean_calculation
    - mode_median
    - interpretation
    - concept
    """

    qtype = random.choice(
        [
            "identify_chart",
            "mean_calculation",
            "mode_median",
            "interpretation",
            "concept",
        ]
    )

    # ------------------------------------------------
    # IDENTIFY CHART TYPE
    # ------------------------------------------------
    if qtype == "identify_chart":
        question = (
            "Which type of diagram is best suited to show "
            "the comparison of different categories?"
        )

        correct = "Bar chart"
        wrongs = [
            "Line graph",
            "Pie chart",
            "Histogram",
        ]

    # ------------------------------------------------
    # MEAN CALCULATION
    # ------------------------------------------------
    elif qtype == "mean_calculation":
        values = [random.randint(5, 15) for _ in range(5)]
        total = sum(values)

        question = (
            f"Find the mean of the following data: {', '.join(map(str, values))}."
        )

        correct = str(round(total / len(values), 2))
        wrongs = [
            str(total),
            str(len(values)),
            str(round(total / (len(values) - 1), 2)),
        ]

    # ------------------------------------------------
    # MODE / MEDIAN
    # ------------------------------------------------
    elif qtype == "mode_median":
        question = "Which measure of central tendency represents the most frequent value?"

        correct = "Mode"
        wrongs = [
            "Mean",
            "Median",
            "Range",
        ]

    # ------------------------------------------------
    # DATA INTERPRETATION
    # ------------------------------------------------
    elif qtype == "interpretation":
        question = (
            "If the mean of a data set is 20, what is the total of 5 observations?"
        )

        correct = "100"
        wrongs = [
            "25",
            "20",
            "5",
        ]

    # ------------------------------------------------
    # CONCEPTUAL QUESTION
    # ------------------------------------------------
    else:
        question = "Which of the following is NOT a measure of central tendency?"

        correct = "Range"
        wrongs = [
            "Mean",
            "Median",
            "Mode",
        ]

    options, answer = shuffle_options(correct, wrongs)

    return {
        "question": question,
        "options": options,
        "correct_answer": answer,
        "difficulty": difficulty,
        "concept": "Data Representation and Interpretation",
        "needs_image": False
    }

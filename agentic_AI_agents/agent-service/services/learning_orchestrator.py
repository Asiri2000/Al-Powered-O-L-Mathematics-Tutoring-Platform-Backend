from services.difficulty_engine import adjust_difficulty
from services.progression_engine import determine_learning_stage
from services.decision_engine import decide_next_action

def orchestrate_learning(analytics, current_difficulty):
    accuracy = float(analytics["accuracy_percentage"]) / 100
    avg_time = float(analytics["avg_time_seconds"])
    attempts = int(analytics["total_attempts"])

    stage = determine_learning_stage(accuracy, attempts)
    action = decide_next_action(stage)

    new_difficulty = adjust_difficulty(
        current_difficulty, accuracy, avg_time
    )

    return {
        "learning_stage": stage,
        "next_action": action,
        "recommended_difficulty": new_difficulty
    }

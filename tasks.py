def grade_task_1(predicted: str, actual: str) -> float:
    return 1.0 if predicted == actual else 0.0


def grade_task_2(predicted: str, actual: str) -> float:
    if predicted == actual:
        return 1.0
    elif predicted in actual:
        return 0.5
    return 0.0


def grade_task_3(classification_correct: bool, action_correct: bool, good_reply: bool) -> float:
    score = 0.0
    if classification_correct:
        score += 0.3
    if action_correct:
        score += 0.3
    if good_reply:
        score += 0.4
    return score
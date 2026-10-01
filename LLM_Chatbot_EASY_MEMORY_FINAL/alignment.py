def reward(answer):
    """Simple educational preference score, not full RLHF/DPO training."""
    score = 0
    if len(answer.strip()) >= 20:
        score += 1
    if "I don't know" not in answer:
        score += 1
    return score


def compare(chosen, rejected):
    return {
        "chosen_reward": reward(chosen),
        "rejected_reward": reward(rejected),
    }

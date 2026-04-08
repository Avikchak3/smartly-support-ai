from env import SmartSupportEnv
from models import Action


def run():
    env = SmartSupportEnv()

    # ✅ START BLOCK
    print("[START] task=customer_support", flush=True)

    # Reset environment
    obs = env.reset()

    total_reward = 0
    step_count = 0

    # ✅ STEP 1: classify issue
    action = Action(action_type="classify_issue", content="refund")
    obs, reward, done, info = env.step(action)

    step_count += 1
    total_reward += reward

    print(f"[STEP] step={step_count} reward={reward}", flush=True)

    # ✅ STEP 2: take action
    action = Action(action_type="take_action", content="issue_refund")
    obs, reward, done, info = env.step(action)

    step_count += 1
    total_reward += reward

    print(f"[STEP] step={step_count} reward={reward}", flush=True)

    # ✅ END BLOCK (very important format)
    print(f"[END] task=customer_support score={total_reward} steps={step_count}", flush=True)


if __name__ == "__main__":
    run()

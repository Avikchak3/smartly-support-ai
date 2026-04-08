from env import SmartSupportEnv
from models import Action

def run():
    env = SmartSupportEnv()

    # START
    print("[START] task=customer_support", flush=True)

    obs = env.reset()

    # STEP 1
    action = Action(action_type="classify_issue", content="refund")
    obs, reward, done, info = env.step(action)
    print(f"[STEP] step=1 reward={reward}", flush=True)

    # STEP 2
    action = Action(action_type="take_action", content="issue_refund")
    obs, reward, done, info = env.step(action)
    print(f"[STEP] step=2 reward={reward}", flush=True)

    # END
    print(f"[END] task=customer_support score={reward} steps=2", flush=True)


if __name__ == "__main__":
    run()

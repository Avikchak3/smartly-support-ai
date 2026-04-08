from env import SmartSupportEnv
from models import Action

env = SmartSupportEnv()
obs = env.reset()

print("Starting inference...")

# Simple baseline logic
actions = [
    Action(action_type="classify_issue", content="refund"),
    Action(action_type="take_action", content="issue_refund"),
    Action(action_type="generate_reply", content="Sorry for the inconvenience. Your refund has been processed.")
]

total_reward = 0

for action in actions:
    obs, reward, done, _ = env.step(action)
    total_reward += reward
    print(f"Action: {action}, Reward: {reward}")
    if done:
        break

print("Final Score:", total_reward)
from typing import Tuple, Dict, Any
from models import Observation, Action, Reward


class SmartSupportEnv:
    def __init__(self):
        self.reset()

    def reset(self) -> Observation:
        self.state_data = {
            "customer_message": "I want a refund for my order. It arrived damaged.",
            "issue_type": None,
            "action_taken": None,
            "conversation_history": [],
            "status": "open",
            "step_count": 0,
        }
        return Observation(**self.state_data)

    def state(self) -> Dict[str, Any]:
        return self.state_data

    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict]:

        reward_value = 0.0
        done = False
        info = {"message": ""}

        self.state_data["step_count"] += 1

        # Classification
        if action.action_type == "classify_issue":
            if action.content == "refund":
                self.state_data["issue_type"] = "refund"
                reward_value += 0.3
                info["message"] = "Correct classification"
            else:
                reward_value -= 0.2
                info["message"] = "Wrong classification"

        # Action decision
        elif action.action_type == "take_action":
            if self.state_data["issue_type"] == "refund" and action.content == "issue_refund":
                self.state_data["action_taken"] = "issue_refund"
                reward_value += 0.3
                info["message"] = "Correct action"
            else:
                reward_value -= 0.2
                info["message"] = "Wrong action"

        # Generate reply
        elif action.action_type == "generate_reply":
            if action.content:
                self.state_data["conversation_history"].append(action.content)

                if "sorry" in action.content.lower() and "refund" in action.content.lower():
                    reward_value += 0.4
                    info["message"] = "Good response"
                else:
                    reward_value -= 0.1
                    info["message"] = "Weak response"

                done = True

        # Escalation
        elif action.action_type == "escalate_ticket":
            self.state_data["status"] = "escalated"
            reward_value += 0.1
            info["message"] = "Ticket escalated"

        else:
            reward_value -= 0.1
            info["message"] = "Invalid or noop action"

        # Episode end condition
        if self.state_data["step_count"] >= 5:
            done = True

        return Observation(**self.state_data), reward_value, done, info
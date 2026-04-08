from typing import Optional, List
from pydantic import BaseModel


class Observation(BaseModel):
    customer_message: str
    issue_type: Optional[str] = None
    action_taken: Optional[str] = None
    conversation_history: List[str] = []
    status: str


class Action(BaseModel):
    action_type: str
    content: Optional[str] = None


class Reward(BaseModel):
    score: float
    message: Optional[str] = None
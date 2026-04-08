# 🚀 Smartly.Support AI
---
title: Smartly Support AI
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: Docker
app_port: 8000
---
An OpenEnv-compliant environment that simulates real-world customer support workflows, enabling AI agents to learn how to handle customer queries efficiently.

---

## 🧠 Problem

Modern companies receive a massive volume of customer queries such as:
- Refund requests
- Order issues
- Complaints
- General queries

Handling these manually is:
- Slow ⏳
- Inconsistent ❌
- Expensive 💰

---

## 💡 Solution

Smartly.Support AI provides a simulated environment where AI agents can:
- Understand customer intent
- Classify issues
- Decide appropriate actions
- Generate professional responses

This environment enables training and evaluation of AI agents in a structured and realistic setting.

---

## ⚙️ OpenEnv Compliance

The environment fully implements the OpenEnv interface:

- `reset()` → Initializes a new episode  
- `step(action)` → Executes an action and returns observation, reward, done, info  
- `state()` → Returns the current environment state  

All components use typed models for Observation, Action, and Reward.

---

## ⚙️ Environment Design

### 📥 Observation Space

```json
{
  "customer_message": "string",
  "issue_type": "string | null",
  "action_taken": "string | null",
  "conversation_history": ["list of messages"],
  "status": "string"
}
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from env import SmartSupportEnv
from models import Action

app = FastAPI()   # ✅ MUST COME FIRST
env = SmartSupportEnv()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Smartly.Support AI</title>
        </head>
        <body style="font-family:Arial; text-align:center; padding:50px;">
            <h1>🚀 Smartly.Support AI</h1>
            <p>AI environment for customer support automation</p>
            <a href="/docs">Go to API Docs</a>
        </body>
    </html>
    """


@app.post("/reset")
def reset():
    return env.reset().dict()


@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": obs.dict(),
        "reward": reward,
        "done": done,
        "info": info
    }
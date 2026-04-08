from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from env import SmartSupportEnv
from models import Action
import uvicorn

app = FastAPI()
env = SmartSupportEnv()


# ✅ Homepage UI (professional)
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Smartly.Support AI</title>
            <style>
                body {
                    margin: 0;
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 40px;
                    border-radius: 20px;
                    width: 500px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
                    text-align: center;
                }
                h1 { margin-bottom: 10px; }
                p { opacity: 0.8; margin-bottom: 20px; }
                input {
                    width: 90%;
                    padding: 10px;
                    border-radius: 10px;
                    border: none;
                    margin-bottom: 10px;
                }
                button {
                    padding: 10px 20px;
                    border: none;
                    border-radius: 10px;
                    background: #00c6ff;
                    color: white;
                    cursor: pointer;
                }
                button:hover { background: #0072ff; }
                .output {
                    margin-top: 20px;
                    text-align: left;
                    background: rgba(0,0,0,0.3);
                    padding: 15px;
                    border-radius: 10px;
                    font-size: 14px;
                    white-space: pre-wrap;
                }
                a { color: #00c6ff; text-decoration: none; }
            </style>
        </head>

        <body>
            <div class="container">
                <h1>🚀 Smartly.Support AI</h1>
                <p>AI-powered customer support simulation</p>

                <input id="message" placeholder="Type customer issue (e.g. refund request)" />
                <br/>
                <button onclick="send()">Send</button>

                <div class="output" id="output">Response will appear here...</div>

                <p><a href="/docs">Open API Docs</a></p>
            </div>

            <script>
                async function send() {
                    let msg = document.getElementById("message").value;

                    let response = await fetch('/step', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            action_type: "classify_issue",
                            content: msg
                        })
                    });

                    let data = await response.json();
                    document.getElementById("output").innerText = JSON.stringify(data, null, 2);
                }
            </script>
        </body>
    </html>
    """


# ✅ Reset endpoint
@app.post("/reset")
def reset():
    return env.reset().dict()


# ✅ Step endpoint
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


# ✅ REQUIRED FOR OPENENV VALIDATION (VERY IMPORTANT)
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

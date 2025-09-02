import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="My FastAPI Demo", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>FastAPI Demo</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>🚀 FastAPI is running!</h1>
            <p>Welcome to my demo app.</p>
            <ul style="list-style:none;">
                <li><a href="/">🏠 Home</a></li>
                <li><a href="/hello?name=Mark">👋 /hello</a></li>
                <li><a href="/routes">📜 /routes</a></li>
                <li><a href="/docs">📖 /docs</a></li>
            </ul>
        </body>
    </html>
    """

@app.get("/hello")
def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.get("/routes")
def list_routes():
    return {
        "available_routes": [
            {"path": route.path, "name": route.name, "methods": list(route.methods)}
            for route in app.routes
        ]
    }

if __name__ == "__main__":
    # Render will set $PORT, fallback to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "main:app",       # filename:app_instance
        host="0.0.0.0",
        port=port,
        reload=True       # enable reload locally for dev
    )

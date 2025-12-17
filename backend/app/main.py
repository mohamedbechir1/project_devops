import os
import json
import psycopg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_NAME = os.getenv("DB_NAME", "appdb")
AI_HOST = os.getenv("AI_HOST", "localhost")
AI_PORT = int(os.getenv("AI_PORT", "8001"))

app = FastAPI(title="DevOps Demo Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI backend", "db": {
        "host": DB_HOST, "port": DB_PORT, "name": DB_NAME
    }}

@app.get("/api/db-time")
def db_time():
    try:
        with psycopg.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, dbname=DB_NAME) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT NOW();")
                row = cur.fetchone()
        return {"db_time": str(row[0])}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/sentiment")
async def sentiment(payload: dict):
    text = payload.get("text", "")
    url = f"http://{AI_HOST}:{AI_PORT}/api/sentiment"
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.post(url, json={"text": text})
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {"error": str(e), "ai_url": url}

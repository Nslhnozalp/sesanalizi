from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import random
import asyncio

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

reps = ["Ayşe", "Can", "Mert", "Zeynep", "Ali"]
texts = [
    "Ürünüm hâlâ elime ulaşmadı.",
    "Destek ekibi çok nazikti, teşekkür ederim.",
    "Şu an çok kararsız kaldım, emin olamıyorum.",
    "Gerçekten çok kötü bir deneyim yaşadım.",
    "Sorun çözüldü ama biraz uğraştırdı."
]

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(3)
        data = {
            "rep": random.choice(reps),
            "text": random.choice(texts)
        }
        await websocket.send_text(json.dumps(data))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
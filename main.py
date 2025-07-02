from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow requests from all domains (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "✅ AI Review Synthesizer Backend is Running!"}

@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    # Save uploaded file to "audios" directory
    os.makedirs("audios", exist_ok=True)
    audio_path = os.path.join("audios", file.filename)

    with open(audio_path, "wb") as f:
        f.write(await file.read())

    # Simulate transcript creation
    os.makedirs("transcripts", exist_ok=True)
    transcript_path = os.path.join("transcripts", file.filename.replace(".mp3", ".txt"))

    with open(transcript_path, "w") as f:
        f.write("This is a placeholder transcript for testing.")

    return {"message": "✅ File received and dummy transcript saved."}


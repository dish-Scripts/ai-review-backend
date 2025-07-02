from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ollama

app = FastAPI()

# Allow CORS (important for frontend to talk to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReviewRequest(BaseModel):
    input_text: str

@app.get("/")
def root():
    return {"message": "✅ AI Review Synthesizer Backend is Running!"}

@app.post("/generate-review")
def generate_review(request: ReviewRequest):
    prompt = f"""
You are an expert product analyst. Based on the following summarized reviews of a product, perform a meta-analysis.

1. Identify the **Top 5–6 key features** discussed (e.g., Battery, Display, Performance).
2. For each feature, explain:
   - What multiple reviewers agreed on
   - Any disagreements or differing opinions
3. Create a final section:
   - ✅ **Consolidated Pros**
   - ❌ **Consolidated Cons**
   - 💡 **Unique Comments** (said by only one reviewer)

Use clear markdown-style formatting.

Summaries:
{request.input_text}
"""

    response = ollama.chat(
        model="mistral",  # or gemma, or any other
        messages=[{"role": "user", "content": prompt}]
    )

    return {"review": response['message']['content']}


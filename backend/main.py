    from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

# Replace with your OpenAI API key
OPENAI_API_KEY = "your-openai-api-key"

class ThoughtInput(BaseModel):
    thought: str

@app.post("/process-thought/")
async def process_thought(input_data: ThoughtInput):
    try:
       response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Organize this thought into a categorized to-do list."},
                      {"role": "user", "content": input_data.thought}],
            api_key=OPENAI_API_KEY
        )

        return {"organized_thought": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

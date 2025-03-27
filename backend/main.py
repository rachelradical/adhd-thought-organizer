from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

app = FastAPI()


class ThoughtInput(BaseModel):
    thought: str

@app.post("/process-thought/")
async def process_thought(input_data: ThoughtInput):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Organize this thought into a categorized to-do list."},
                {"role": "user", "content": input_data.thought}
            ],
            api_key=openai.api_key
        )
        # Return should align with try block, not inside API call
        return {"organized_thought": response["choices"][0]["message"]["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI, Body
from DietPlan import total_model
from fastapi.middleware.cors import CORSMiddleware
import openai
import json


openai.api_key = "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"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/diet")
async def diet(kg: float = Body(), calories: int = Body()):
    diet = total_model(kg, calories)
    return diet

@app.post("/chat")
async def chat(message: str = Body(), diet_plan: object = Body()):
    full_message = f'''
    Here is the current diet plan: 

    {diet_plan}

    and now you have to modify the food to fit this condition:
    {message}


    make sure to changes to only change the ones that do not fit. Don't add any other text besides the plan. make sure it's a valid json with dobuble quotes for strings.
    '''

    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {
                'role': 'system', 
                'content': ''
            },
            {
                'role': 'user', 
                'content': full_message
            }
        ],
        temperature=0
    )

    print("==== RESPONSE ===")
    print(response)

    response_message = response['choices'][0]['message']['content']
    print("==== RESPONSE MESSAGE ===")
    print(response_message)

    return json.loads(response_message)

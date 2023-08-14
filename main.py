from fastapi import FastAPI, Body
from DietPlan import total_model

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/diet")
async def diet(kg: float = Body(), calories: int = Body()):
    diet = total_model(kg, calories)
    return diet

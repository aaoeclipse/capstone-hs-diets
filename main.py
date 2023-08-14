from fastapi import FastAPI, request
from DietService import total_model

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/diet")
async def diet():
    kg, diets = request.data
    return total_model(kg, diets)

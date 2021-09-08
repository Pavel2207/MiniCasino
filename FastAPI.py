from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def funk():
    return{'message':'hello'}
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"status": "success", "message": "i am at backend lead"}

@app.get("/About")
def about():
    return {"project" : " loan risk model", "version":"1.0.10"}
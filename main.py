from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
        "Message":"This is my first deployment project on render"
    }
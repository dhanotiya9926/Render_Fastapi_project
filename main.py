from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
        "Message":"This is my first deployment project on render"
    }
@app.get("/user")
def user():
    return {
        "name":"Abhishek dhanotiya",
        "Roll_no":"0103CA251010",
        "college":"lakshmi narain college of technology"
    }
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def app_start():
    return {"message":"Hello, FastAPI from Himanshu!"}
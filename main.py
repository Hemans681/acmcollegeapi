from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def app_start():
    return {"message":"Hello, FastAPI from Himanshu!"}




fakeUserDb = {
    "testuser":{"username": "testuser",
                "password": "secret123"}
}


class LoginRequest(BaseModel):
    username : str
    password : str


@app.post("/login")
def login(request: LoginRequest):
    userData = fakeUserDb.get(request.username)
    if not userData or userData["password"] != request.password:
        raise HTTPException(status_code =401, detail = "Invalid username and password")
    return {"message": f"welcome {request.username}"}
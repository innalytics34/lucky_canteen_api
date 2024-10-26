from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from fastapi import FastAPI, Request, Depends, HTTPException
from auth import py_jwt
from filter import py_filter
from login import py_login
import json
auth_scheme = py_jwt.JWTBearer()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "success"}


@app.post("/canteen/login")
async def login(request: Request):
    try:
        request = await request.json()
        response = py_login.login(request)
        return response
    except Exception as e:
        print(str(e))


@app.get("/canteen/get_lookup")
async def get_lookup(data: str = "{}"):
    try:
        request = json.loads(data)
        print(request, "---------")
        response = py_filter.get_lookup(request, {})
        return response
    except Exception as e:
        print(str(e))


if __name__ =="__main__":
    run(app, host='0.0.0.0', port=8065)

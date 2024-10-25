from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from fastapi import FastAPI, Request, Depends
from auth import py_jwt
from login import py_login
from register import py_register
from filter import py_filter
from dashboard import py_dashboard
import json
from azure_blob import blob_upload

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

@app.post("/task/login")
async def login(request: Request):
    try:
        request = await request.json()
        response = py_login.login(request)
        return response
    except Exception as e:
        print(str(e))


@app.post("/task/register")
async def register(request: Request):
    try:
        request = await request.json()
        print(request)
        response = py_register.employee_register(request)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/dept")
async def dept():
    try:
        response = py_filter.department()
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/main_menu")
async def main_menu(decoded=Depends(auth_scheme)):
    try:
        response = py_filter.main_menu(decoded)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_employee")
async def get_employee():
    try:
        response = py_filter.get_employee()
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_priority")
async def get_priority():
    try:
        response = py_filter.priority_list()
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_task_type")
async def get_task_type():
    try:
        response = py_filter.get_task_type()
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_status_type")
async def get_status_type():
    try:
        response = py_filter.status_type()
        return response
    except Exception as e:
        print(str(e))

@app.post("/task/insert_task")
async def insert_task(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        print(request)
        response = py_dashboard.assignments(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.get("/task/get_task")
async def get_task(decoded=Depends(auth_scheme)):
    try:
        response = py_dashboard.get_assignment(decoded)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_file")
async def get_file(data: str = '{"file_name":""}'):
    try:
        request = json.loads(data)
        response = blob_upload.getfile_azure_blob(request.get("file_name"))
        print(response)
        return response
    except Exception as e:
        print(str(e))

@app.post("/task/delete_task")
async def delete_task(request: Request):
    try:
        request = await request.json()
        response = py_dashboard.delete_task(request)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_assignee_task")
async def get_assignee_task(decoded=Depends(auth_scheme)):
    try:
        response = py_dashboard.get_assignee_assignment(decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/task/update_task")
async def update_task(request: Request):
    try:
        request = await request.json()
        response = py_dashboard.update_task(request)
        return response
    except Exception as e:
        print(str(e))

@app.post("/task/insert_assign_details")
async def insert_assign_details(request: Request):
    try:
        request = await request.json()
        print(request)
        response = py_dashboard.insert_assignment_details(request)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/get_task")
async def get_task(decoded=Depends(auth_scheme)):
    try:
        response = py_dashboard.get_assignment(decoded)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/task_count")
async def task_count(decoded: dict = Depends(auth_scheme)):
    try:
        response = py_dashboard.get_emp_task_count(decoded)
        return response
    except Exception as e:
        print(str(e))


@app.get("/task/assigner_task_count")
async def assigner_task_count(decoded: dict = Depends(auth_scheme)):
    try:
        response = py_dashboard.get_assigner_task_count(decoded)
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/super_admin_total_task_count")
async def get_super_admin_total_task_count():
    try:
        response = py_dashboard.get_super_admin_total_task_count()
        return response
    except Exception as e:
        print(str(e))

@app.get("/task/admin_total_task_count")
async def get_admin_total_task_count():
    try:
        response = py_dashboard.get_admin_total_task_count()
        return response
    except Exception as e:
        print(str(e))


if __name__ =="__main__":
    run(app, host='0.0.0.0', port=8065)

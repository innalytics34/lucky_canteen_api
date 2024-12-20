from starlette.middleware.cors import CORSMiddleware
from uvicorn import run
from fastapi import FastAPI, Request, Depends, HTTPException

from auth import py_jwt
from delete import py_delete
from fetch import py_fetch
from filter import py_filter
from login import py_login, py_dropdown
from sidebar import py_sidebar
import json

from generalMaster import py_generalMaster
from product import py_pmrm, py_pmim, py_product
from uom import py_uom
from accountM import py_accountM
from hsn import py_hsn

from transaction.purchase_order import py_purchase_order
from transaction.material_inward import py_material_inward
from transaction.menu import py_menu
from transaction.material_request import py_material_request
from transaction.material_issue import py_material_issue
from transaction.material_return import py_material_return
from transaction.rm_opening_stock import raw_material_os

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


@app.get("/canteen/get_cy")
async def get_cy():
    try:
        response = py_dropdown.cy()
        return response
    except Exception as e:
        print(str(e))


@app.get("/canteen/get_branch")
async def get_branch(data: str = '{}'):
    try:
        request = json.loads(data)
        response = py_dropdown.BranchName(request)
        return response
    except Exception as e:
        print(str(e))


@app.get("/canteen/get_username")
async def get_username(data: str = '{"branch_id": ''}'):
    try:
        request = json.loads(data)
        response = py_dropdown.UserName(request)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/login")
async def login(request: Request):
    try:
        request = await request.json()
        response = py_login.fn_login(request)
        return response
    except Exception as e:
        print(str(e))


@app.get("/canteen/get_lookup")
async def get_lookup(data: str = "{}", decoded=Depends(auth_scheme)):
    try:
        request = json.loads(data)
        response = py_filter.get_lookup(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.get("/canteen/get_sidebar")
async def get_sidebar(decoded=Depends(auth_scheme)):
    if decoded:
        try:
            response = py_sidebar.GetMenu(decoded)
            return response
        except Exception as e:
            print(str(e))
    else:
        raise HTTPException(status_code=401, detail="Invalid token or expired token.")


@app.post("/canteen/accountM")
async def accountM(request: Request):
    try:
        request = await request.json()
        decoded = {'branch_id': 100000, "user_id": 1}
        response = py_accountM.accountM(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.get("/canteen/fetch_data")
async def fetch_data(data: str = "{}", decoded=Depends(auth_scheme)):
    try:
        request = json.loads(data)
        response = py_fetch.fetch_data(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/delete_data")
async def delete_data(request: Request):
    try:
        request = await request.json()
        decoded = {'branch_id': 100000, "user_id": 1}
        response = py_delete.delete_data(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/uom_insert_update")
async def uom_insert_update(request: Request):
    try:
        request = await request.json()
        response = py_uom.uom_insert_update(request)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/add_charges_insert_update")
async def add_charges_insert_update(request: Request):
    try:
        request = await request.json()
        decoded = {'branch_id': 100000, "user_id": 1}
        response = py_product.add_charges_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/hsn_insert_update")
async def hsn_insert_update(request: Request):
    try:
        request = await request.json()
        decoded = {'branch_id': 100000, "user_id": 1}
        response = py_hsn.hsn_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/uomconversion_insert_update")
async def uomconversion_insert_update(request: Request):
    try:
        request = await request.json()
        response = py_uom.uomconversion_insert_update(request)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/pmrm_insert_update")
async def pmrm_insert_update(request: Request):
    try:
        request = await request.json()
        decoded = {'branch_id': 100000, "user_id": 1}
        response = py_pmrm.pmrm_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/pmim_insert_update")
async def pmim_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_pmim.pmim_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/generalMaster_insert_update")
async def generalMaster_insert_update(request: Request):
    try:
        request = await request.json()
        decoded = {'branch_id': 100000, "user_id": 1}
        response = py_generalMaster.generalMaster_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))


@app.post("/canteen/po_insert_update")
async def po_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_purchase_order.po_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/canteen/mi_insert_update")
async def mi_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_material_inward.mi_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/canteen/m_insert_update")
async def m_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_menu.menu(request, decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/canteen/mr_insert_update")
async def mr_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_material_request.mr_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/canteen/mai_insert_update")
async def mai_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_material_issue.mai_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/canteen/mar_insert_update")
async def mar_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = py_material_return.mar_insert_update(request, decoded)
        return response
    except Exception as e:
        print(str(e))

@app.post("/canteen/rmos_insert_update")
async def rmos_insert_update(request: Request, decoded=Depends(auth_scheme)):
    try:
        request = await request.json()
        response = raw_material_os.RawMaterialOpeningStock(request, decoded)
        return response
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    run(app, host='0.0.0.0', port=8065)

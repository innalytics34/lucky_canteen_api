from auth.py_jwt import signJWT
from db_connection import py_connection
from Crypto.Cipher import DES3
import base64
import os
import inspect
from logger.logger_config import logger

directory = os.path.dirname(os.path.abspath(__file__))


key = b'Binary--Solution'


def fn_login(request):
    try:
        print(request)
        username = request.get("username")
        encrypted_password = request.get("password")
        branch_id = request.get('branch_id')
        year = request.get('year')
        encrypted_password = encrypt_password(encrypted_password, key)
        company_id = request.get("company_id")
        company_name = request.get("company_name")
        state_code = request.get("StateCode")
        qry = '{call canteen.[bis_EmployeeDetails_Select_ByUId_PWD] (?)}'
        res, k = py_connection.call_prop1(qry, (request['emp_fk']))
        print(res)
        db_password = res[0][1]
        if db_password == encrypted_password:
            token = signJWT(username, branch_id, year, request['emp_fk'], company_id, company_name, state_code)
            return {"message": "Login successfully", "rval": 1, "token": token}
        else:
            return {"message": "Username or password is incorrect", "rval": 0, "data": [],  "token": ""}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + str(e))
        return {"message": "Something went wrong", "rval": 0}


def get_encrypt_pwd(req):
    encrypt_pwd = str(req.get("pwd"))
    res = encrypt_password(encrypt_pwd, key)
    return {"encpypt_pwd": res}


def get_decrypt_pwd(req):
    encrypt_pwd = str(req.get("pwd"))
    res = decrypt_password(encrypt_pwd, key)
    return {"decrypt_pwd": res}


def pad(data):
    padding_length = 8 - len(data) % 8
    return data + bytes([padding_length] * padding_length)


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def encrypt_password(password, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_password = pad(password.encode())
    encrypted_password = cipher.encrypt(padded_password)
    return base64.b64encode(encrypted_password).decode()


def decrypt_password(encrypted_password, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_password = base64.b64decode(encrypted_password)
    decrypted_password = cipher.decrypt(encrypted_password)
    return unpad(decrypted_password).decode()
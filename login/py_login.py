import base64

from db_connection import py_connection
from Crypto.Cipher import DES3
from auth.py_jwt import signJWT

key = b'Binary--Solution'

def login(request):
    try:
        print(request)
        username = request.get("username")
        password = request.get("password")
        # encrypted_password = encrypt_password(password,key)
        qry = ("select username,emp_fk,role_fk,dept_fk from rmsranga.Web_task_logins "
               "where username = '{0}' and password = '{1}'".format(username, password))
        print(qry)
        result, k = py_connection.get_result_col(qry)
        lst = []
        if result and len(result) > 0:
            for row in result:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            token = signJWT(result[0][0], result[0][1], result[0][2], result[0][3])
            return {"message": "Login successfully", "rval": 1, "token": token}
        else:
            return {"message": "Username or password is incorrect", "rval": 0, "token": ""}

    except Exception as e:
        print(str(e))
        return {"message": "Something went wrong", "rval": 0}


def pad(data):
    padding_length =8 -len(data) % 8
    return data + bytes([padding_length] * padding_length)


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def encrypt_password(password,key):
    cipher = DES3.new(key,DES3.MODE_ECB)
    padded_password = pad(password.encode())
    encrypt_password = cipher.encrypt(padded_password)
    return base64.b64encode(encrypt_password).decode()


def decrypt_password(encrypted_password, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_password = base64.b64decode(encrypted_password)
    decrypted_password = cipher.decrypt(encrypted_password)
    return unpad(decrypted_password).decode()
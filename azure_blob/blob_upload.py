import uuid
from db_connection import py_connection
from datetime import datetime as dt, datetime, timedelta
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import base64
import json

connection_string = ("DefaultEndpointsProtocol=https;AccountName=iecstore;AccountKey"
                     "=E52k3gjrBxRZ31swWniFzziNsj5TKrLAxEn/jranR/E+f7BFZpHOnso/tgFXKb5B0VSC09ZJHF85Ma2rsi01pw"
                     "==;EndpointSuffix=core.windows.net")
container_name = "wmpfiles"


def blob_connection():
    try:
        qry = "SELECT connection_string, container_name FROM Web_task_azure_connection"
        result = py_connection.get_result(qry)
        print(result)
        if result:
            blob_service_client = BlobServiceClient.from_connection_string(result[0][0])
            container_client = blob_service_client.get_container_client(result[0][1])
            return container_client
        else:
            raise ValueError("No Azure Blob connection details found in the database.")
    except:
        print("blob connection failed")


def upload_to_azure_blob(base64string):
    try:
        container_client = blob_connection()
        filename = str(uuid.uuid4().hex) + ".json"
        base_dir = os.getenv("FILE_PATH", "../temp_file/")
        blob_client = container_client.get_blob_client("task_file/" + filename)
        data = {'base64string': base64string}
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        with open(base_dir + filename, 'w') as f:
            json.dump(data, f)
        with open(base_dir + filename, "rb") as data:
            blob_client.upload_blob(data)
        os.remove(base_dir + filename)
        return "task_file/" + filename
    except Exception as e:
        print("Error uploading file to Azure Blob Storage:", e)


def getfile_azure_blob(blob_name):
    try:
        if blob_name and blob_name not in ['', None]:
            container_client = blob_connection()
            blob_client = container_client.get_blob_client(blob_name)
            blob_data = blob_client.download_blob().readall()
            data = json.loads(blob_data)
            return data
        else:
            return {'base64string': ''}
    except Exception as e:
        print("Error downloading file from Azure Blob Storage:", e)



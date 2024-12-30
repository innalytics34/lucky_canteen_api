from db_connection import py_connection
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))

def uom_insert_update(request):
    try:
        UID = request.get("UID")
        UOM = request.get("UOM")
        Description = request.get("Description")
        ActiveStatus = request.get("ActiveStatus")
        BaseUOM = request.get("BaseUOM")
        Factor = request.get("Factor")

        if UID not in [0, '0', '']:

            py_connection.put_result("{call Canteen.Bis_UOMMaster_Update"
                                     "(?,?,?,?,?,?)}", (UID, UOM, Description, BaseUOM, ActiveStatus, Factor))
            stat = "updated"
        else:
            res = py_connection.put_result("{call Canteen.Bis_UOMMaster_Insert"
                                           "(?,?,?,?,?,?)}", (0, UOM, Description, BaseUOM, ActiveStatus, Factor))
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("uom_insert_update " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something went wrong!", "rval": 0}


def uomconversion_insert_update(request):
    try:
        UID = request.get("UID")
        UOM_UID = request.get("UOM_UID")
        BaseUnit = request.get("BaseUnit")
        ActiveStatus = request.get("ActiveStatus")
        Factor = request.get("Factor")

        if UID not in [0, '0', '']:
            py_connection.put_result("{call Canteen.Bis_UOMConversion_Update"
                                     "(?,?,?,?,?)}", (UID, UOM_UID, BaseUnit, Factor, ActiveStatus))
            stat = "updated"
        else:
            py_connection.put_result("{call Canteen.Bis_UOMConversion_Insert"
                                     "(?,?,?,?,?)}", (0, UOM_UID, BaseUnit, Factor, ActiveStatus))
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("uom_insert_update " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something went wrong!", "rval": 0}
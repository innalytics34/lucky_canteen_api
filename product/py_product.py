from charges.py_charges import charges_insert_update, add_charges_insert
from db_connection import py_connection
from datetime import datetime as dt
import os
from logger.logger_config import logger
import inspect

directory = os.path.dirname(os.path.abspath(__file__))


def add_charges_insert_update(request, decoded):
    try:
        UID = request.get('UID')
        branch_id = decoded.get('branch_id')
        product_code = request.get('ProductCode')
        product_description = request.get('ProductDescription')
        uom_id = request.get('UOMID')
        uom_description = request.get('UOMDescription')
        charge_description = request.get('ChargeDescription')
        product_type = request.get('ProductType')
        price = request.get('Price')
        hsn_code = request.get('HSNCode')
        active_status = request.get('ActiveStatus')
        created_by = request.get('CreatedBy')
        created_on = request.get('CreatedDate')
        updated_by = request.get('UpdatedBy')
        updated_on = request.get('UpdatedDate')
        product_category = request.get('ProductCategory')

        if UID not in [0, '0', '']:
            values = (UID, branch_id, product_code, product_description, uom_id, uom_description, product_type,
                      price, hsn_code, active_status, created_by, created_on, updated_by, updated_on, product_category)
            py_connection.put_result("{call Canteen.bis_CanteenProductMaster_Update"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            stat = "updated"
            request = {"UID": UID, "ChargesDescription": charge_description, "ActiveStatus": active_status}
            charges_insert_update(request)
        else:
            values = (branch_id, product_code, product_description, uom_id, uom_description, product_type,
                      price, hsn_code, active_status, created_by, created_on, updated_by, updated_on, product_category)
            sql = """
            DECLARE @UID int;
            set nocount on;
            EXEC [Canteen].[bis_CanteenProductMaster_Insert]
                @UID OUTPUT,?,?,?,?,?,?,?,?,?,?,?,?,?,?;
            SELECT @UID;
            """
            res = py_connection.call_prop_return_pk(sql, values)
            request1 = {"UID": res, "ChargesDescription": charge_description, "ActiveStatus": active_status}
            add_charges_insert(request1)
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("uom_insert_update " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something went wrong!", "rval": 0}
from charges.py_charges import charges_insert_update
from db_connection import py_connection


def product_insert_update(request):
    try:
        UID = request.get('UID')
        branch_id = request.get('BranchId')
        product_code = request.get('ProductCode')
        product_description = request.get('ProductDescription')
        uom_id = request.get('UOMID')
        uom_description = request.get('UOMDescription')
        product_type = request.get('ProductType')
        price = request.get('Price')
        hsn_code = request.get('HSNCode')
        active_status = request.get('ActiveStatus')
        created_by = request.get('CreatedBy')
        created_on = request.get('CreatedOn')
        updated_by = request.get('UpdatedBy', None)
        updated_on = request.get('UpdatedOn', None)
        product_category = request.get('ProductCategory')

        if UID not in [0, '0', '']:
            values = (UID, branch_id, product_code, product_description, uom_id, uom_description, product_type,
                      price, hsn_code, active_status, created_by, created_on, updated_by, updated_on, product_category)
            py_connection.put_result("{call Canteen.bis_CanteenProductMaster_Update"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            stat = "updated"
            request = {"UID": UID, "ChargesDescription": '', "ActiveStatus": active_status, "BranchID": branch_id}
            charges_insert_update(request)
        else:
            values = (UID, branch_id, product_code, product_description, uom_id, uom_description, product_type,
                      price, hsn_code, active_status, created_by, created_on, updated_by, updated_on, product_category)
            py_connection.put_result("{call Canteen.bis_CanteenProductMaster_Insert"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            request = {"UID": UID, "ChargesDescription": '', "ActiveStatus": active_status, "BranchID": branch_id}
            charges_insert_update(request)
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("uom_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}
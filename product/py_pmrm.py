from db_connection import py_connection
from product.PRMI_config import product_master, raw_material


def pmrm_insert_update(request, decoded):
    try:
        print(request, "-------fg")
        UID = request.get("UID")
        ProductMasterXML = product_master(request.get("purchase_master"), decoded)
        RawMaterialMaster = raw_material(request.get("raw_material"))
        ProductCode = request.get("ProductCode")

        if UID not in ['', 0, '0']:
            values = (ProductMasterXML, RawMaterialMaster, UID, 0)
            py_connection.put_result("{call Canteen.Bis_ProductMaster_RawMaterialMasters"
                                     "(?,?,?,?)}", values)
            stat = "updated"
        else:
            values = (ProductMasterXML, RawMaterialMaster, ProductCode, 0)
            py_connection.put_result("{call Canteen.Bis_ProductMaster_RawMaterialMaster"
                                 "(?,?,?,?)}", values)
            stat = "inserted"
        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("pmrm_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}



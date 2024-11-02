from db_connection import py_connection
from product.PRMI_config import product_master, item_master


def pmim_insert_update(request, decoded):
    try:
        UID = request.get("UID")
        ProductMasterXML = product_master(request.get("purchase_master"), decoded)
        ItemMaster = item_master(request.get("item_master"))
        ProductCode = request.get("ProductCode")

        if UID not in ['', 0, '0']:
            values = (ProductMasterXML, ItemMaster, UID, 0)
            py_connection.put_result("{call Canteen.Bis_ProductMaster_ItemMaster"
                                     "(?,?,?,?,?,?)}", values)
            stat = "updated"
        else:
            values = (ProductMasterXML, ItemMaster, ProductCode, 0)
            py_connection.put_result("{call Canteen.Bis_ProductMaster_ItemMasters"
                                 "(?,?,?,?,?,?)}", values)
            stat = "inserted"
        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("pmim_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}



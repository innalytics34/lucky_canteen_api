from db_connection import py_connection
from product.PRMI_config import product_master, item_master, item_master_list


def pmim_insert_update(request, decoded):
    try:
        UID = request.get("UID")
        ProductMasterXML = product_master(request.get("purchase_master"), decoded)
        ItemMaster = item_master(request.get("item_master"))
        ProductCode = request.get("ProductCode")
        itemListInsert, itemListUpdate = find_new_record(request.get("item_master_list"))
        itemListinsertXML = item_master_list(itemListInsert, decoded)
        itemListupdateXML = item_master_list(itemListUpdate, decoded)

        if UID not in ['', 0, '0']:
            values = (ProductMasterXML, ItemMaster, itemListinsertXML, itemListupdateXML, UID, 0)
            py_connection.put_result("{call Canteen.Bis_ProductMaster_ItemMasters"
                                     "(?,?,?,?,?,?)}", values)
            stat = "updated"
        else:
            values = (ProductMasterXML, ItemMaster, itemListinsertXML, itemListupdateXML,  ProductCode, 0)
            py_connection.put_result("{call Canteen.Bis_ProductMaster_ItemMaster"
                                 "(?,?,?,?,?,?)}", values)
            stat = "inserted"
        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("pmim_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}


def find_new_record(itemlist):
    itemListInsert = [entry for entry in itemlist if entry["UID"] == 0]
    itemListUpdate = [entry for entry in itemlist if entry["UID"] != 0]
    return (itemListInsert if len(itemListInsert) else '',
            itemListUpdate if len(itemListUpdate) else '',)

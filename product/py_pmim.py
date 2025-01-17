from db_connection import py_connection
from product.PRMI_config import product_master, item_master, item_master_list
import os
from logger.logger_config import logger
import inspect

directory = os.path.dirname(os.path.abspath(__file__))

def pmim_insert_update(request, decoded):
    try:
        UID = request.get("UID")
        ProductCode = request.get("ProductCode")
        ProductMasterXML = product_master(request.get("purchase_master"), decoded, ProductCode)
        ItemMaster = item_master(request.get("item_master"))
        itemListInsert, itemListUpdate = find_new_record(request.get("item_master_list"))

        element_name = 'ItemMasterList'
        itemListinsertXML = item_master_list(itemListInsert, decoded, element_name)
        itemListupdateXML = item_master_list(itemListUpdate, decoded, element_name)
        if UID not in ['', 0, '0']:
            qry = """ 
                    DECLARE @return_value int, 
                    @successful bit
                    SET NOCOUNT ON; 

                    EXEC @return_value = [Canteen].[Bis_ProductMaster_ItemMasters]
                    @ProductMasterInsert = ?, 
                    @ItemMasterInsert = ?,
                    @ItemMasterListInsert = ?, 
                    @ItemMasterListUpdate = ?,
                    @UID = ?,
                    @successful = @successful OUTPUT

                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """

            values = (ProductMasterXML, ItemMaster, itemListinsertXML, itemListupdateXML, UID)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Item Master Details Updated Successfully", "rval": 1}
            else:
                return {"message": "Item Master Updation Failed", "rval": 0}

        else:
            qry = """
                    DECLARE @return_value int, 
                    @successful bit
                    SET NOCOUNT ON; 

                    EXEC @return_value = [Canteen].[Bis_ProductMaster_ItemMaster]
                    @ProductMasterInsert = ?, 
                    @ItemMasterInsert = ?,
                    @ItemMasterListInsert = ?, 
                    @ItemMasterListUpdate = ?,
                    @ProductCode = ?,
                    @successful = @successful OUTPUT

                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """
            values = (ProductMasterXML, ItemMaster, itemListinsertXML, itemListupdateXML,  ProductCode)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Item Master Details Inserted Successfully", "rval": 1}
            else:
                return {"message": "Item Master Insertion Failed", "rval": 0}
    except Exception as e:
        print("pmim_insert_update " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something went wrong!", "rval": 0}


def find_new_record(itemlist):
    itemListInsert = [entry for entry in itemlist if entry["UID"] == 0]
    itemListUpdate = [entry for entry in itemlist if entry["UID"] != 0]
    return (itemListInsert if len(itemListInsert) else '',
            itemListUpdate if len(itemListUpdate) else '',)

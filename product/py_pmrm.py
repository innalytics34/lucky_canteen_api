from db_connection import py_connection
from product.PRMI_config import product_master, raw_material


def pmrm_insert_update(request, decoded):
    try:
        print(request, "-------fg")
        UID = request.get("UID")
        ProductCode = request.get("ProductCode")
        ProductMasterXML = product_master(request.get("purchase_master"), decoded, ProductCode)
        RawMaterialMaster = raw_material(request.get("raw_material"), ProductCode)

        if UID not in ['', 0, '0']:
            qry = """ 
                    DECLARE @return_value int, 
                    @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[Bis_ProductMaster_RawMaterialMasters]
                    @ProductMasterInsert = ?, 
                    @RawMaterialMasterInsert = ?,
                    @UID = ?,
                    @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """
            values = (ProductMasterXML, RawMaterialMaster, UID)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Raw Material Master Updated Successfully", "rval": 1}
            else:
                return {"message": "Raw Material Master Updation Failed", "rval": 0}
        else:
            qry = """ 
                    DECLARE @return_value int, 
                    @successful bit
                    SET NOCOUNT ON; 

                    EXEC @return_value = [Canteen].[Bis_ProductMaster_RawMaterialMaster]
                    @ProductMasterInsert = ?, 
                    @RawMaterialMasterInsert = ?,
                    @ProductCode = ?,
                    @successful = @successful OUTPUT

                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """

            values = (ProductMasterXML, RawMaterialMaster, ProductCode)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Raw Material Master Inserted Successfully", "rval": 1}
            else:
                return {"message": "Raw Material Master Insertion Failed", "rval": 0}
    except Exception as e:
        print("pmrm_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}



from db_connection import py_connection
from transaction.material_return.mar_config import material_return_xml, material_return_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year

def mar_insert_update(request, decoded):  # 80700

    UID = request.get("UID")

    CanteenMaterialReturnXML = material_return_xml(request['material_return'], decoded)
    print(CanteenMaterialReturnXML, '000')

    CanteenMaterialReturnListInsertXML, CanteenMaterialReturnListUpdateXML = find_new_record(request['mar_list'])

    element_lst = 'CanteenMaterialReturnList'
    i_CanteenMaterialReturnListXML = material_return_list_xml(CanteenMaterialReturnListInsertXML, decoded, element_lst)
    print(i_CanteenMaterialReturnListXML, '111')

    element_lsts = 'CanteenMaterialReturnLists'
    u_CanteenMaterialReturnListXML = material_return_list_xml(CanteenMaterialReturnListUpdateXML, decoded, element_lsts)
    print(u_CanteenMaterialReturnListXML, '222')

    if UID not in ['', 0, '0']:
        qry = """ 
                DECLARE @return_value int, @successful bit
                SET NOCOUNT ON; 

                EXEC @return_value = [Canteen].[bis_CanteenMaterialReturn_Update]
                @CanteenmaterialReturnInsert = ?,
                @CanteenmaterialReturnListInsert = ?,
                @CanteenmaterialReturnListUpdate = ?,
                @UID = ?,
                @successful = @successful OUTPUT

                SELECT @successful as N'@successful'
                SELECT 'Return Value' = @return_value
             """

        values = (CanteenMaterialReturnXML, i_CanteenMaterialReturnListXML, u_CanteenMaterialReturnListXML,
                  UID)
        res = py_connection.call_prop_return_pk1(qry, values)
        if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
            return {"message": "Material Return Details Updated Successfully", "rval": 1}
        else:
            return {"message": "Material Return Updation Failed", "rval": 0}
    else:
        qry = """ 
                DECLARE @return_value int, @successful bit
                SET NOCOUNT ON; 

                EXEC @return_value = [Canteen].[bis_CanteenMaterialReturn_Insert]
                @CanteenmaterialReturnInsert = ?, 
                @CanteenmaterialReturnListInsert = ?, 
                @DocumetTypeId = ?, 
                @Branch_ID = ?, 
                @Year = ?, 
                @DocumentDate = ?, @successful = @successful OUTPUT

                SELECT @successful as N'@successful'
                SELECT 'Return Value' = @return_value
             """

        values = (CanteenMaterialReturnXML, i_CanteenMaterialReturnListXML,
                  80700, decoded['branch_id'], Year()[0]["Yr"], dt.now())
        res = py_connection.call_prop_return_pk1(qry, values)

        if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
            return {"message": "Material Return Details Inserted Successfully", "rval": 1}
        else:
            return {"message": "Material Return Insertion Failed", "rval": 0}


def find_new_record(mar_list):
    MaterialReturnListInsert = [entry for entry in mar_list if entry["UID"] == 0]
    MaterialReturnListUpdate = [entry for entry in mar_list if entry["UID"] != 0]

    return (MaterialReturnListInsert if len(MaterialReturnListInsert) else '',
            MaterialReturnListUpdate)
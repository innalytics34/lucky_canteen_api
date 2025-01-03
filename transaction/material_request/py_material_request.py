from db_connection import py_connection
from transaction.material_request.mr_config import (material_request_xml, material_request_list_xml,
                                                   material_request_details_xml)
from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))


def mr_insert_update(request, decoded):  # 80500
    try:
        UID = request.get("UID")

        CanteenMaterialRequestXML = material_request_xml(request['material_request'], decoded)


        (CanteenMaterialRequestListInsertXML, CanteenMaterialRequestListUpdateXML, CanteenMaterialRequestDetailsInsertXML,
         CanteenMaterialRequestDetailsUpdateXML) = find_new_record(request['mr_list'], request['mr_details'])

        element_lst = 'CanteenMaterialRequestList'
        i_CanteenMaterialRequestListXML = material_request_list_xml(CanteenMaterialRequestListInsertXML, decoded, element_lst)


        element_lsts = 'CanteenMaterialRequestLists'
        u_CanteenMaterialRequestListXML = material_request_list_xml(CanteenMaterialRequestListUpdateXML, decoded, element_lsts)


        element_chg = 'CanteenMaterialRequestDetails'
        i_CanteenMaterialRequestDetailsXML = material_request_details_xml(CanteenMaterialRequestDetailsInsertXML, decoded,
                                                                          element_chg)

        element_chgs = 'CanteenMaterialRequestDetailss'
        u_CanteenMaterialRequestDetailsXML = material_request_details_xml(CanteenMaterialRequestDetailsUpdateXML, decoded,
                                                                          element_chgs)


        if UID not in ['', 0, '0']:
            qry = """ 
                    DECLARE @return_value int, @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[bis_CanteenMaterialRequest_Update]
                    @CanteenMaterialRequestInsert = ?, 
                    @CanteenMaterialRequestListInsert = ?,
                    @CanteenMaterialRequestListUpdate = ?, 
                    @CanteenMaterialRequestDetailsInsert = ?,
                    @CanteenMaterialRequestDetailsUpdate =?, 
                    @UID = ?,
                    @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                 """

            values = (CanteenMaterialRequestXML, i_CanteenMaterialRequestListXML, u_CanteenMaterialRequestListXML,
                      i_CanteenMaterialRequestDetailsXML, u_CanteenMaterialRequestDetailsXML, UID)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Material Request Details Updated Successfully", "rval": 1}
            else:
                return {"message": "Material Request Updation Failed", "rval": 0}
        else:
            qry = """ 
                    DECLARE @return_value int, @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[bis_CanteenMaterialRequest_Insert]
                    @CanteenMaterialRequestInsert = ?, 
                    @CanteenMaterialRequestListInsert = ?, 
                    @CanteenMaterialRequestDetailsInsert = ?, 
                    @DocumetTypeId = ?, 
                    @Branch_ID = ?, 
                    @Year = ?, 
                    @DocumentDate = ?, @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                 """
            values = (CanteenMaterialRequestXML, i_CanteenMaterialRequestListXML, i_CanteenMaterialRequestDetailsXML,
                      80500, 100000, Year()[0]["Yr"], dt.now())
            res = py_connection.call_prop_return_pk1(qry, values)

            if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
                return {"message": "Material Request Details Inserted Successfully", "rval": 1}
            else:
                return {"message": "Material Request Insertion Failed", "rval": 0}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something Went Wrong", "rval": 0}


def find_new_record(mr_list, mr_details):
    MaterialRequestListInsert = [entry for entry in mr_list if entry["UID"] == 0]
    MaterialRequestListUpdate = [entry for entry in mr_list if entry["UID"] != 0]
    MaterialRequestDetailsInsert = [entry for entry in mr_details if entry["UID"] == 0]
    MaterialRequestDetailsUpdate = [entry for entry in mr_details if entry["UID"] != 0]

    return (MaterialRequestListInsert if len(MaterialRequestListInsert) else '',
            MaterialRequestListUpdate, MaterialRequestDetailsInsert if len(MaterialRequestDetailsInsert) else '',
            MaterialRequestDetailsUpdate)
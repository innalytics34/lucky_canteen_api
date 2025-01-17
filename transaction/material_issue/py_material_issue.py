from db_connection import py_connection
from transaction.material_issue.mi_config import material_issue_xml, material_issue_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))


def mai_insert_update(request, decoded):  # 80600
    try:
        UID = request.get("UID")

        CanteenMaterialIssueXML = material_issue_xml(request['material_issue'], decoded)


        CanteenMaterialIssueListInsertXML, CanteenMaterialIssueListUpdateXML = find_new_record(request['mai_list'])

        element_lst = 'CanteenMaterialIssueList'
        i_CanteenMaterialIssueListXML = material_issue_list_xml(CanteenMaterialIssueListInsertXML, decoded, element_lst)


        element_lsts = 'CanteenMaterialIssueLists'
        u_CanteenMaterialIssueListXML = material_issue_list_xml(CanteenMaterialIssueListUpdateXML, decoded, element_lsts)


        if UID not in ['', 0, '0']:
            qry = """ 
                    DECLARE @return_value int, @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[bis_CanteenMaterialIssue_Update]
                    @CanteenMaterialIssueInsert = ?, 
                    @CanteenMaterialIssueListInsert = ?,
                    @CanteenMaterialIssueListUpdate = ?,
                    @UID = ?,
                    @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """

            values = (CanteenMaterialIssueXML, i_CanteenMaterialIssueListXML, u_CanteenMaterialIssueListXML, UID)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Material Issue Details Updated Successfully", "rval": 1}
            else:
                return {"message": "Material Issue Updation Failed", "rval": 0}
        else:
            qry = """ 
                    DECLARE @return_value int, @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[bis_CanteenMaterialIssue_Insert]
                    @CanteenMaterialIssueInsert = ?,
                    @CanteenMaterialIssueListInsert = ?,
                    @DocumetTypeId = ?,
                    @Branch_ID = ?, 
                    @Year= ?, 
                    @DocumentDate = ?,
                    @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                 """
            values = (CanteenMaterialIssueXML, i_CanteenMaterialIssueListXML, 80600, decoded['branch_id'],
                      Year()[0]["Yr"], dt.now())
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
                return {"message": "Material Issue Details Inserted Successfully", "rval": 1}
            else:
                return {"message": "Material Issue Insertion Failed", "rval": 0}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something went Wrong", "rval": 0}



def find_new_record(mai_list):
    MaterialIssueListInsert = [entry for entry in mai_list if entry["UID"] == 0]
    MaterialIssueListUpdate = [entry for entry in mai_list if entry["UID"] != 0]

    return (MaterialIssueListInsert if len(MaterialIssueListInsert) else '',
            MaterialIssueListUpdate)
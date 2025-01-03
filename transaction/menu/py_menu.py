import os
from db_connection import py_connection
from transaction.menu.m_config import menu_xml, menu_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect

directory = os.path.dirname(os.path.abspath(__file__))


def menu(request, decoded):
    try:
        UID = request.get("UID")

        CanteenMenuXML = menu_xml(request['menu'], decoded)

        CanteenMenuXMLListInsertXML, CanteenMenuXMLListUpdateXML = find_new_record(request['menu_list'])

        element_lst = 'CanteenMenuList'
        i_CanteenMenuXMLListInsertXML = menu_list_xml(CanteenMenuXMLListInsertXML, decoded, element_lst)


        element_lsts = 'CanteenMenuLists'
        u_CanteenMenuXMLListUpdateXML = menu_list_xml(CanteenMenuXMLListUpdateXML, decoded, element_lsts)

        if UID not in ['', 0, '0']:
            qry = """ 
                    DECLARE @return_value int, 
                            @successful bit, 
                            @DecUID int
                    SET NOCOUNT ON; 

                    EXEC @return_value = [Canteen].[bis_CanteenMenu_Update]
                    @CanteenMenuInsert = ?,
                    @CanteenMenuListInsert = ?,
                    @CanteenMenuListUpdate = ?, 
                    @UID = ?,
                    @successful = @successful OUTPUT

                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """

            values = (CanteenMenuXML, i_CanteenMenuXMLListInsertXML, u_CanteenMenuXMLListUpdateXML, UID)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Canteen Menu Updated Successfully", "rval": 1}
            else:
                return {"message": "Canteen Menu Updated Failed", "rval": 0}

        else:
            qry = """ 
                DECLARE @return_value int, @successful bit, @DecUID int
                SET NOCOUNT ON; 
    
                EXEC @return_value = [Canteen].[bis_CanteenMenu_Insert]
                @CanteenMenuInsert = ?, 
                @CanteenMenuListInsert = ?, 
                @DocumetTypeId = ?, 
                @Branch_ID = ?, 
                @Year = ?, 
                @DocumentDate = ?, 
                @successful = @successful OUTPUT
    
                SELECT @successful as N'@successful'
                SELECT 'Return Value' = @return_value
            """

            values = (CanteenMenuXML, i_CanteenMenuXMLListInsertXML, 80400, decoded["branch_id"], Year()[0]["Yr"], dt.now())
            res = py_connection.call_prop_return_pk1(qry, values)

            if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
                return {"message": "Canteen Menu Inserted Successfully", "rval": 1}
            else:
                return {"message": "Canteen Menu Insertion Failed", "rval": 0}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': '+ str(e))
        return {"message": "Something Went Wrong", "rval": 0}


def find_new_record(menu_list):
    MaterialInwardListInsert = [entry for entry in menu_list if entry["UID"] == 0]
    MaterialInwardListUpdate = [entry for entry in menu_list if entry["UID"] != 0]

    return (MaterialInwardListInsert if len(MaterialInwardListInsert) else '',
            MaterialInwardListUpdate)

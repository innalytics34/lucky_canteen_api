from db_connection import py_connection
from transaction.material_inward.mi_config import (material_inward_xml, material_inward_list_xml,
                                                   material_inward_charges_xml, material_inward_terms_xml)
from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))

def mi_insert_update(request, decoded):
    try:
        UID = request.get("UID")

        CanteenMaterialInwardXML = material_inward_xml(request['material_inward'], decoded)


        (CanteenMaterialInwardListInsertXML, CanteenMaterialInwardListUpdateXML, CanteenMaterialInwardChargesInsertXML,
         CanteenMaterialInwardChargesUpdateXML, CanteenMaterialInwardTermsInsertXML, CanteenMaterialInwardTermsUpdateXML)= \
            (find_new_record(request['mi_list'], request['mi_charges'], request['mi_items']))

        element_lst = 'CanteenMaterialInwardList'
        i_CanteenMaterialInwardListXML = material_inward_list_xml(CanteenMaterialInwardListInsertXML, decoded, element_lst)


        element_lsts = 'CanteenMaterialInwardLists'
        u_CanteenMaterialInwardListXML = material_inward_list_xml(CanteenMaterialInwardListUpdateXML, decoded, element_lsts)


        element_chg = 'CanteenMaterialInwardCharges'
        i_CanteenMaterialInwardChargesXML = material_inward_charges_xml(CanteenMaterialInwardChargesInsertXML, decoded,
                                                                        element_chg)


        element_chgs = 'CanteenMaterialInwardChargess'
        u_CanteenMaterialInwardChargesXML = material_inward_charges_xml(CanteenMaterialInwardChargesUpdateXML, decoded,
                                                                        element_chgs)


        element_trm = 'CanteenMaterialInwardTerms'
        i_CanteenMaterialInwardtermsXML = material_inward_terms_xml(CanteenMaterialInwardTermsInsertXML, decoded, element_trm)



        element_trms = 'CanteenMaterialInwardTermss'
        u_CanteenMaterialInwardtermsXML = material_inward_terms_xml(CanteenMaterialInwardTermsUpdateXML, decoded,
                                                                    element_trms)


        if UID not in ['', 0, '0']:
            qry = """ 
                    DECLARE @return_value int, @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[bis_CanteenMaterialInward_Update]
                    @CanteenMaterialInwardInsert = ?, 
                    @CanteenMaterialInwardListInsert = ?,
                    @CanteenMaterialInwardListUpdate = ?, 
                    @CanteenMaterialInwardChargesInsert = ?,
                    @CanteenMaterialInwardChargesUpdate =?, 
                    @CanteenMaterialInwardTermsInsert = ?,
                    @CanteenMaterialInwardTermsUpdate = ?, 
                    @UID = ?,
                    @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                """

            values = (CanteenMaterialInwardXML, i_CanteenMaterialInwardListXML, u_CanteenMaterialInwardListXML,
                      i_CanteenMaterialInwardChargesXML, u_CanteenMaterialInwardChargesXML, i_CanteenMaterialInwardtermsXML,
                      u_CanteenMaterialInwardtermsXML, UID)
            res = py_connection.call_prop_return_pk1(qry, values)
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Material Inward Details Updated Successfully", "rval": 1}
            else:
                return {"message": "Material Inward Updation Failed", "rval": 0}
        else:
            qry = """ 
                    DECLARE @return_value int, @successful bit
                    SET NOCOUNT ON; 
    
                    EXEC @return_value = [Canteen].[bis_CanteenMaterialInward_Insert]
                    @CanteenMaterialInwardInsert = ?, 
                    @CanteenMaterialInwardListInsert = ?, 
                    @CanteenMaterialInwardChargesInsert = ?,
                    @CanteenMaterialInwardTermsInsert = ?,
                    @DocumetTypeId = ?, 
                    @Branch_ID = ?, 
                    @Year = ?, 
                    @DocumentDate = ?, 
                    @successful = @successful OUTPUT
    
                    SELECT @successful as N'@successful'
                    SELECT 'Return Value' = @return_value
                 """

            values = (CanteenMaterialInwardXML, i_CanteenMaterialInwardListXML, i_CanteenMaterialInwardChargesXML,
                      i_CanteenMaterialInwardtermsXML, 80300, decoded['branch_id'], Year()[0]["Yr"], dt.now())
            res = py_connection.call_prop_return_pk1(qry, values)

            if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
                return {"message": "Material Inward Details Inserted Successfully", "rval": 1}
            else:
                return {"message": "Material Inward Insertion Failed", "rval": 0}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"message": "Something went Wrong", "rval": 0}

def find_new_record(mi_list, mi_charges, mi_terms):
    MaterialInwardListInsert = [entry for entry in mi_list if entry["UID"] == 0]
    MaterialInwardListUpdate = [entry for entry in mi_list if entry["UID"] != 0]
    MaterialInwardChargesInsert = [entry for entry in mi_charges if entry["UID"] == 0]
    MaterialInwardChargesUpdate = [entry for entry in mi_charges if entry["UID"] != 0]
    MaterialInwardTermsInsert = [entry for entry in mi_terms if entry["UID"] == 0]
    MaterialInwardTermsUpdate = [entry for entry in mi_terms if entry["UID"] != 0]

    return (MaterialInwardListInsert if len(MaterialInwardListInsert) else '',
            MaterialInwardListUpdate, MaterialInwardChargesInsert if len(MaterialInwardChargesInsert) else '',
            MaterialInwardChargesUpdate, MaterialInwardTermsInsert if len(MaterialInwardTermsInsert) else '',
            MaterialInwardTermsUpdate)
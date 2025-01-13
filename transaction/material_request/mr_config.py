from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))


def material_request_xml(data, decoded):
    try:
        print(decoded, 'q-q0q')
        xml_data = '<CanteenMaterialRequest>'
        for row in data:
            xml_data += (
                f'<CanteenMaterialRequest '
                f'UID="{row["UID"]}" '
                f'LogonUser="{decoded["user_id"]}" '
                f'BranchID="{decoded["branch_id"]}" '
                f'DocumentTypeID="{row["DocumentTypeID"]}" '
                f'Year="{Year()[0]["Yr"]}" '
                f'LongDocumentNo="{row["LongDocumentNo"]}" '
                f'DocumentDate="{row["DocumentDate"]}" '
                f'ReferenceTransID="{row["ReferenceTransID"]}" '
                f'ReferenceNo="{row["ReferenceNo"]}" '
                f'ReferenceDate="{row["ReferenceDate"]}" '
                f'MealsTypeID="{row["MealsTypeID"]}" '
                f'MealsType="{row["MealsType"]}" '
                f'TypeID="{row["TypeID"]}" '
                f'Type="{row["Type"]}" '
                f'TotalMembers="{row["TotalMembers"]}" '
                f'Status="{row["Status"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'RejectReason="{row["RejectReason"]}" '
                f'Remarks="{row["Remarks"]}" '
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" '
                f'ADDD1="{row["ADDD1"]}" '   # decimal
                f'ADDD2="{row["ADDD2"]}" '
                f'ADDD3="{row["ADDD3"]}" '
                f'ADDD4="{row["ADDD4"]}" '
                f'ADDD5="{row["ADDD5"]}" '
                f'ADDI1="{row["ADDI1"]}" '   # int
                f'ADDI2="{row["ADDI2"]}" '
                f'ADDI3="{row["ADDI3"]}" '
                f'ADDI4="{row["ADDI4"]}" '
                f'ADDI5="{row["ADDI5"]}" '
                f'ADDT1="{row["ADDT1"]}" '  # varchar
                f'ADDT2="{row["ADDT2"]}" '
                f'ADDT3="{row["ADDT3"]}" '
                f'ADDT4="{row["ADDT4"]}" '
                f'ADDT5="{row["ADDT5"]}" '
                f'ADDDT1="{row["ADDDT1"]}" '  # datetime
                f'ADDDT2="{row["ADDDT2"]}" '
                f'ADDDT3="{row["ADDDT3"]}" '
                f'ADDDT4="{row["ADDDT4"]}" '
                f'ADDDT5="{row["ADDDT5"]}" />'
            )
        xml_data += '</CanteenMaterialRequest>'
        return xml_data

    except Exception as e:
        print("Error in material_request_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def material_request_list_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMaterialRequestID="{row["CanteenMaterialRequestID"]}" '
                f'ReferenceTransID="{row["ReferenceTransID"]}" '
                f'ReferenceTransListID="{row["ReferenceTransListID"]}" '
                f'ReferenceTransNo="{row["ReferenceTransNo"]}" '
                f'ItemID="{row["ItemID"]}" '
                f'ItemDescription="{row["ItemDescription"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'UomDescription="{row["UomDescription"]}" '
                f'BaseUOMID="{row["BaseUOMID"]}" '
                f'BaseUomDescription="{row["BaseUomDescription"]}" '
                f'BaseUOMQty="{row["BaseUOMQty"]}" '
                f'Qty="{row["Qty"]}" '
                f'Status="{row["Status"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" '
                f'ADDD1="{row["ADDD1"]}" '  # decimal
                f'ADDD2="{row["ADDD2"]}" '
                f'ADDD3="{row["ADDD3"]}" '
                f'ADDD4="{row["ADDD4"]}" '
                f'ADDD5="{row["ADDD5"]}" '
                f'ADDI1="{row["ADDI1"]}" '  # int
                f'ADDI2="{row["ADDI2"]}" '
                f'ADDI3="{row["ADDI3"]}" '
                f'ADDI4="{row["ADDI4"]}" '
                f'ADDI5="{row["ADDI5"]}" '
                f'ADDT1="{row["ADDT1"]}" '  # varchar
                f'ADDT2="{row["ADDT2"]}" '
                f'ADDT3="{row["ADDT3"]}" '
                f'ADDT4="{row["ADDT4"]}" '
                f'ADDT5="{row["ADDT5"]}" '
                f'ADDDT1="{row["ADDDT1"]}" '  # datetime
                f'ADDDT2="{row["ADDDT2"]}" '
                f'ADDDT3="{row["ADDDT3"]}" '
                f'ADDDT4="{row["ADDDT4"]}" '
                f'ADDDT5="{row["ADDDT5"]}"  />'
                            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in material_request_list_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def material_request_details_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMaterialRequestID="{row["CanteenMaterialRequestID"]}" '
                f'ItemID="{row["ItemID"]}" '
                f'ItemDescription="{row["ItemDescription"]}" '
                f'RawMaterialID="{row["RawMaterialID"]}" '
                f'RawMaterialDescription="{row["RawMaterialDescription"]}" '
                f'ItemTypeID="{row["ItemTypeID"]}" '
                f'ItemType="{row["ItemType"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'UOMDescription="{row["UOMDescription"]}" '
                f'Qty="{row["Qty"]}" '
                f'BaseUOMID="{row["BaseUOMID"]}" '
                f'BaseUOM="{row["BaseUOM"]}" '
                f'BaseUOMQty="{row["BaseUOMQty"]}" '
                f'TotalQty="{row["TotalQty"]}" '
                f'RequestQty="{row["RequestQty"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" '
                f'ADDD1="{row["ADDD1"]}" '  # decimal
                f'ADDD2="{row["ADDD2"]}" '
                f'ADDD3="{row["ADDD3"]}" '
                f'ADDD4="{row["ADDD4"]}" '
                f'ADDD5="{row["ADDD5"]}" '
                f'ADDI1="{row["ADDI1"]}" '  # int
                f'ADDI2="{row["ADDI2"]}" '
                f'ADDI3="{row["ADDI3"]}" '
                f'ADDI4="{row["ADDI4"]}" '
                f'ADDI5="{row["ADDI5"]}" '
                f'ADDT1="{row["ADDT1"]}" '  # varchar
                f'ADDT2="{row["ADDT2"]}" '
                f'ADDT3="{row["ADDT3"]}" '
                f'ADDT4="{row["ADDT4"]}" '
                f'ADDT5="{row["ADDT5"]}" '
                f'ADDDT1="{row["ADDDT1"]}" '  # datetime
                f'ADDDT2="{row["ADDDT2"]}" '
                f'ADDDT3="{row["ADDDT3"]}" '
                f'ADDDT4="{row["ADDDT4"]}" '
                f'ADDDT5="{row["ADDDT5"]}"  />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in material_request_details_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None
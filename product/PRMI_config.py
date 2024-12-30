from datetime import datetime as dt
import os
from logger.logger_config import logger
import inspect

directory = os.path.dirname(os.path.abspath(__file__))

def product_master(data, decoded, product_code):
    try:
        xml_data = '<CanteenProductMaster>'
        for row in data:
            xml_data += (
                '<CanteenProductMaster '
                f'UID="{row.get("UID", 0)}" '
                f'BranchId="{decoded.get("branch_id", "")}" '
                f'ProductCode="{product_code}" '
                f'ProductDescription="{row.get("ProductDescription", "")}" '
                f'UOMID="{row.get("UOMID", "")}" '
                f'UOMDescription="{row.get("UOMDescription", "")}" '
                f'ProductType="{row.get("ProductType", "")}" '
                f'Price="{row.get("Price", "")}" '
                f'HSNCode="{row.get("HSNCode", "")}" '
                f'ActiveStatus="{row.get("ActiveStatus", "")}" '
                f'CreatedBy="{decoded.get("user_id", "")}" '
                f'CreatedOn="{dt.now()}" '
                f'UpdatedBy="{decoded.get("user_id", "")}" '
                f'UpdatedOn="{dt.now()}" '
                f'ProductCategory="{row.get("ProductCategory", "")}" />'
            )
        xml_data += '</CanteenProductMaster>'
        return xml_data
    except Exception as e:
        print("product_master " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))


def raw_material(data, product_code):
    try:
        xml_data = '<RawMaterialMaster>'
        for row in data:
            xml_data += (
                '<RawMaterialMaster '
                f'UID="{row.get("UID", "")}" '
                f'PartNo="{row.get("PartNo", "")}" '
                f'ItemCode="{product_code}" '
                f'ItemDescription="{row.get("ItemDescription", "")}" '
                f'ItemTypeID="{row.get("ItemTypeID", "")}" '
                f'ItemType="{row.get("ItemType", "")}" '
                f'Status="{row.get("Status", "")}" '
                f'ADDD1="{0}" '
                f'ADDD2="{0}" '
                f'ADDD3="{0}" '
                f'ADDD4="{0}" '
                f'ADDD5="{0}" '
                f'ADDI1="{0}" '
                f'ADDI2="{0}" '
                f'ADDI3="{0}" '
                f'ADDI4="{0}" '
                f'ADDI5="{0}" '
                f'ADDT1="" '
                f'ADDT2="" '
                f'ADDT3="" '
                f'ADDT4="" '
                f'ADDT5="" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                f'ADDDT5="{dt.now()}" />'
            )
        xml_data += '</RawMaterialMaster>'
        return xml_data
    except Exception as e:
        print("raw_material " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))


def item_master(data):
    try:
        xml_data = '<ItemMaster>\n'
        for row in data:
            xml_data += (
                '    <ItemMaster '
                f'UID="{row.get("UID", 0)}" '
                f'PartNo="{row.get("PartNo", "")}" '
                f'ItemCode="{row.get("ItemCode", "")}" '
                f'ItemDescription="{row.get("ItemDescription", "")}" '
                f'Qty="{row.get("Qty", "")}" '
                f'Status="{row.get("Status", "")}" '
                f'ADDD1="{0}" '
                f'ADDD2="{0}" '
                f'ADDD3="{0}" '
                f'ADDD4="{0}" '
                f'ADDD5="{0}" '
                f'ADDI1="{0}" '
                f'ADDI2="{0}" '
                f'ADDI3="{0}" '
                f'ADDI4="{0}" '
                f'ADDI5="{0}" '
                f'ADDT1="" '
                f'ADDT2="" '
                f'ADDT3="" '
                f'ADDT4="" '
                f'ADDT5="" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                f'ADDDT5="{dt.now()}" '
                '/>\n'
            )
        xml_data += '</ItemMaster>'
        return xml_data
    except Exception as e:
        print("item_master " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))

def item_master_list(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'ItemMasterID="{row["ItemMasterID"]}" '
                f'RawMaterialID="{row["RawMaterialID"]}" '
                f'RawMaterialDescription="{row["RawMaterialDescription"]}" '
                f'PartNo="{row["PartNo"]}" '
                f'ItemTypeID="{row["ItemTypeID"]}" '
                f'ItemType="{row["ItemType"]}" '
                f'UOM="{row["UOM"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'BaseUOMID="{row["BaseUOMID"]}" '
                f'BaseUOM="{row["BaseUOM"]}" '
                f'BaseUOMQty="{row["BaseUOMQty"]}" '
                f'Qty="{row["Qty"]}" '
                f'TotalQty="{row["TotalQty"]}" '
                f'Status="{row["Status"]}" '
                f'Remarks="{row["Remarks"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'CreatedBy="{decoded.get("user_id", "")}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded.get("user_id", "")}" '
                f'UpdatedDate="{dt.now()}" '
                f'ADDT1="{""}" '
                f'ADDT2="{""}" '
                f'ADDT3="{""}" '
                f'ADDT4="{""}" '
                f'ADDI1="{0}" '
                f'ADDI2="{0}" '
                f'ADDI3="{0}" '
                f'ADDI4="{0}" '
                f'ADDD1="{0.000}" '
                f'ADDD2="{0.000}" '
                f'ADDD3="{0.000}" '
                f'ADDD4="{0.000}" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                '/>'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("item_master_list " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))

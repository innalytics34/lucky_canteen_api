from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))

def material_inward_xml(data, decoded):
    try:
        xml_data = '<CanteenMaterialInward>'
        for row in data:
            xml_data += (
                f'<CanteenMaterialInward '
                f'UID="{row["UID"]}" '
                f'LogonUser="{decoded["user_id"]}" '
                f'Branch_UID="{decoded["branch_id"]}" '
                f'DocumentType_UID="{row["DocumentType_UID"]}" '
                f'LongDocumentNo="{row["LongDocumentNo"]}" '
                f'DocumentDate="{row["DocumentDate"]}" '
                f'Year="{Year()[0]["Yr"]}" '
                f'ReferenceNo="{row["ReferenceNo"]}" '
                f'ReferenceDate="{row["ReferenceDate"]}" '
                f'Supplier_UID="{row["Supplier_UID"]}" '
                f'SupplierAddress="{row["SupplierAddress"]}" '
                f'District="{row["District"]}" '
                f'District_UID="{row["District_UID"]}" '
                f'State="{row["State"]}" '
                f'State_UID="{row["State_UID"]}" '
                f'Country="{row["Country"]}" '
                f'Country_UID="{row["Country_UID"]}" '
                f'Pincode="{row["Pincode"]}" '
                f'SupplierContact_UID="{row["SupplierContact_UID"]}" '
                f'Prepareby="{decoded["user_id"]}" '
                f'Status="{row["Status"]}" '
                f'TransportName="{row["TransportName"]}" '
                f'LRNo="{row["LRNo"]}" '
                f'LRDate="{row["LRDate"]}" '
                f'Location="{row["Location"]}" '
                f'VehicleNumber="{row["VehicleNumber"]}" '
                f'BalanceQty="{row["BalanceQty"]}" '
                f'TotalItemValue="{row["TotalItemValue"]}" '
                f'DiscountAmount="{row["DiscountAmount"]}" '
                f'TaxableAmount="{row["TaxableAmount"]}" '
                f'TaxableCharges="{row["TaxableCharges"]}" '
                f'CGSTTotal="{row["CGSTTotal"]}" '
                f'SGSTTotal="{row["SGSTTotal"]}" '
                f'IGSTTotal="{row["IGSTTotal"]}" '
                f'RoundOff="{row["RoundOff"]}" '
                f'NetTotal="{row["NetTotal"]}" '
                f'Remarks="{row["Remarks"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'RejectReason="{row["RejectReason"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
                f'Currency="{row["Currency"]}" '
                f'OrderType="{row["OrderType"]}" '
                f'GRNNo="{row["GRNNo"]}" '
                f'GRNDate="{row["GRNDate"]}" '
                f'TDSPercentage="{row["TDSPercentage"]}" '
                f'TDSAmount="{row["TDSAmount"]}" '
                f'ConversionRate="{row["ConversionRate"]}" '
                f'ADDD1="{0.000}" '
                f'ADDD2="{0.000}" '
                f'ADDD3="{0.000}" '
                f'ADDD4="{0.000}" '
                f'ADDD5="{0.000}" '
                f'ADDI1="{0}" '
                f'ADDI2="{0}" '
                f'ADDI3="{0}" '
                f'ADDI4="{0}" '
                f'ADDI5="{0}" '
                f'ADDT1="{""}" '
                f'ADDT2="{""}" '
                f'ADDT3="{""}" '
                f'ADDT4="{""}" '
                f'ADDT5="{""}" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                f'ADDDT5="{dt.now()}"  />'
            )
        xml_data += '</CanteenMaterialInward>'
        return xml_data

    except Exception as e:
        print("Error in material_inward_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def material_inward_list_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMaterialInwardID="{row["CanteenMaterialInwardID"]}" '
                f'ReferenceTransListID="{row["ReferenceTransListID"]}" '
                f'ReferenceTransID="{row["ReferenceTransID"]}" '
                f'ReferenceTransNo="{row["ReferenceTransNo"]}" '
                f'LotNo="{row["LotNo"]}" '
                f'BatchNo="{row["BatchNo"]}" '
                f'ItemID="{row["ItemID"]}" '
                f'ItemDescription="{row["ItemDescription"]}" '
                f'InvoiceNo="{row["InvoiceNo"]}" '
                f'InvoiceDate="{row["InvoiceDate"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'UOMDescription="{row["UOMDescription"]}" '
                f'BaseUOMID="{row["BaseUOMID"]}" '
                f'BaseUOMDescription="{row["BaseUOMDescription"]}" '
                f'BaseUOMQty="{row["BaseUOMQty"]}" '
                f'Qty="{row["Qty"]}" '
                f'POQty="{row["POQty"]}" '
                f'TotalQty="{row["TotalQty"]}" '
                f'Price="{row["Price"]}" '
                f'BasicAmount="{row["BasicAmount"]}" '
                f'DiscountPercent="{row["DiscountPercent"]}" '
                f'DiscountAmount="{row["DiscountAmount"]}" '
                f'TotalBasicAmount="{row["TotalBasicAmount"]}" '
                f'CGSTPer="{row["CGSTPer"]}" '
                f'CGSTAmount="{row["CGSTAmount"]}" '
                f'SGSTPer="{row["SGSTPer"]}" '
                f'SGSTAmount="{row["SGSTAmount"]}" '
                f'IGSTPer="{row["IGSTPer"]}" '
                f'IGSTAmount="{row["IGSTAmount"]}" '
                f'TotalAmount="{row["TotalAmount"]}" '
                f'Status="{row["Status"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
                f'DocumentTypeID="{row["DocumentTypeID"]}" '
                f'WarrantyFromDate="{row["WarrantyFromDate"]}" '
                f'WarrantyToDate="{row["WarrantyToDate"]}" '
                f'ExcessQty="{row["ExcessQty"]}" '
                f'ShortageQty="{row["ShortageQty"]}" '
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
                f'ADDT1="{""}" '
                f'ADDT2="{""}" '
                f'ADDT3="{""}" '
                f'ADDT4="{""}" '
                f'ADDT5="{""}" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                f'ADDDT5="{dt.now()}"  />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in material_inward_list_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def material_inward_charges_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMaterialInward_UID="{row["CanteenMaterialInward_UID"]}" '
                f'ChargesM_UID="{row["ChargesM_UID"]}" '
                f'ChargesPer="{row["ChargesPer"]}" '
                f'ChargesAmount="{row["ChargesAmount"]}" '
                f'CGSTPer="{row["CGSTPer"]}" '
                f'CGSTAmount="{row["CGSTAmount"]}" '
                f'SGSTPer="{row["SGSTPer"]}" '
                f'SGSTAmount="{row["SGSTAmount"]}" '
                f'IGSTPer="{row["IGSTPer"]}" '
                f'IGSTAmount="{row["IGSTAmount"]}" '
                f'TotalAmount="{row["TotalAmount"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}"  />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in material_inward_charges_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def material_inward_terms_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMaterialInward_UID="{row["CanteenMaterialInward_UID"]}" '
                f'Terms_UID="{row["Terms_UID"]}" '
                f'Terms="{row["Terms"]}" '
                f'TermDescription="{row["TermDescription"]}" '
                f'Description="{row["Description"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in material_inward_terms_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None

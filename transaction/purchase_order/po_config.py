from datetime import datetime as dt
from login.py_dropdown import Year
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))


def purchase_order_xml(data, decoded):
    try:
        xml_data = '<CanteenPurchaseOrder>'
        for row in data:
            xml_data += (
                f'<CanteenPurchaseOrder '
                f'UID="{row["UID"]}" '
                f'LogonUser="{decoded["user_id"]}" '
                f'BranchID="{decoded["branch_id"]}" '
                f'LongDocumentNo="{row["LongDocumentNo"]}" '
                f'DocumentDate="{row["DocumentDate"]}" '
                f'Year="{Year()[0]["Yr"]}" '
                f'DocumentType_UID="{row["DocumentType_UID"]}" '
                f'ReferenceNo="{row["ReferenceNo"]}" '
                f'ReferenceDate="{row["ReferenceDate"]}" '
                f'SupplierID="{row["SupplierID"]}" '
                f'SupplierName="{row["SupplierName"]}" '
                f'Address="{row["Address"]}" '
                f'DistrictID="{row["DistrictID"]}" '
                f'District="{row["District"]}" '
                f'StateID="{row["StateID"]}" '
                f'State="{row["State"]}" '
                f'CountryID="{row["CountryID"]}" '
                f'Country="{row["Country"]}" '
                f'Pincode="{row["Pincode"]}" '
                f'ContactPerson="{row["ContactPerson"]}" '
                f'DispatchName="{row["DispatchName"]}" '
                f'DispatchAddress="{row["DispatchAddress"]}" '
                f'DispatchDistrictID="{row["DispatchDistrictID"]}" '
                f'DispatchDistrict="{row["DispatchDistrict"]}" '
                f'DispatchStateID="{row["DispatchStateID"]}" '
                f'DispatchState="{row["DispatchState"]}" '
                f'DispatchCountryID="{row["DispatchCountryID"]}" '
                f'DispatchCountry="{row["DispatchCountry"]}" '
                f'DispatchPincode="{row["DispatchPincode"]}" '
                f'DispatchContactPerson="{row["DispatchContactPerson"]}" '
                f'ExpectedDelivery="{row["ExpectedDelivery"]}" '
                f'PreparedBy="{decoded["user_id"]}" '
                f'VehicleNo="{row["VehicleNo"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'RejectReason="{row["RejectReason"]}" '
                f'Status="{row["Status"]}" '
                f'TotalItemValue="{row["TotalItemValue"]}" '
                f'DiscountAmount="{row["DiscountAmount"]}" '
                f'TaxableAmount="{row["TaxableAmount"]}" '
                f'TaxableCharges="{row["TaxableCharges"]}" '
                f'CGSTTotal="{row["CGSTTotal"]}" '
                f'SGSTTotal="{row["SGSTTotal"]}" '
                f'IGSTTotal="{row["IGSTTotal"]}" '
                f'TCSPer="{row["TCSPer"]}" '
                f'TCSAmount="{row["TCSAmount"]}" '
                f'RoundOff="{row["RoundOff"]}" '
                f'NetTotal="{row["NetTotal"]}" '
                f'TotalQty="{row["TotalQty"]}" '
                f'Remarks="{row["Remarks"]}" '
                f'AmendmentNo="{row["AmendmentNo"]}" '
                f'AmendmentDate="{row["AmendmentDate"]}" '
                f'AmendmentReason="{row["AmendmentReason"]}" ' 
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" '                
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
                f'FreightChargesID="{row["FreightChargesID"]}" '
                f'FreightCharges="{row["FreightCharges"]}" '
                f'TDSPercentage="{row["TDSPercentage"]}" '
                f'TDSAmount="{row["TDSAmount"]}" '
                f'POTypeID="{row["POTypeID"]}" '
                f'POType="{row["POType"]}" '
                f'file_path="{row["file_path"]}" />'
            )
        xml_data += '</CanteenPurchaseOrder>'
        return xml_data

    except Exception as e:
        print("Error in purchase_order_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def purchase_order_list_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenPurchaseOrderID="{row["CanteenPurchaseOrderID"]}" '
                f'ReferenceTransID="{row["ReferenceTransID"]}" '
                f'ReferenceTransListID="{row["ReferenceTransListID"]}" '
                f'ReferenceTransNo="{row["ReferenceTransNo"]}" '
                f'ItemID="{row["ItemID"]}" '
                f'ItemDescription="{row["ItemDescription"]}" '
                f'PartNo="{row["PartNo"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'UomDescription="{row["UomDescription"]}" '
                f'Qty="{row["Qty"]}" '
                f'BaseUOMID="{row["BaseUOMID"]}" '
                f'BaseUomDescription="{row["BaseUomDescription"]}" '
                f'BaseUOMQty="{row["BaseUOMQty"]}" '
                f'TotalQty="{row["TotalQty"]}" '
                f'Price="{row["Price"]}" '
                f'DiscountPer="{row["DiscountPer"]}" '
                f'DiscountAmount="{row["DiscountAmount"]}" '
                f'BasicValue="{row["BasicValue"]}" '
                f'TotalBasicValue="{row["TotalBasicValue"]}" '
                f'CGSTPer="{row["CGSTPer"]}" '
                f'CGSTAmount="{row["CGSTAmount"]}" '
                f'SGSTPer="{row["SGSTPer"]}" '
                f'SGSTAmount="{row["SGSTAmount"]}" '
                f'IGSTPer="{row["IGSTPer"]}" '
                f'IGSTAmount="{row["IGSTAmount"]}" '
                f'TotalAmount="{row["TotalAmount"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'DocumentTypeID="{row["DocumentTypeID"]}" '
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
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in purchase_order_list_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def purchase_order_charges_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenPurchaseOrderID="{row["CanteenPurchaseOrderID"]}" '
                f'ChargesMID="{row["ChargesMID"]}" '
                f'ChargesDescription="{row["ChargesDescription"]}" '
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
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in purchase_order_charges_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None


def purchase_order_terms_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'PurchaseOrderID="{row["PurchaseOrderID"]}" '
                f'TermsID="{row["TermsID"]}" '
                f'Terms="{row["Terms"]}" '
                f'TermDescription="{row["TermDescription"]}" '
                f'Description="{row["Description"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{row.get("CreatedBy", "")}" '
                f'CreatedDate="{row.get("CreatedDate", "")}" '
                f'UpdatedBy="{row.get("UpdatedBy", "")}" '
                f'UpdatedDate="{row.get("UpdatedBy", "")}" />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in purchase_order_terms_xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return None

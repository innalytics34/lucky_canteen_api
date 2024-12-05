from datetime import datetime as dt
from login.py_dropdown import Year

def menu_xml(data, decoded):
    try:
        xml_data = '<CanteenMenu>'
        for row in data:
            xml_data += (
                f'<CanteenMenu '
                f'UID="{row["UID"]}" '
                f'LogonUser="{decoded["user_id"]}" '
                f'BranchID="{decoded["branch_id"]}" '
                f'DocumentTypeID="{row["DocumentTypeID"]}" '
                f'Year="{Year()[0]["Yr"]}" '
                f'LongDocumentNo="{row["LongDocumentNo"]}" '
                f'DocumentDate="{row["DocumentDate"]}" '
                f'ReferenceTransID="{row["ReferenceTransID"]}" '
                f'ReferenceDate="{row["ReferenceDate"]}" '
                f'ReferenceTransNo="{row["ReferenceTransNo"]}" '
                f'MealsTypeID="{row["MealsTypeID"]}" '
                f'MealsType="{row["MealsType"]}" '
                f'TotalMembers="{row["TotalMembers"]}" '
                f'Status="{row["Status"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'RejectReason="{row["RejectReason"]}" '
                f'Remarks="{row["Remarks"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
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
        xml_data += '</CanteenMenu>'
        return xml_data

    except Exception as e:
        print("Error in canteen_menu xml: " + str(e))
        return None


def menu_list_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMenuID="{row["CanteenMenuID"]}" '
                f'ItemID="{row["ItemID"]}" '
                f'ItemDescription="{row["ItemDescription"]}" '
                f'PartNo="{row["PartNo"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'UomDescription="{row["UomDescription"]}" '
                f'Qty="{row["Qty"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
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
                f'ADDDT5="{dt.now()}" '
                f'MaxOrderQty="{row["MaxOrderQty"]}" '
                f'ItemCode="{row["ItemCode"]}" />'
            )
        xml_data += f'</{element_name}>'
        return xml_data
    except Exception as e:
        print("Error in canteen_menu_list_xml: " + str(e))
        return None
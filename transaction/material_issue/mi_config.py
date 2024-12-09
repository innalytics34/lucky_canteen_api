from datetime import datetime as dt
from login.py_dropdown import Year


def material_issue_xml(data, decoded):
    try:
        xml_data = '<CanteenMaterialIssue>'
        for row in data:
            xml_data += (
                f'<CanteenMaterialIssue '
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
                f'TotalMembers="{row["TotalMembers"]}" '
                f'LocationID="{row["LocationID"]}" '
                f'Location="{row["Location"]}" '
                f'Status="{row["Status"]}" '
                f'WorkFlowStatus="{row["WorkFlowStatus"]}" '
                f'RejectReason="{row["RejectReason"]}" '
                f'Remarks="{row["Remarks"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
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
                f'ADDDT5="{row["ADDDT5"]}" />'
            )
        xml_data += '</CanteenMaterialIssue>'
        return xml_data

    except Exception as e:
        print("Error in material_issue_xml: " + str(e))
        return None


def material_issue_list_xml(data, decoded, element_name):
    try:
        xml_data = f'<{element_name}>'
        for row in data:
            xml_data += (
                f'<{element_name} '
                f'UID="{row["UID"]}" '
                f'CanteenMaterialIssueID="{row["CanteenMaterialIssueID"]}" '
                f'ReferenceTransID="{row["ReferenceTransID"]}" '
                f'ReferenceTransListID="{row["ReferenceTransListID"]}" '
                f'ReferenceTransNo="{row["ReferenceTransNo"]}" '
                f'ItemID="{row["ItemID"]}" '
                f'ItemDescription="{row["ItemDescription"]}" '
                f'RawMaterialID="{row["RawMaterialID"]}" '
                f'RawMaterialDescription="{row["RawMaterialDescription"]}" '
                f'ItemTypeID="{row["ItemTypeID"]}" '
                f'ItemType="{row["ItemType"]}" '
                f'StockID="{row["StockID"]}" '
                f'BatchID="{row["BatchID"]}" '
                f'UOMID="{row["UOMID"]}" '
                f'UOMDescription="{row["UOMDescription"]}" '
                f'BaseUOMID="{row["BaseUOMID"]}" '
                f'BaseUOMDescription="{row["BaseUOMDescription"]}" '
                f'BaseUOMQty="{row["BaseUOMQty"]}" '
                f'StockQty="{row["StockQty"]}" '
                f'StockTotalQty="{row["StockTotalQty"]}" '
                f'UOMQty="{row["UOMQty"]}" '
                f'RequestQty="{row["RequestQty"]}" '
                f'RequestTotalQty="{row["RequestTotalQty"]}" '
                f'TotalQty="{row["TotalQty"]}" '
                f'Price="{row["Price"]}" '
                f'Status="{row["Status"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
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
        print("Error in material_issue_list_xml: " + str(e))
        return None
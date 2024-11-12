from datetime import datetime as dt


def product_master(data, decoded):
    try:
        xml_data = '<CanteenProductMaster>\n'
        for row in data:
            xml_data += (
                '    <CanteenProductMaster '
                f'BranchId="{decoded.get("branch_id", "")}" '
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
                f'ProductCategory="{row.get("ProductCategory", "")}" '
                '/>\n'
            )
        xml_data += '</CanteenProductMaster>'
        return xml_data
    except Exception as e:
        print("product_master " + str(e))


def raw_material(data):
    try:
        xml_data = '<RawMaterialMaster>\n'
        for row in data:
            xml_data += (
                '    <RawMaterialMaster '
                f'PartNo="{row.get("PartNo", "")}" '
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
                f'ADDDT5="{dt.now()}" '
                '/>\n'
            )
        xml_data += '</RawMaterialMaster>'
        return xml_data
    except Exception as e:
        print("raw_material " + str(e))


def item_master(data):
    try:
        xml_data = '<ItemMaster>\n'
        for row in data:
            xml_data += (
                '    <ItemMaster '
                f'PartNo="{row.get("PartNo", "")}" '
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


def item_master_list(data, decoded):
    try:
        xml_data = '<ItemMasterList>\n'
        for row in data:
            xml_data += '    <ItemMasterList\n'
            xml_data += f'        UID="{row.get("UID")}"\n'
            xml_data += f'        ItemMasterID="{row.get("ItemMasterID")}"\n'
            xml_data += f'        RawMaterialID="{row.get("RawMaterialID")}"\n'
            xml_data += f'        RawMaterialDescription="{row.get("RawMaterialDescription")}"\n'
            xml_data += f'        PartNo="{row.get("PartNo")}"\n'
            xml_data += f'        ItemTypeID="{row.get("ItemTypeID")}"\n'
            xml_data += f'        ItemType="{row.get("ItemType")}"\n'
            xml_data += f'        UOM="{row.get("UOM")}"\n'
            xml_data += f'        UOMID="{row.get("UOMID")}"\n'
            xml_data += f'        Qty="{row.get("Qty")}"\n'
            xml_data += f'        Status="{row.get("Status")}"\n'
            xml_data += f'        Remarks="{row.get("Remarks")}"\n'
            xml_data += f'        WorkFlowStatus="{row.get("WorkFlowStatus")}"\n'
            xml_data += f'        CreatedBy="{decoded.get("user_id")}"\n'
            xml_data += f'        CreatedDate="{dt.now()}"\n'
            xml_data += f'        UpdatedBy="{decoded.get("user_id")}"\n'
            xml_data += f'        UpdatedDate="{dt.now()}"\n'
            xml_data += f'        ADDT1=" "\n'
            xml_data += f'        ADDT2=" "\n'
            xml_data += f'        ADDT3=" "\n'
            xml_data += f'        ADDT4=" "\n'
            xml_data += f'        ADDI1=" "\n'
            xml_data += f'        ADDI2="{0}"\n'
            xml_data += f'        ADDI3="{0}"\n'
            xml_data += f'        ADDI4="{0}"\n'
            xml_data += f'        ADDD1="{0}"\n'
            xml_data += f'        ADDD2="{0}"\n'
            xml_data += f'        ADDD3="{0}"\n'
            xml_data += f'        ADDD4="{0}"\n'
            xml_data += f'        ADDDT1="{dt.now()}"\n'
            xml_data += f'        ADDDT2="{dt.now()}"\n'
            xml_data += f'        ADDDT3="{dt.now()}"\n'
            xml_data += f'        ADDDT4="{dt.now()}"\n'
            xml_data += '    />\n'
        xml_data += '</ItemMasterList>'
        return xml_data
    except Exception as e:
        print("item_master_list " + str(e))

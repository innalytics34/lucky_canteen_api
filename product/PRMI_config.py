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
                f'UpdatedBy="{row.get("user_id", "")}" '
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

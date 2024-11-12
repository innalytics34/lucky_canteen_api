from db_connection import py_connection


def hsn_insert_update(request, decoded):
    try:
        print(request)
        UID = request.get("UID")
        HSNSACCode = request.get("HSNSACCode")
        BranchID = decoded.get("branch_id")
        ShortDescription = request.get("ShortDescription")
        LongDescription = request.get("LongDescription")
        Type = request.get("Type")
        CGST = request.get("CGST")
        SGST = request.get("SGST")
        IGST = request.get("IGST")
        CustomDuty = request.get("CustomDuty")
        Active = request.get("Active")
        AED = request.get("AED")
        CESS1 = request.get("CESS1")
        CESS2 = request.get("CESS2")
        GSTPaySlab_UID = request.get("GSTPaySlab_UID")

        if UID not in [0, '0', '']:
            values = (UID, HSNSACCode, BranchID, ShortDescription, LongDescription, Type, CGST, SGST, IGST,
                      CustomDuty, Active, AED, CESS1, CESS2, GSTPaySlab_UID)
            py_connection.put_result("{call Canteen.Bis_HSNSACMaster_Update"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            stat = "updated"
        else:
            values = (UID, HSNSACCode, BranchID, ShortDescription, LongDescription, Type, CGST, SGST, IGST,
                      CustomDuty, Active, AED, CESS1, CESS2, GSTPaySlab_UID)
            py_connection.put_result("{call Canteen.Bis_HSNSACMaster_Insert"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("uom_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}

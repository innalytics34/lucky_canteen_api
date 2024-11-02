from db_connection import py_connection


def charges_insert_update(request):
    try:
        UID = request.get("UID")
        ChargesDescription = request.get("ChargesDescription")
        ActiveStatus = request.get("ActiveStatus")
        BranchID = request.get("BranchID")
        if UID not in [0, '0', '']:
            values = (UID, ChargesDescription, ActiveStatus, BranchID)
            py_connection.put_result("{call Canteen.Bis_AdditionalCharges_Update"
                                     "(?,?,?,?)}", values)
            stat = "updated"
        else:
            values = (UID, ChargesDescription, ActiveStatus, BranchID)
            py_connection.put_result("{call Canteen.Bis_AdditionalCharges_Insert"
                                     "(?,?,?,?)}", values)
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("charges_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}

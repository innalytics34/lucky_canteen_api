from db_connection import py_connection


def charges_insert_update(request):
    try:
        print(request)
        UID = request.get("UID")
        ChargesDescription = request.get("ChargesDescription")
        ActiveStatus = request.get("ActiveStatus")
        if UID not in [0, '0', '']:
            values = (UID, ChargesDescription, ActiveStatus)
            py_connection.put_result("{call Canteen.Bis_AdditionalCharges_Update"
                                     "(?,?,?)}", values)
            stat = "updated"
        else:
            values = (UID, ChargesDescription, ActiveStatus)
            py_connection.put_result("{call Canteen.Bis_AdditionalCharges_Insert"
                                     "(?,?,?)}", values)
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("charges_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}


def add_charges_insert(request):
    try:
        UID = request.get("UID")
        ChargesDescription = request.get("ChargesDescription")
        ActiveStatus = request.get("ActiveStatus")
        values = (UID, ChargesDescription, ActiveStatus)
        py_connection.put_result("{call Canteen.Bis_AdditionalCharges_Insert"
                                 "(?,?,?)}", values)
        stat = "inserted"
        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("charges_insert_update " + str(e))
        return {"message": "Something went wrong!", "rval": 0}
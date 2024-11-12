from db_connection import py_connection


def generalMaster_insert_update(request, decoded):
    try:
        UID = request.get('UID')
        BranchID = decoded.get('branch_id')
        MasterTypeM_UID = request.get('MasterTypeM_UID')
        Code = request.get('Code', None)
        Description = request.get('Description')
        Remarks = request.get('Remarks', None)
        Active = request.get('Active')
        IsFixed = request.get('IsFixed')
        IsReqForSysAccess = request.get('IsReqForSysAccess')
        Type_UID = request.get('Type_UID')
        MasterParentType_UID = request.get('MasterParentType_UID')

        if UID not in [0, '0', '']:
            values = (UID, BranchID, BranchID, MasterTypeM_UID, Code, Description, Remarks, Active, IsFixed,
                      IsReqForSysAccess, Type_UID, MasterParentType_UID)
            py_connection.put_result("{call Canteen.bis_MasterM_Update"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            stat = "updated"
        else:
            values = (UID, BranchID, BranchID, MasterTypeM_UID, Code, Description, Remarks, Active, IsFixed,
                      IsReqForSysAccess, Type_UID, MasterParentType_UID)
            py_connection.put_result("{call Canteen.bis_MasterM_Insert"
                                     "(?,?,?,?,?,?,?,?,?,?,?,?)}", values)
            stat = "inserted"

        return {"message": "Data " + stat + " successfully", "rval": 1}
    except Exception as e:
        print("generalMaster " + str(e))
        return {"message": "Something went wrong!", "rval": 0}
    
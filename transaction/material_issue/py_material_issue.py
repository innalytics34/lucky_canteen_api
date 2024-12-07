from db_connection import py_connection
from transaction.material_issue.mi_config import material_issue_xml, material_issue_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year

def mai_insert_update(request, decoded):  # 80500
    UID = request.get("UID")

    CanteenMaterialIssueXML = material_issue_xml(request['material_issue'], decoded)
    print(CanteenMaterialIssueXML, '000')

    CanteenMaterialIssueListInsertXML, CanteenMaterialIssueListUpdateXML = find_new_record(request['mai_list'])

    element_lst = 'CanteenMaterialIssueList'
    i_CanteenMaterialIssueListXML = material_issue_list_xml(CanteenMaterialIssueListInsertXML, decoded, element_lst)
    print(i_CanteenMaterialIssueListXML, '111')

    element_lsts = 'CanteenMaterialIssueLists'
    u_CanteenMaterialIssueListXML = material_issue_list_xml(CanteenMaterialIssueListUpdateXML, decoded, element_lsts)
    print(u_CanteenMaterialIssueListXML, '222')

    if UID not in ['', 0, '0']:
        values = (CanteenMaterialIssueXML, i_CanteenMaterialIssueListXML, u_CanteenMaterialIssueListXML, UID)
        py_connection.call_prop("{call Canteen.[bis_MaterialIssue_Update]"
                                "(?,?,?,?)}", values)
        return {"message": "Material Issue Updated Successfully", "rval": 1}
    else:
        values = (CanteenMaterialIssueXML, i_CanteenMaterialIssueListXML,
                  80600, decoded['branch_id'], Year()[0]["Yr"], dt.now())
        print(values, '00992')
        py_connection.call_prop("{call Canteen.bis_CanteenMaterialIssue_Insert"
                                "(?,?,?,?,?,?)}", values)
        return {"message": "Material Issue Inserted Successfully", "rval": 1}


def find_new_record(mai_list):
    MaterialIssueListInsert = [entry for entry in mai_list if entry["UID"] == 0]
    MaterialIssueListUpdate = [entry for entry in mai_list if entry["UID"] != 0]

    return (MaterialIssueListInsert if len(MaterialIssueListInsert) else '',
            MaterialIssueListUpdate)
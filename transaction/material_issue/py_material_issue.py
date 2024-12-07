from db_connection import py_connection
from transaction.material_issue.mi_config import material_issue_xml, material_issue_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year

def mai_insert_update(request, decoded):  # 80500
    UID = request.get("UID")

    CanteenMaterialIssueXML = material_issue_xml(request['material_issue'], decoded)
    print(CanteenMaterialIssueXML, '000')

    CanteenMaterialIssueListInsertXML, CanteenMaterialIssueListUpdateXML = find_new_record(request['mr_list'])

    element_lst = 'MaterialIssueList'
    i_CanteenMaterialRequestListXML = material_issue_xml(CanteenMaterialRequestListInsertXML, decoded, element_lst)
    print(i_CanteenMaterialRequestListXML, '111')

    element_lsts = 'MaterialIssueLists'
    u_CanteenMaterialRequestListXML = material_issue_list_xml(CanteenMaterialRequestListUpdateXML, decoded, element_lsts)
    print(u_CanteenMaterialRequestListXML, '222')

    if UID not in ['', 0, '0']:
        values = (CanteenMaterialRequestXML, i_CanteenMaterialRequestListXML, u_CanteenMaterialRequestListXML,
                  i_CanteenMaterialRequestDetailsXML, u_CanteenMaterialRequestDetailsXML, UID)
        py_connection.call_prop("{call Canteen.bis_CanteenMaterialRequest_Update"
                                "(?,?,?,?,?,?)}", values)
        return {"message": "Material Request Updated Successfully", "rval": 1}
    else:
        values = (CanteenMaterialRequestXML, i_CanteenMaterialRequestListXML, i_CanteenMaterialRequestDetailsXML,
                  80500, 100000, Year()[0]["Yr"], dt.now())
        print(values, '00992')
        py_connection.call_prop("{call Canteen.bis_CanteenMaterialRequest_Insert"
                                "(?,?,?,?,?,?,?)}", values)
        return {"message": "Material Request Inserted Successfully", "rval": 1}


def find_new_record(mr_list):
    MaterialRequestListInsert = [entry for entry in mr_list if entry["UID"] == 0]
    MaterialRequestListUpdate = [entry for entry in mr_list if entry["UID"] != 0]

    return (MaterialRequestListInsert if len(MaterialRequestListInsert) else '',
            MaterialRequestListUpdate)
from db_connection import py_connection
from transaction.material_request.mr_config import (material_request_xml, material_request_list_xml,
                                                   material_request_details_xml)
from datetime import datetime as dt
from login.py_dropdown import Year

def mr_insert_update(request, decoded):
    UID = request.get("UID")

    CanteenMaterialRequestXML = material_request_xml(request['material_request'], decoded)
    print(CanteenMaterialRequestXML, '000')

    (CanteenMaterialRequestListInsertXML, CanteenMaterialRequestListUpdateXML, CanteenMaterialRequestDetailsInsertXML,
     CanteenMaterialRequestDetailsUpdateXML) = find_new_record(request['mr_list'], request['mr_charges'])

    element_lst = 'CanteenMaterialRequestList'
    i_CanteenMaterialRequestListXML = material_request_list_xml(CanteenMaterialRequestListInsertXML, decoded, element_lst)
    print(i_CanteenMaterialRequestListXML, '111')

    element_lsts = 'CanteenMaterialRequestLists'
    u_CanteenMaterialRequestListXML = material_request_list_xml(CanteenMaterialRequestListUpdateXML, decoded, element_lsts)
    print(u_CanteenMaterialRequestListXML, '222')

    element_chg = 'CanteenMaterialRequestDetails'
    i_CanteenMaterialRequestDetailsXML = material_request_details_xml(CanteenMaterialRequestDetailsInsertXML, decoded,
                                                                      element_chg)
    print(i_CanteenMaterialRequestDetailsXML, '333')

    element_chgs = 'CanteenMaterialRequestDetailss'
    u_CanteenMaterialRequestDetailsXML = material_request_details_xml(CanteenMaterialRequestDetailsUpdateXML, decoded,
                                                                      element_chgs)
    print(u_CanteenMaterialRequestDetailsXML, '444')


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


def find_new_record(mr_list, mr_details):
    MaterialRequestListInsert = [entry for entry in mr_list if entry["UID"] == 0]
    MaterialRequestListUpdate = [entry for entry in mr_list if entry["UID"] != 0]
    MaterialRequestDetailsInsert = [entry for entry in mr_details if entry["UID"] == 0]
    MaterialRequestDetailsUpdate = [entry for entry in mr_details if entry["UID"] != 0]

    return (MaterialRequestListInsert if len(MaterialRequestListInsert) else '',
            MaterialRequestListUpdate, MaterialRequestDetailsInsert if len(MaterialRequestDetailsInsert) else '',
            MaterialRequestDetailsUpdate)
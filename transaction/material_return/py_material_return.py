from db_connection import py_connection
from transaction.material_return.mar_config import material_return_xml, material_return_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year

def mar_insert_update(request, decoded):  # 80700

    UID = request.get("UID")

    CanteenMaterialReturnXML = material_return_xml(request['material_return'], decoded)
    print(CanteenMaterialReturnXML, '000')

    CanteenMaterialReturnListInsertXML, CanteenMaterialReturnListUpdateXML = find_new_record(request['mar_list'])

    element_lst = 'CanteenMaterialReturnList'
    i_CanteenMaterialReturnListXML = material_return_list_xml(CanteenMaterialReturnListInsertXML, decoded, element_lst)
    print(i_CanteenMaterialReturnListXML, '111')

    element_lsts = 'CanteenMaterialReturnLists'
    u_CanteenMaterialReturnListXML = material_return_list_xml(CanteenMaterialReturnListUpdateXML, decoded, element_lsts)
    print(u_CanteenMaterialReturnListXML, '222')

    if UID not in ['', 0, '0']:
        values = (CanteenMaterialReturnXML, i_CanteenMaterialReturnListXML, u_CanteenMaterialReturnListXML, UID)
        py_connection.call_prop("{call Canteen.bis_CanteenMaterialReturn_Update"
                                "(?,?,?,?)}", values)
        return {"message": "Material Issue Updated Successfully", "rval": 1}
    else:
        values = (CanteenMaterialReturnXML, i_CanteenMaterialReturnListXML,
                  80700, decoded['branch_id'], Year()[0]["Yr"], dt.now())
        print(values, '00992')
        py_connection.call_prop("{call Canteen.bis_CanteenMaterialReturn_Insert"
                                "(?,?,?,?,?,?)}", values)
        return {"message": "Material Return Inserted Successfully", "rval": 1}


def find_new_record(mar_list):
    MaterialReturnListInsert = [entry for entry in mar_list if entry["UID"] == 0]
    MaterialReturnListUpdate = [entry for entry in mar_list if entry["UID"] != 0]

    return (MaterialReturnListInsert if len(MaterialReturnListInsert) else '',
            MaterialReturnListUpdate)
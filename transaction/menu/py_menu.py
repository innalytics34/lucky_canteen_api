from db_connection import py_connection
from transaction.menu.m_config import menu_xml, menu_list_xml
from datetime import datetime as dt
from login.py_dropdown import Year

def menu(request, decoded):
    print(request, '333')

    UID = request.get("UID")

    CanteenMenuXML = menu_xml(request['menu'], decoded)
    print(CanteenMenuXML, '444')

    CanteenMenuXMLListInsertXML, CanteenMenuXMLListUpdateXML = find_new_record(request['menu_list'])

    element_lst = 'CanteenMenuList'
    i_CanteenMenuXMLListInsertXML = menu_list_xml(CanteenMenuXMLListInsertXML, decoded, element_lst)
    print(i_CanteenMenuXMLListInsertXML, '111')

    element_lsts = 'CanteenMenuLists'
    u_CanteenMenuXMLListUpdateXML = menu_list_xml(CanteenMenuXMLListUpdateXML, decoded, element_lsts)
    print(u_CanteenMenuXMLListUpdateXML, '222')

    if UID not in ['', 0, '0']:
        values = (CanteenMenuXML, i_CanteenMenuXMLListInsertXML, u_CanteenMenuXMLListUpdateXML, UID)
        py_connection.call_prop("{call Canteen.bis_CanteenMenu_Update(?,?,?,?)}", values)
        return {"message": "Canteen Menu Updated Successfully", "rval": 1}

    else:
        values = (CanteenMenuXML, i_CanteenMenuXMLListInsertXML, 80400, decoded['branch_id'], Year()[0]["Yr"], dt.now())
        py_connection.call_prop("{call Canteen.bis_CanteenMenu_Insert"
                                "(?,?,?,?,?,?)}", values)
        return {"message": "Canteen Menu Inserted Successfully", "rval": 1}

def find_new_record(menu_list):
    MaterialInwardListInsert = [entry for entry in menu_list if entry["UID"] == 0]
    MaterialInwardListUpdate = [entry for entry in menu_list if entry["UID"] != 0]

    return (MaterialInwardListInsert if len(MaterialInwardListInsert) else '',
            MaterialInwardListUpdate)

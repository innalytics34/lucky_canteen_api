from db_connection import py_connection
from transaction.purchase_order.po_config import (purchase_order_xml,
                                                  purchase_order_list_xml, purchase_order_charges_xml,purchase_order_terms_xml)
from datetime import datetime as dt
from login.py_dropdown import Year

def po_insert_update(request, decoded):
    print(request, '0101')
    UID = request.get("UID")
    CanteenPurchaseOrderXML = purchase_order_xml(request['purchase_order'], decoded)
    print(CanteenPurchaseOrderXML, '000')

    (CanteenPurchaseOrderListInsertXML, CanteenPurchaseOrderListUpdateXML, CanteenPurchaseOrderChargesInsertXML,
     CanteenPurchaseOrderChargesUpdateXML, CanteenPurchaseOrderTermsInsertXML, CanteenPurchaseOrderTermsUpdateXML)= \
        (find_new_record(request['po_list'], request['po_charges'], request['po_items']))

    i_CanteenPurchaseOrderListXML = purchase_order_list_xml(CanteenPurchaseOrderListInsertXML, decoded)

    u_CanteenPurchaseOrderListXML = purchase_order_list_xml(CanteenPurchaseOrderListUpdateXML, decoded)

    i_CanteenPurchaseOrderChargesXML = purchase_order_charges_xml(CanteenPurchaseOrderChargesInsertXML, decoded)

    u_CanteenPurchaseOrderChargesXML = purchase_order_charges_xml(CanteenPurchaseOrderChargesUpdateXML, decoded)

    i_CanteenPurchaseOrderItermsXML = purchase_order_terms_xml(CanteenPurchaseOrderTermsInsertXML, decoded)

    u_CanteenPurchaseOrderItermsXML = purchase_order_terms_xml(CanteenPurchaseOrderTermsUpdateXML, decoded)

    if UID not in ['', 0, '0']:
        values = (CanteenPurchaseOrderXML, i_CanteenPurchaseOrderListXML, i_CanteenPurchaseOrderChargesXML,
                  i_CanteenPurchaseOrderItermsXML, 80200, 100000, Year()[0]["Yr"], dt.now())
        py_connection.call_prop("{call Canteen.bis_CanteenPurchaseOrder_Insert"
                                "(?,?,?,?,?,?,?,?)}", values)
    else:
        values = (CanteenPurchaseOrderXML, i_CanteenPurchaseOrderListXML, u_CanteenPurchaseOrderListXML,
                  i_CanteenPurchaseOrderChargesXML, u_CanteenPurchaseOrderChargesXML, i_CanteenPurchaseOrderItermsXML,
                  u_CanteenPurchaseOrderItermsXML, UID)
        py_connection.call_prop("{call Canteen.bis_CanteenPurchaseOrder_Update"
                                "(?,?,?,?,?,?,?,?)}", values)

    return {"message": "Purchase Order Inserted Successfully", "rval": 1}


def find_new_record(po_list, po_charges, po_terms):
    PurchaseOrderListInsert = [entry for entry in po_list if entry["UID"] == 0]
    PurchaseOrderListUpdate = [entry for entry in po_list if entry["UID"] != 0]
    PurchaseOrderChargesInsert = [entry for entry in po_charges if entry["UID"] == 0]
    PurchaseOrderChargesUpdate = [entry for entry in po_charges if entry["UID"] != 0]
    PurchaseOrderTermsInsert = [entry for entry in po_terms if entry["UID"] == 0]
    PurchaseOrderTermsUpdate = [entry for entry in po_terms if entry["UID"] != 0]

    return (PurchaseOrderListInsert if len(PurchaseOrderListInsert) else '',
            PurchaseOrderListUpdate, PurchaseOrderChargesInsert if len(PurchaseOrderChargesInsert) else '',
            PurchaseOrderChargesUpdate, PurchaseOrderTermsInsert if len(PurchaseOrderTermsInsert) else '',
            PurchaseOrderTermsUpdate)
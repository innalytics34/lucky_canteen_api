from db_connection import py_connection
from transaction.purchase_order.po_config import (purchase_order_xml,
                                                  purchase_order_list_xml, purchase_order_charges_xml,purchase_order_terms_xml)


def po_insert_update(request, decoded):
    print(request, '0101')
    CanteenPurchaseOrderXML = purchase_order_xml(request['purchase_order'], decoded)
    CanteenPurchaseOrderListXML = purchase_order_list_xml(request['po_list'], decoded)
    CanteenPurchaseOrderChargesXML = purchase_order_charges_xml(request['po_charges'], decoded)
    CanteenPurchaseOrderItermsXML = purchase_order_terms_xml(request['po_items'], decoded)
    values = (CanteenPurchaseOrderXML, CanteenPurchaseOrderListXML, CanteenPurchaseOrderChargesXML,
              CanteenPurchaseOrderItermsXML, 80200, 100000, 7, '2024-11-16')
    py_connection.call_prop("{call Canteen.bis_CanteenPurchaseOrder_Insert"
                            "(?,?,?,?,?,?,?,?)}", values)




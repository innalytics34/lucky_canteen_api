from db_connection import py_connection
from transaction.purchase_order.po_config import (purchase_order_xml,
                                                  purchase_order_list_xml, purchase_order_charges_xml,purchase_order_terms_xml)
from datetime import datetime as dt
from login.py_dropdown import Year

def po_insert_update(request, decoded):
    UID = request.get("UID")

    CanteenPurchaseOrderXML = purchase_order_xml(request['purchase_order'], decoded)
    print(CanteenPurchaseOrderXML, '000')
    (CanteenPurchaseOrderListInsertXML, CanteenPurchaseOrderListUpdateXML, CanteenPurchaseOrderChargesInsertXML,
     CanteenPurchaseOrderChargesUpdateXML, CanteenPurchaseOrderTermsInsertXML, CanteenPurchaseOrderTermsUpdateXML)= \
        (find_new_record(request['po_list'], request['po_charges'], request['po_items']))

    element_lst = 'CanteenPurchaseOrderList'
    i_CanteenPurchaseOrderListXML = purchase_order_list_xml(CanteenPurchaseOrderListInsertXML, decoded, element_lst)
    print(i_CanteenPurchaseOrderListXML, '111')

    element_lsts = 'CanteenPurchaseOrderLists'
    u_CanteenPurchaseOrderListXML = purchase_order_list_xml(CanteenPurchaseOrderListUpdateXML, decoded, element_lsts)
    print(u_CanteenPurchaseOrderListXML, '222')

    element_chg = 'CanteenPurchaseOrderCharges'
    i_CanteenPurchaseOrderChargesXML = purchase_order_charges_xml(CanteenPurchaseOrderChargesInsertXML, decoded,
                                                                  element_chg)
    print(i_CanteenPurchaseOrderChargesXML, '333')

    element_chgs = 'CanteenPurchaseOrderChargess'
    u_CanteenPurchaseOrderChargesXML = purchase_order_charges_xml(CanteenPurchaseOrderChargesUpdateXML, decoded,
                                                                  element_chgs)
    print(u_CanteenPurchaseOrderChargesXML, '444')

    element_trm = 'CanteenPurchaseOrderTerms'
    i_CanteenPurchaseOrderItermsXML = purchase_order_terms_xml(CanteenPurchaseOrderTermsInsertXML, decoded, element_trm)

    print(i_CanteenPurchaseOrderItermsXML, '555')

    element_trms = 'CanteenPurchaseOrderTermss'
    u_CanteenPurchaseOrderItermsXML = purchase_order_terms_xml(CanteenPurchaseOrderTermsUpdateXML, decoded,
                                                               element_trms)
    print(u_CanteenPurchaseOrderItermsXML, '666')

    if UID not in ['', 0, '0']:
        qry = """ 
                DECLARE @return_value int, @successful bit
                SET NOCOUNT ON; 

                EXEC @return_value = [Canteen].[bis_CanteenPurchaseOrder_Update]
                @CanteenPurchaseOrderInsert = ?,
                @CanteenPurchaseOrderListInsert = ?,
                @CanteenPurchaseOrderListUpdate = ?, 
                @CanteenPurchaseOrderChargesInsert = ?,
                @CanteenPurchaseOrderChargesUpdate =?, 
                @CanteenPurchaseOrderTermsInsert = ?,
                @CanteenPurchaseOrderTermsUpdate = ?, 
                @UID = ?,
                @successful = @successful OUTPUT

                SELECT @successful as N'@successful'
                SELECT 'Return Value' = @return_value
            """

        values = (CanteenPurchaseOrderXML, i_CanteenPurchaseOrderListXML, u_CanteenPurchaseOrderListXML,
                  i_CanteenPurchaseOrderChargesXML, u_CanteenPurchaseOrderChargesXML, i_CanteenPurchaseOrderItermsXML,
                  u_CanteenPurchaseOrderItermsXML, UID)
        res = py_connection.call_prop_return_pk1(qry, values)
        if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
            return {"message": "Purchase Order Details Updated Successfully", "rval": 1}
        else:
            return {"message": "Purchase Order Updation Failed", "rval": 0}
    else:
        qry = """ 
                DECLARE @return_value int, @successful bit
                SET NOCOUNT ON; 

                EXEC @return_value = [Canteen].[bis_CanteenPurchaseOrder_Insert]
                @CanteenPurchaseOrderInsert = ?, 
                @CanteenPurchaseOrderListInsert = ?, 
                @CanteenPurchaseOrderChargesInsert = ?,
                @CanteenPurchaseOrderTermsInsert = ?,
                @DocumetTypeId = ?,
                @Branch_ID = ?,
                @Year = ?, 
                @DocumentDate = ?, @successful = @successful OUTPUT

                SELECT @successful as N'@successful'
                SELECT 'Return Value' = @return_value
             """
        values = (CanteenPurchaseOrderXML, i_CanteenPurchaseOrderListXML, i_CanteenPurchaseOrderChargesXML,
                  i_CanteenPurchaseOrderItermsXML, 80200, 100000, Year()[0]["Yr"], dt.now())
        res = py_connection.call_prop_return_pk1(qry, values)
        if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
            return {"message": "Purchase Order Details Inserted Successfully", "rval": 1}
        else:
            return {"message": "Purchase Order Insertion Failed", "rval": 0}


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
fetch_config = {
    "accountM": {
        "data_source": "Bis_AccountM_SelectByField",
        "params": [
            {
                "label": 'fieldName',
                "source": "request"
            },
            {
                "label": 'AccountTypeM_UID',
                "source": "request"
            }
        ]
    },
    "accountMAddress": {
        "data_source": "bis_AccountMAddress_SelectByField",
        "params": [
                 {
                    "label": 'fieldName',
                    "source": "request"
                 },
                 {
                    "label": 'AccountID',
                    "source": "request"
                 }
            ]
    },
    "accountMContact": {
        "data_source": "Bis_AccountMContacts_SelectByField",
        "params": [
            {
                "label": 'fieldName',
                "source": "request"
            },
            {
                "label": 'AccountM_UID',
                "source": "request"
            }
        ]
    },
    "UOMMaster": {
        "data_source": "Bis_UOMMaster_SelectByField",
        "params": [
            {
                "label": 'fieldName',
                "source": "request"
            },
            {
                "label": 'UID',
                "source": "request"
            }
        ]
    },
    "UOMConversion": {
        "data_source": "Bis_UOMConversion_SelectByField",
        "params": [
            {
                "label": 'fieldName',
                "source": "request"
            },
            {
                "label": 'UID',
                "source": "request"
            }
        ]
    },
    "HSNSAC": {
        "data_source": "bis_Lookup_HSNSAC",
        "params": []
    },
    "TaxType": {
        "data_source": "bis_HSNSACMaster_TaxType",
        "params": []
    },
    "ItemsForItemMaster": {
        "data_source": "bis_Lookup_ItemsForItemMaster",
        "params": [
            {
                "label": 'branch_id',
                "source": "request"
            }
        ]
    },
    "Status": {
        "data_source": "bis_Lookup_Status",
        "params": []
    },
    "hsn": {
        "data_source": "Bis_HSNSACMaster_SelectAll",
        "params": []
    },
    "add_charges": {
        "data_source": "bis_CanteenProductMaster_SelectAll",
        "params": []
    },
    "add_charges_all": {
        "data_source": "Bis_AdditionalCharges_SelectAll",
        "params": []
    },
    "product_master_by_fields": {
        "data_source": "bis_CanteenProductMaster_SelectByField",
        "params": [
            {
                "label": 'fieldName',
                "source": "request"
            },
            {
                "label": 'UID',
                "source": "request"
            },
        ]
    },
    "uomMaster": {
        "data_source": "Bis_UOMMaster_SelectAll",
        "params": []
    },
    "UOMConversionAll": {
        "data_source": "bis_Search_UOM",
        "params": []
    },
    "UOMConversionByField": {
        "data_source": "bis_Search_UOM",
        "params": []
    },
    "RawMaterialMaster_SelectAll": {
        "data_source": "bis_RawMaterialMaster_SelectAll",
        "params": []
    },
    "PO_SearchView": {
        "data_source": "bis_Search_CanteenPurchaseOrder",
        "params": [
            {
                "label": "branch_id",
                "source": "decoded"
            },
            {
                "label": "year",
                "source": "decoded"
            },
            {
                "label": "document_type_id",  # 80200
                "source": "request"
            }
        ]
    },
    "PO_PurchaseOrder": {
        "data_source": "bis_CanteenPurchaseOrder_SelectByField",
        "params": [
            {
                "label": "field_name",  # UID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "PO_PurchaseOrderList": {
        "data_source": "bis_CanteenPurchaseOrderList_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenPurchaseOrderID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "PO_PurchaseOrderCharges": {
        "data_source": "bis_CanteenPurchaseOrderCharges_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenPurchaseOrderID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "PO_PurchaseOrderTerms": {
        "data_source": "bis_CanteenPurchaseOrderTerms_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenPurchaseOrderID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
}

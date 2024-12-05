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
    "IM_SearchView": {
        "data_source": "bis_Search_ItemMaster_Master",
        "params": []
    },
    "IM_ProductMaster": {
        "data_source": "bis_CanteenProductMaster_SelectByField",
        "params": [
            {
                "label": "field_name",
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "IM_ItemMaster": {
        "data_source": "bis_ItemMaster_SelectByField",
        "params": [
            {
                "label": "field_name",
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "IM_ItemMasterList": {
        "data_source": "bis_ItemMasterList_SelectByField",
        "params": [
            {
                "label": "field_name",
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
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
    "MI_SearchView": {
        "data_source": "bis_Search_CanteenMaterialInward",
        "params": [
            {
                "label": "branch_id",
                "source": "decoded"
            },
            {
                "label": "document_type_id",  # 80300
                "source": "request"
            },
            {
                "label": "year",
                "source": "decoded"
            }
        ]
    },
    "MI_MaterialInward": {
        "data_source": "bis_CanteenMaterialInward_SelectByField",
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
    "MI_MaterialInwardList": {
        "data_source": "bis_CanteenMaterialInwardList_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMaterialInwardID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "MI_MaterialInwardCharges": {
        "data_source": "bis_CanteenMaterialInwardCharges_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMaterialInwardID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "MI_MaterialInwardTerms": {
        "data_source": "bis_CanteenMaterialInwardTerms_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMaterialInwardID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "M_Search View": {
        "data_source": "bis_Search_CanteenMenu",
        "params": [
            {
                "label": "year",
                "source": "decoded"
            },
            {
                "label": "document_type_id",  # 80400
                "source": "request"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            }
        ]
    },
    "M_Menu": {
        "data_source": "bis_CanteenMenu_SelectByField",
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
    "M_MenuList": {
        "data_source": "bis_CanteenMenuList_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMenuID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    }
}

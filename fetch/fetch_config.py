fetch_config = {
    "ReviewPendingAdmin": {
        "data_source": "bis_LookUp_Select_ReviewDocuments_Admin",
        "params": []

    },
    "ReviewPendingEmployee": {
        "data_source": "bis_LookUp_Select_ReviewDocuments",
        "params": [
            {
                "label": "user_id",
                "source": "decoded"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            }
        ]
    },
    "ApprovePendingAdmin": {
        "data_source": "bis_LookUp_Select_ApprovePendingDocuments_Admin",
        "params": [
            {
                "label": "branch_id",
                "source": "decoded"
            }
        ]
    },
    "ApprovePendingEmployee": {
        "data_source": "bis_LookUp_Select_ApprovePendingDocuments",
        "params": [
            {
                "label": "user_id",
                "source": "decoded"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            }
        ]
    },
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
    "M_SearchView": {
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
    },
    "MR_SearchView": {
        "data_source": "bis_Search_CanteenMaterialRequest",
        "params": [
            {
                "label": "year",
                "source": "decoded"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            },
            {
                "label": "document_type_id",  # 80500
                "source": "request"
            }

        ]
    },
    "MR_MaterialRequest": {
        "data_source": "bis_CanteenMaterialRequest_SelectByField",
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
    "MR_MaterialRequestList": {
        "data_source": "bis_CanteenMaterialRequestList_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMaterialRequestID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "MR_MaterialRequestDetails": {
        "data_source": "bis_CanteenMaterialRequestDetails_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMaterialRequestID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "MaI_SearchView": {
        "data_source": "bis_Search_CanteenMaterialIssue",
        "params": [
            {
                "label": "year",
                "source": "decoded"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            },
            {
                "label": "document_type_id",  # 80600
                "source": "request"
            }
        ]
    },
    "MaI_MaterialIssue": {
        "data_source": "bis_MaterialIssue_SelectByField",
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
    "MaI_MaterialIssueList": {
        "data_source": "bis_MaterialIssueList_SelectByField",
        "params": [
            {
                "label": "field_name",  # MaterialIssueID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
    "Mar_SearchView": {
        "data_source": "bis_Search_CanteenMaterialReturn",
        "params": [
            {
                "label": "year",
                "source": "decoded"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            },
            {
                "label": "document_type_id",  # 80700
                "source": "request"
            }
        ]
    },
    "Mar_MaterialReturn": {
        "data_source": "bis_CanteenMaterialReturn_SelectByField",
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
    "Mar_MaterialReturnList": {
        "data_source": "bis_CanteenMaterialReturnList_SelectByField",
        "params": [
            {
                "label": "field_name",  # CanteenMaterialReturnID
                "source": "request"
            },
            {
                "label": "value",
                "source": "request"
            }
        ]
    },
}

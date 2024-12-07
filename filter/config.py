filter_config = {
    "common": {
        "data_source": "bis_Lookup_Master",
        "params": [
            {
                "label": "description",
                "source": "request"
            },
            {
                "label": "branch_id",
                "source": "request"
            },
            {
                "label": "master_type_id",
                "source": "request"
            },
        ]
    },
    "state_country_id": {
        "data_source": "bis_Lookup_DistrictStateCountry",
        "params": [
            {
                "label": "district_id",
                "source": "request"
            }
        ]
    },
    "GSTSlab": {
            "data_source": "bis_Lookup_GSTSlab",
            "params": []
        },
    "TaxType": {
            "data_source": "bis_HSNSACMaster_TaxType",
            "params": []
        },
    "hsn": {
            "data_source": "bis_HSNSACMaster_TaxType",
            "params": []
        },
    "UOM": {
            "data_source": "bis_Lookup_UOM",
            "params": [
                {
                    "label": "BaseUOM",
                    "source": "request"
                }
            ]
        },
    "baseUOM": {
        "data_source": "bis_Lookup_BaseUOM",
        "params": [
            {
                "label": 'BaseUOM',
                "source": "request"
            },
        ]
    },
    "Status": {
            "data_source": "bis_Lookup_Status",
            "params": []
    },
    "PO_Supplier": {
        "data_source": "Bis_Lookup_Supplier_All",
        "params": []
    },
    "PO_Dispatch": {
        "data_source": "Bis_Lookup_Company_Company",
        "params": [
            {
                "label": 'branch_id',
                "source": "decoded"
            }
        ]
    },
    "PO_ConfirmedBy": {
        "data_source": "bis_EmployeeM_Select_User",
        "params": [
            {
                "label": 'branch_id',
                "source": "decoded"
            }
        ]
    },
    "PO_ItemLookup": {
        "data_source": "bis_Lookup_ItemsForItemMaster",
        "params": [
            {
                "label": 'branch_id',
                "source": "decoded"
            }
        ]
    },
    "PO_Charges": {
        "data_source": "bis_Lookup_Charges",
        "params": []
    },
    "PO_Terms": {
        "data_source": "Bis_Gst_LoadTerms",
        "params": [
            {
                "label": 'branch_id',
                "source": "decoded"
            },
            {
                "label": 'document_type_id',
                "source": "request"  # 80200
            }
        ]
    },
    "UOM_Conversion": {
        "data_source": "bis_Lookup_UOMConversion",
        "params": [
            {
                "label": "uom_id",
                "source": "request"
            }
        ]
    },
    "PO_Contacts": {
        "data_source": "bis_Lookup_Customer_Contact",
        "params": [
            {
                "label": "customer_uid",
                "source": "request"
            }
        ]
    },
    "MI_Location": {
        "data_source": "bis_Lookup_Location",
        "params": []
    },
    "MI_Transport": {
        "data_source": "bis_Lookup_TransportName",
        "params": [
            {
                "label": "id",
                "source": "request"
            },
            {
                "label": "branch_id",
                "source": "decoded"
            }
        ]
    },
    "MI_ItemLookUp": {
        "data_source": "bis_Lookup_CanteenMaterialInward_Items",
        "params": [
            {
                "label": "supplier_id",
                "source": "request"
            }
        ]
    },
    "M_LookupItem": {
        "data_source": "bis_Lookup_ItemsForCanteenMenu",
        "params": []
    },
    "MR_Reference No": {
        "data_source": "bis_lookup_ItemsForCanteenMaterialRequest",
        "params": [
            {
                "label": "id",
                "source": "request"
            }
        ]
    },
    "MR_ItemLookup": {
        "data_source": "bis_lookup_ItemsForMenuList",
        "params": [
            {
                "label": "uid",
                "source": "request"
            }
        ]
    },
    "MR_TypeItemWise": {
        "data_source": "bis_lookup_ItemsForMenuList_RawMaterial",
        "params": [
            {
                "label": "uid",
                "source": "request"
            },
            {
                "label": "item_id",
                "source": "request"
            },
        ]
    },
    "MRTypeDirect": {
        "data_source": "bis_lookup_ItemsForMenuList_RawMaterial_Direct",
        "params": []
    },
    "MaI_ReferenceNo": {  # Material Issue
        "data_source": "bis_lookup_ItemsForCanteenMaterialIssue",
        "params": [
            {
                "label": "id",  # 1
                "source": "request"
            }
        ]
    },
    "MaI_ItemLookUp": {
        "data_source": "bis_lookup_ItemsForMaterialIssue",
        "params": [
            {
                "label": "ReferenceNo",
                "source": "request"
            },
            {
                "label": "location",
                "source": "request"
            }
        ]
    },
}

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
"GSTSlab": {
        "data_source": "bis_Lookup_GSTSlab",
        "params": []
    },
"UOM": {
        "data_source": "bis_Lookup_UOM",
        "params": [
            {
                "label": 'BaseUOM',
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
}

delete_config = {
    "accountM": {
        "data_source": "Bis_AccountM_DeleteByField",
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
   "accountMAddress": {
        "data_source": "bis_AccountMAddress_DeleteByField",
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
    "accountMContact": {
        "data_source": "Bis_AccountMContacts_DeleteByField",
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
}

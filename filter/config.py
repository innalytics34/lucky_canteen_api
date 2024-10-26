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
}

from contact.xml_config import accountMaddress
from db_connection import py_connection


def insert_multiple_addresses(data):
    xml_accountMAddress = accountMaddress(data)
    py_connection.put_result("{call Canteen.Bis_AccountMAddress_Insert(?,?)}", (xml_accountMAddress, 98))


def insert_conduct_list(contacts):
    xml_data = '<AccountMContact>'
    for contact in contacts:
        xml_data += (
            '<AccountMContact '
            f'Name="{contact["Name"]}" '
            f'Department="{contact["Department"]}" '
            f'Designation="{contact["Designation"]}" '
            f'MobileNo="{contact["MobileNo"]}" '
            f'PhoneNumber="{contact["PhoneNumber"]}" '
            f'EmailID="{contact["EmailID"]}" '
            f'IsRecordDeleted="{contact["IsRecordDeleted"]}" '
            f'CreatedBy="{contact["CreatedBy"]}" '
            f'CreatedDate="{contact["CreatedDate"]}" '
            f'UpdatedBy="{contact["UpdatedBy"]}" '
            f'UpdateDate="{contact["UpdateDate"]}" '
            f'ADDT1="{contact["ADDT1"]}" '
            f'ADDT2="{contact["ADDT2"]}" '
            f'ADDT3="{contact["ADDT3"]}" '
            f'ADDT4="{contact["ADDT4"]}" '
            f'ADDT5="{contact["ADDT5"]}" '
            f'ADDD1="{contact["ADDD1"]}" '
            f'ADDD2="{contact["ADDD2"]}" '
            f'ADDD3="{contact["ADDD3"]}" '
            f'ADDD4="{contact["ADDD4"]}" '
            f'ADDD5="{contact["ADDD5"]}" '
            f'ADDDT1="{contact["ADDDT1"]}" '
            f'ADDDT2="{contact["ADDDT2"]}" '
            f'ADDDT3="{contact["ADDDT3"]}" '
            f'ADDDT4="{contact["ADDDT4"]}" '
            f'ADDDT5="{contact["ADDDT5"]}" '
            f'ADDI1="{contact["ADDI1"]}" '
            f'ADDI2="{contact["ADDI2"]}" '
            f'ADDI3="{contact["ADDI3"]}" '
            f'ADDI4="{contact["ADDI4"]}" '
            f'ADDI5="{contact["ADDI5"]}" '
            f'ADDB1="{contact["ADDB1"]}" '
            f'ADDB2="{contact["ADDB2"]}" '
            f'ADDB3="{contact["ADDB3"]}" '
            f'ADDB4="{contact["ADDB4"]}" '
            f'ADDB5="{contact["ADDB5"]}" />'
        )
    xml_data += '</AccountMContact>'
    print(xml_data)
    py_connection.put_result("{call Canteen.Bis_AccountMContacts_Insert(?,?)}", (xml_data, 12))


contacts_to_insert = [
    {
        "Name": "John Doe",
        "Department": "HR",
        "Designation": "Manager",
        "MobileNo": "1234567890",
        "PhoneNumber": "0987654321",
        "EmailID": "john.doe@example.com",
        "IsRecordDeleted": '0',
        "CreatedBy": "1",
        "CreatedDate": "2024-10-26T12:00:00",
        "UpdatedBy": "1",
        "UpdateDate": "2024-10-26T12:00:00",
        "ADDT1": "Value1",
        "ADDT2": "Value2",
        "ADDT3": "Value3",
        "ADDT4": "Value4",
        "ADDT5": "Value5",
        "ADDD1": '100.0',
        "ADDD2": '200.0',
        "ADDD3": '300.0',
        "ADDD4": '400.0',
        "ADDD5": '500.0',
        "ADDDT1": "2024-10-26T12:00:00",
        "ADDDT2": "2024-10-26T12:00:00",
        "ADDDT3": "2024-10-26T12:00:00",
        "ADDDT4": "2024-10-26T12:00:00",
        "ADDDT5": "2024-10-26T12:00:00",
        "ADDI1": '1',
        "ADDI2": '2',
        "ADDI3": '3',
        "ADDI4": '4',
        "ADDI5": '5',
        "ADDB1": '0',
        "ADDB2": '0',
        "ADDB3": '0',
        "ADDB4": '0',
        "ADDB5": '0',
    },
]
# insert_conduct_list(contacts_to_insert)


address_list = [
    {
        "Address1": "456 Sample Rd",
        "Address2": "Near Sample Park",
        "DistrictID": '201',
        "District": "Sample District",
        "StateID": '101',
        "State": "California",
        "CountryID": '1',
        "Country": "USA",
        "Pincode": '90210',
        "Status": '1',
        "CreatedBy": '1',
        "UpdatedBy": '1',
        "ADDT1": "Additional Data 1",
        "ADDT2": "Additional Data 2",
        "ADDT3": "Additional Data 3",
        "ADDT4": "Additional Data 4",
        "ADDT5": "Additional Data 5",
        "ADDI1": '10',
        "ADDI2": '20',
        "ADDI3": '30',
        "ADDI4": '40',
        "ADDI5": '50',
        "ADDD1": '100.000',
        "ADDD2": '200.500',
        "ADDD3": '300.750',
        "ADDD4": '400.250',
        "ADDD5": '500.000',
        "ADDDT1": "2024-01-01T00:00:00",
        "ADDDT2": "2024-01-02T00:00:00",
        "ADDDT3": "2024-01-03T00:00:00",
        "ADDDT4": "2024-01-04T00:00:00",
        "ADDDT5": "2024-01-05T00:00:00",
        "ADDB1": '0',
        "ADDB2": '1',
        "ADDB3": '0',
        "ADDB4": '1',
        "ADDB5": '0',
        "ActiveStatus": '1',
    },
]

# insert_multiple_addresses(address_list)


def insert_account(account_data):
    xml_data = '<AccountM>'
    xml_data += (
        f'<AccountM AccountTypeM_UID="{account_data["AccountTypeM_UID"]}" '
        f'Branch_UID="{account_data["Branch_UID"]}" '
        f'Name="{account_data["Name"]}" '
        f'ShortName="{account_data["ShortName"]}" '
        f'Website="{account_data["Website"]}" '
        f'EmailID="{account_data["EmailID"]}" '
        f'StateCode="{account_data["StateCode"]}" '
        f'PanNo="{account_data["PanNo"]}" '
        f'GSTNo="{account_data["GSTNo"]}" '
        f'GstDate="{account_data["GstDate"]}" '
        f'CINNo="{account_data["CINNo"]}" '
        f'IsBilling="{account_data["IsBilling"]}" '
        f'IsDelivery="{account_data["IsDelivery"]}" '
        f'IsParent="{account_data["IsParent"]}" '
        f'Address="{account_data["Address"]}" '
        f'Address1="{account_data["Address1"]}" '
        f'District_UID="{account_data["District_UID"]}" '
        f'District="{account_data["District"]}" '
        f'State_UID="{account_data["State_UID"]}" '
        f'State="{account_data["State"]}" '
        f'Country_UID="{account_data["Country_UID"]}" '
        f'Country="{account_data["Country"]}" '
        f'Pincode="{account_data["Pincode"]}" '
        f'PhoneNo="{account_data["PhoneNo"]}" '
        f'MobileNo="{account_data["MobileNo"]}" '
        f'Fax="{account_data["Fax"]}" '
        f'IsActive="{account_data["IsActive"]}" '
        f'Logo="{account_data["Logo"]}" '
        f'CommisionPercent="{account_data["CommisionPercent"]}" '
        f'ProcessType_UID="{account_data["ProcessType_UID"]}" '
        f'IndustryType_UID="{account_data["IndustryType_UID"]}" '
        f'CreditDays="{account_data["CreditDays"]}" '
        f'CreditLimit="{account_data["CreditLimit"]}" '
        f'MinCreelCapacity="{account_data["MinCreelCapacity"]}" '
        f'MaxCreelCapacity="{account_data["MaxCreelCapacity"]}" '
        f'SetLength="{account_data["SetLength"]}" '
        f'IsTCSApplicable="{account_data["IsTCSApplicable"]}" '
        f'CreatedBy="{account_data["CreatedBy"]}" '
        f'CreatedDate="{account_data["CreatedDate"]}" '
        f'UpdatedBy="{account_data["UpdatedBy"]}" '
        f'UpdatedDate="{account_data["UpdatedDate"]}" '
        f'LedgerName="{account_data["LedgerName"]}" '
        f'ADDT1="{account_data["ADDT1"]}" '
        f'ADDT2="{account_data["ADDT2"]}" '
        f'ADDT3="{account_data["ADDT3"]}" '
        f'ADDT4="{account_data["ADDT4"]}" '
        f'ADDT5="{account_data["ADDT5"]}" '
        f'ADDD1="{account_data["ADDD1"]}" '
        f'ADDD2="{account_data["ADDD2"]}" '
        f'ADDD3="{account_data["ADDD3"]}" '
        f'ADDD4="{account_data["ADDD4"]}" '
        f'ADDD5="{account_data["ADDD5"]}" '
        f'ADDDT1="{account_data["ADDDT1"]}" '
        f'ADDDT2="{account_data["ADDDT2"]}" '
        f'ADDDT3="{account_data["ADDDT3"]}" '
        f'ADDDT4="{account_data["ADDDT4"]}" '
        f'ADDDT5="{account_data["ADDDT5"]}" '
        f'ADDI1="{account_data["ADDI1"]}" '
        f'ADDI2="{account_data["ADDI2"]}" '
        f'ADDI3="{account_data["ADDI3"]}" '
        f'ADDI4="{account_data["ADDI4"]}" '
        f'ADDI5="{account_data["ADDI5"]}" '
        f'ADDB1="{account_data["ADDB1"]}" '
        f'ADDB2="{account_data["ADDB2"]}" '
        f'ADDB3="{account_data["ADDB3"]}" '
        f'ADDB4="{account_data["ADDB4"]}" '
        f'ADDB5="{account_data["ADDB5"]}" '
        f'GSTTypeID="{account_data["GSTTypeID"]}" '
        f'GSTType="{account_data["GSTType"]}" />'
    )
    xml_data += '</AccountM>'
    print(xml_data)
    py_connection.put_result("{call Canteen.Bis_AccountM_Insert"
                             "(?,?,?,?,?,?,?,?,?,?,?,?,?)}",
        (xml_data, '', '', '', '', '', '', '', '', '', '', '', ''))


account_to_insert = {
    "AccountTypeM_UID": 200,
    "Branch_UID": 100000,
    "Name": "Sample Account",
    "ShortName": "Sample",
    "Website": "http://example.com",
    "EmailID": "sample@example.com",
    "StateCode": "NY",
    "PanNo": "ABCDE1234F",
    "GSTNo": "27ABCDE1234F1Z5",
    "GstDate": "2024-10-26T12:00:00",
    "CINNo": "U12345MH2020PTC123456",
    "IsBilling": 1,
    "IsDelivery": 1,
    "IsParent": 1,
    "Address": "123 Main St",
    "Address1": "Apt 1",
    "District_UID": 1,
    "District": "District Name",
    "State_UID": 1,
    "State": "State Name",
    "Country_UID": 1,
    "Country": "Country Name",
    "Pincode": 123456,
    "PhoneNo": "0123456789",
    "MobileNo": "9876543210",
    "Fax": "0123456789",
    "IsActive": 1,
    "Logo": "logo.png",
    "CommisionPercent": 10.0,
    "ProcessType_UID": 1,
    "IndustryType_UID": 1,
    "CreditDays": 30,
    "CreditLimit": 50000,
    "MinCreelCapacity": 100.0,
    "MaxCreelCapacity": 200.0,
    "SetLength": 10.0,
    "IsTCSApplicable": 1,
    "CreatedBy": 1,
    "CreatedDate": "2024-10-26T12:00:00",
    "UpdatedBy": 1,
    "UpdatedDate": "2024-10-26T12:00:00",
    "LedgerName": "Sample Ledger",
    "ADDT1": "Value1",
    "ADDT2": "Value2",
    "ADDT3": "Value3",
    "ADDT4": "Value4",
    "ADDT5": "Value5",
    "ADDD1": 100.0,
    "ADDD2": 200.0,
    "ADDD3": 300.0,
    "ADDD4": 400.0,
    "ADDD5": 500.0,
    "ADDDT1": "2024-10-26T12:00:00",
    "ADDDT2": "2024-10-26T12:00:00",
    "ADDDT3": "2024-10-26T12:00:00",
    "ADDDT4": "2024-10-26T12:00:00",
    "ADDDT5": "2024-10-26T12:00:00",
    "ADDI1": 1,
    "ADDI2": 2,
    "ADDI3": 3,
    "ADDI4": 4,
    "ADDI5": 5,
    "ADDB1": 1,
    "ADDB2": 1,
    "ADDB3": 1,
    "ADDB4": 1,
    "ADDB5": 1,
    "GSTTypeID": 1,
    "GSTType": "Regular",
}

insert_account(account_to_insert)







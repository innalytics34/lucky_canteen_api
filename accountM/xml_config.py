from datetime import datetime as dt
import os
from logger.logger_config import logger
import inspect

directory = os.path.dirname(os.path.abspath(__file__))

def AccountM(data, decoded, AccountTypeM_UID):
    try:
        xml_data = '<AccountM>\n'
        for row in data:
            xml_data += (
                '  <AccountM '
                f'UID="{row["UID"]}" '
                f'AccountTypeM_UID="{AccountTypeM_UID}" '
                f'Branch_UID="{decoded["branch_id"]}" '
                f'Name="{row["Name"]}" '
                f'ShortName="{row["ShortName"]}" '
                f'Website="{row["Website"]}" '
                f'EmailID="{row["EmailID"]}" '
                f'StateCode="{row["StateCode"]}" '
                f'PanNo="{row["PanNo"]}" '
                f'GSTNo="{row["GSTNo"]}" '
                f'GstDate="{row["GstDate"]}" '
                f'CINNo="{row["CINNo"]}" '
                f'IsBilling="{False}" '
                f'IsDelivery="{False}" '
                f'IsParent="{False}" '
                f'Address="{row["Address"]}" '
                f'Address1="{row["Address1"]}" '
                f'District_UID="{row["District_UID"]}" '
                f'District="{row["District"]}" '
                f'State_UID="{row["State_UID"]}" '
                f'State="{row["State"]}" '
                f'Country_UID="{row["Country_UID"]}" '
                f'Country="{row["Country"]}" '
                f'Pincode="{row["Pincode"]}" '
                f'PhoneNo="{row["PhoneNo"]}" '
                f'MobileNo="{row["MobileNo"]}" '
                f'Fax="{""}" '
                f'IsActive="{row["IsActive"]}" '
                f'Logo="{row["Logo"]}" '
                f'CommisionPercent="{0}" '
                f'ProcessType_UID="{0}" '
                f'IndustryType_UID="{0}" '
                f'CreditDays="{0}" '
                f'CreditLimit="{0}" '
                f'MinCreelCapacity="{0}" '
                f'MaxCreelCapacity="{0}" '
                f'SetLength="{0}" '
                f'IsTCSApplicable="{False}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdatedDate="{dt.now()}" '
                f'LedgerName="{""}" '
                f'ADDT1="" '
                f'ADDT2="" '
                f'ADDT3="" '
                f'ADDT4="" '
                f'ADDT5="" '
                f'ADDD1="{0}" '
                f'ADDD2="{0}" '
                f'ADDD3="{0}" '
                f'ADDD4="{0}" '
                f'ADDD5="{0}" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                f'ADDDT5="{dt.now()}" '
                f'ADDI1="{0}" '
                f'ADDI2="{0}" '
                f'ADDI3="{0}" '
                f'ADDI4="{0}" '
                f'ADDI5="{0}" '
                f'ADDB1="{False}" '
                f'ADDB2="{False}" '
                f'ADDB3="{False}" '
                f'ADDB4="{False}" '
                f'ADDB5="{False}" '
                f'GSTTypeID="{row["GSTTypeID"]}" '
                f'GSTType="{row["GSTType"]}" '
                '/>\n'
            )
        xml_data += '</AccountM>'
        return xml_data
    except Exception as e:
        print("Error in AccountM xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))



def AccountMContacts(contacts, decoded, element_name_contact):
    try:
        xml_data = f'<{element_name_contact}>'
        for contact in contacts:
            xml_data += (
                f'<{element_name_contact} '
                f'UID="{contact["UID"]}" '
                f'AccountM_UID="{contact["AccountM_UID"]}" '
                f'Name="{contact["Name"]}" '
                f'Department="{contact["Department"]}" '
                f'Designation="{contact["Designation"]}" '
                f'MobileNo="{contact["MobileNo"]}" '
                f'PhoneNumber="{contact["PhoneNumber"]}" '
                f'EmailID="{contact["EmailID"]}" '
                f'IsRecordDeleted="{contact["IsRecordDeleted"]}" '
                f'CreatedBy="{decoded["user_id"]}" '
                f'CreatedDate="{dt.now()}" '
                f'UpdatedBy="{decoded["user_id"]}" '
                f'UpdateDate="{dt.now()}" '
                f'ADDT1="{""}" '
                f'ADDT2="{""}" '
                f'ADDT3="{""}" '
                f'ADDT4="{""}" '
                f'ADDT5="{""}" '
                f'ADDD1="{0}" '
                f'ADDD2="{0}" '
                f'ADDD3="{0}" '
                f'ADDD4="{0}" '
                f'ADDD5="{0}" '
                f'ADDDT1="{dt.now()}" '
                f'ADDDT2="{dt.now()}" '
                f'ADDDT3="{dt.now()}" '
                f'ADDDT4="{dt.now()}" '
                f'ADDDT5="{dt.now()}" '
                f'ADDI1="{0}" '
                f'ADDI2="{0}" '
                f'ADDI3="{0}" '
                f'ADDI4="{0}" '
                f'ADDI5="{0}" '
                f'ADDB1="{False}" '
                f'ADDB2="{False}" '
                f'ADDB3="{False}" '
                f'ADDB4="{False}" '
                f'ADDB5="{False}" />'
            )
        xml_data += f'</{element_name_contact}>'
        return xml_data
    except Exception as e:
        print("Error in AccountMContacts xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))


def accountMaddress(data, decoded, element_name_address):
    try:
        xml_entries = "".join(f"""
                <{element_name_address}
                    UID="{row['UID']}"
                    AccountID="{row['AccountID']}"
                    Address1="{row['Address1']}"
                    Address2="{row['Address2']}"
                    DistrictID="{row['DistrictID']}"
                    District="{row['District']}"
                    StateID="{row['StateID']}"
                    State="{row['State']}"
                    CountryID="{row['CountryID']}"
                    Country="{row['Country']}"
                    Pincode="{row['Pincode']}"
                    Status="{row['Status']}"
                    CreatedBy="{decoded["user_id"]}"
                    UpdatedBy="{decoded["user_id"]}"
                    ADDT1="{""}"
                    ADDT2="{""}"
                    ADDT3="{""}"
                    ADDT4="{""}"
                    ADDT5="{""}"
                    ADDI1="{0}"
                    ADDI2="{0}"
                    ADDI3="{0}"
                    ADDI4="{0}"
                    ADDI5="{0}"
                    ADDD1="{0}"
                    ADDD2="{0}"
                    ADDD3="{0}"
                    ADDD4="{0}"
                    ADDD5="{0}"
                    ADDDT1="{dt.now()}"
                    ADDDT2="{dt.now()}"
                    ADDDT3="{dt.now()}"
                    ADDDT4="{dt.now()}"
                    ADDDT5="{dt.now()}"
                    ADDB1="{False}"
                    ADDB2="{False}"
                    ADDB3="{False}"
                    ADDB4="{False}"
                    ADDB5="{False}"
                    ActiveStatus="{row['ActiveStatus']}" />
            """ for row in data)
        full_xml = f"<{element_name_address}>{xml_entries}</{element_name_address}>"
        return full_xml
    except Exception as e:
        print("Error in accountMaddress xml: " + str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
from accountM.xml_config import accountMaddress, AccountM, AccountMContacts
from db_connection import py_connection
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))

def accountM(request, decoded):
    try:
        form_type = request.get('form_type')
        accountM_uid = request.get('accountM_uid')
        accountMAddress = request.get('accountMAddress')
        accountMContact = request.get('accountMContact')
        accountM = request.get('accountM')
        if form_type == 'supplier':
            AccountTypeM_UID = 200
            if accountM_uid not in [0, '']:
                element_name_contact = "AccountMContact"
                element_name_address = "AccountMAddress"
                element_name_contacts = "AccountMContacts"
                element_name_addresss = "AccountMAddresss"
                (accountMaddressList, accountMaddresssList,
                 AccountMContactList, AccountMContactsList) = find_new_record(accountMAddress, accountMContact)

                AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)

                accountMaddressXML = accountMaddress(accountMaddressList, decoded, element_name_address)
                accountMaddresssXML = accountMaddress(accountMaddresssList, decoded, element_name_addresss)

                AccountMContactXML = AccountMContacts(AccountMContactList, decoded, element_name_contact)
                AccountMContactsXML = AccountMContacts(AccountMContactsList, decoded, element_name_contacts)

                process, status, rval = svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
                                                   AccountMContactsXML, accountM_uid)

            else:
                element_name_contact = "AccountMContact"
                element_name_address = "AccountMAddress"
                AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)
                accountMaddressXML = accountMaddress(accountMAddress, decoded, element_name_address)
                AccountMContactXML = AccountMContacts(accountMContact, decoded, element_name_contact)
                process, status, rval = svt_insert(AccountMXML, accountMaddressXML, AccountMContactXML)
            return {"message": "Data " + process + " "+ status, "rval": rval}

        elif form_type == 'vendor':
            AccountTypeM_UID = 400
            if accountM_uid not in [0, '']:
                element_name_contact = "AccountMContact"
                element_name_address = "AccountMAddress"
                element_name_contacts = "AccountMContacts"
                element_name_addresss = "AccountMAddresss"
                (accountMaddressList, accountMaddresssList,
                 AccountMContactList, AccountMContactsList) = find_new_record(accountMAddress, accountMContact)

                AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)

                accountMaddressXML = accountMaddress(accountMaddressList, decoded, element_name_address)
                accountMaddresssXML = accountMaddress(accountMaddresssList, decoded, element_name_addresss)

                AccountMContactXML = AccountMContacts(AccountMContactList, decoded, element_name_contact)
                AccountMContactsXML = AccountMContacts(AccountMContactsList, decoded, element_name_contacts)

                process, status, rval = svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML,
                                                   AccountMContactXML, AccountMContactsXML, accountM_uid)

            else:
                element_name_contact = "AccountMContact"
                element_name_address = "AccountMAddress"
                AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)
                accountMaddressXML = accountMaddress(accountMAddress, decoded, element_name_address)
                AccountMContactXML = AccountMContacts(accountMContact, decoded, element_name_contact)
                process, status, rval = svt_insert(AccountMXML, accountMaddressXML, AccountMContactXML)
            return {"message": "Data " + process + " "+ status, "rval": rval}

        elif form_type == 'transport':
            AccountTypeM_UID = 500
            if accountM_uid not in [0, '']:
                element_name_contact = "AccountMContact"
                element_name_address = "AccountMAddress"
                element_name_contacts = "AccountMContacts"
                element_name_addresss = "AccountMAddresss"
                (accountMaddressList, accountMaddresssList,
                 AccountMContactList, AccountMContactsList) = find_new_record(accountMAddress, accountMContact)

                AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)

                accountMaddressXML = accountMaddress(accountMaddressList, decoded, element_name_address)
                accountMaddresssXML = accountMaddress(accountMaddresssList, decoded, element_name_addresss)

                AccountMContactXML = AccountMContacts(AccountMContactList, decoded, element_name_contact)
                AccountMContactsXML = AccountMContacts(AccountMContactsList, decoded, element_name_contacts)

                process, status, rval = svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
                                                   AccountMContactsXML, accountM_uid)

            else:
                element_name_contact = "AccountMContact"
                element_name_address = "AccountMAddress"
                AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)
                accountMaddressXML = accountMaddress(accountMAddress, decoded, element_name_address)
                AccountMContactXML = AccountMContacts(accountMContact, decoded, element_name_contact)
                process, status, rval = svt_insert(AccountMXML, accountMaddressXML, AccountMContactXML)

            return {"message": "Data " + process + " "+ status, "rval": rval}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': '+ str(e))
        return {"message": "Something Went Wrong", "rval": 0}


def find_new_record(accountMAddresslist, accountMContactlist):
    accountMAddress = [entry for entry in accountMAddresslist if entry["UID"] == 0]
    accountMAddresss = [entry for entry in accountMAddresslist if entry["UID"] != 0]
    accountMContact = [entry for entry in accountMContactlist if entry["UID"] == 0]
    accountMContacts = [entry for entry in accountMContactlist if entry["UID"] != 0]
    return (accountMAddress if len(accountMAddress) else '',
            accountMAddresss, accountMContact if len(accountMContact) else '', accountMContacts)


def svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
               AccountMContactsXML, accountM_uid):
    try:
        qry = """
                DECLARE @return_value int, 
                    @successful bit;
    
                SET NOCOUNT ON; 
                
                EXEC @return_value = [Canteen].[Bis_AccountM_Update]
                @AccountMInsert = ?, 
                @AccountMContactsInsert = ?,
                @AccountMContactsUpdate = ?, 
                @AccountMTermsInsert = ?,
                @AccountMTermsUpdate = ?, 
                @AccountMAgentInsert = ?,
                @AccountMAgentUpdate = ?, 
                @AccountMVolumeDescriptionInsert = ?, 
                @AccountMVolumeDescriptionUpdate = ?, 
                @AccountMTransPortInsert = ?, 
                @AccountMTransPortUpdate = ?, 
                @AccountMTransPortListInsert = ?, 
                @AccountMTransPortListUpdate = ?, 
                @AccountMTransportVehicleInsert = ?, 
                @AccountMTransportVehicleUpdate = ?, 
                @CompanyDetailsInsert = ?, 
                @CompanyDetailsUpdate = ?, 
                @CompanyDetailsContactactsInsert = ?, 
                @CompanyDetailsContactsUpdate = ?, 
                @AccountMTareCategoryInsert = ?, 
                @AccountMTareCategoryUpdate = ?, 
                @AccountMChargesInsert = ?, 
                @AccountMChargesUpdate = ?, 
                @AccountMAddressInsert = ?, 
                @AccountMAddressUpdate = ?, 
                @UID = ?, 
                @successful = @successful OUTPUT;
            
                SELECT @successful AS N'@successful';
                SELECT 'Return Value' = @return_value;
            """

        res = py_connection.call_prop_return_pk1(qry, (AccountMXML, AccountMContactXML, AccountMContactsXML,
                                                       '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                                                       '', '', '', '', '', '', accountMaddressXML,
                                                       accountMaddresssXML, accountM_uid))
        if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
            return 'Updated', 'successfully', 1
        else:
            return 'Updation', 'Failed', 0
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': '+ str(e))


def svt_insert(AccountMInsert, accountMaddressXML, AccountMContactXML):
    try:
        qry = """ 
                DECLARE @return_value int, 
                @successful bit
                SET NOCOUNT ON; 
    
                EXEC @return_value = [Canteen].[Bis_AccountM_Insert]
                @AccountMInsert = ?, 
                @AccountMContactsInsert = ?,
                @AccountMTermsInsert = ?,
                @AccountMAgentInsert = ?,
                @AccountMVolumeDescriptionInsert = ?,
                @AccountMTransPortInsert = ?,
                @AccountMTransPortListInsert = ?,
                @AccountMTransportVehicleInsert= ?,
                @CompanyDetailsInsert = ?,
                @CompanyDetailsContactactsInsert = ?,
                @AccountMTareCategoryInsert = ?,
                @AccountMChargesInsert = ?,
                @AccountMAddressInsert = ?,
                
                @successful = @successful OUTPUT
    
                SELECT @successful as N'@successful'
                SELECT 'Return Value' = @return_value
            """

        res = py_connection.call_prop_return_pk1(qry, (AccountMInsert, AccountMContactXML, '', '', '',
                                                       '', '', '', '', '', '', '', accountMaddressXML))
        if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
            return 'Inserted', 'successfully', 1
        else:
            return 'Insertion', 'Failed', 0
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': '+ str(e))
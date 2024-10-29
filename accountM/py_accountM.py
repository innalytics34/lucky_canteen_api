from accountM.xml_config import accountMaddress, AccountM, AccountMContacts
from db_connection import py_connection


def accountM(request, decoded):
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

            svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
                       AccountMContactsXML, accountM_uid)
            response = "updated"
        else:
            print("--------------6")
            element_name_contact = "AccountMContact"
            element_name_address = "AccountMAddress"
            AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)
            accountMaddressXML = accountMaddress(accountMAddress, decoded, element_name_address)
            AccountMContactXML = AccountMContacts(accountMContact, decoded, element_name_contact)
            svt_insert(AccountMXML, accountMaddressXML, AccountMContactXML)
            response = "inserted"
        return {"message": "Data " + response + " successfully", "rval": 1}

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

            svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
                       AccountMContactsXML, accountM_uid)
            response = "updated"
        else:
            element_name_contact = "AccountMContact"
            element_name_address = "AccountMAddress"
            AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)
            accountMaddressXML = accountMaddress(accountMAddress, decoded, element_name_address)
            AccountMContactXML = AccountMContacts(accountMContact, decoded, element_name_contact)
            svt_insert(AccountMXML, accountMaddressXML, AccountMContactXML)
            response = "inserted"
        return {"message": "Data " + response + " successfully", "rval": 1}

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

            svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
                       AccountMContactsXML, accountM_uid)
            response = "updated"
        else:
            element_name_contact = "AccountMContact"
            element_name_address = "AccountMAddress"
            AccountMXML = AccountM(accountM, decoded, AccountTypeM_UID)
            accountMaddressXML = accountMaddress(accountMAddress, decoded, element_name_address)
            AccountMContactXML = AccountMContacts(accountMContact, decoded, element_name_contact)
            svt_insert(AccountMXML, accountMaddressXML, AccountMContactXML)
            response = "inserted"
        return {"message": "Data " + response + " successfully", "rval": 1}


def find_new_record(accountMAddresslist, accountMContactlist):
    accountMAddress = [entry for entry in accountMAddresslist if entry["UID"] == 0]
    accountMAddresss = [entry for entry in accountMAddresslist if entry["UID"] != 0]
    accountMContact = [entry for entry in accountMContactlist if entry["UID"] == 0]
    accountMContacts = [entry for entry in accountMContactlist if entry["UID"] != 0]
    return (accountMAddress if len(accountMAddress) else '',
            accountMAddresss, accountMContact if len(accountMContact) else '', accountMContacts)


def svt_update(AccountMXML, accountMaddressXML, accountMaddresssXML, AccountMContactXML,
               AccountMContactsXML, accountM_uid):
    res = py_connection.put_result("{call Canteen.Bis_AccountM_Update"
        "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}",
        (AccountMXML, AccountMContactXML, AccountMContactsXML, '', '', '', '', '', '', '', '', '', '', '',
         '', '', '', '', '', '', '', '', '', accountMaddressXML, accountMaddresssXML, accountM_uid))


def svt_insert(AccountMInsert, accountMaddressXML, AccountMContactXML):
    print("-----------56")
    res = py_connection.put_result("{call Canteen.Bis_AccountM_Insert"
                             "(?,?,?,?,?,?,?,?,?,?,?,?,?)}",
                             (AccountMInsert, AccountMContactXML, '', '', '', '', '', '',
                              '', '', '', '', accountMaddressXML))













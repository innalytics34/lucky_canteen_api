from db_connection import py_connection


def cy():
    try:
        company = CompanyName()
        year = Year()
        print(year)
        return {"CompanyName": company, "Year": year}
    except Exception as e:
        print(str(e))


def CompanyName():
    try:
        qry = '{call canteen.bis_Lookup_CompanyName}'
        res, k = py_connection.call_prop_col_without_param(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                UID = view_data['UID']
                Description = view_data['Description']
                lst.append({"UID": UID, "Description": Description})
            return lst
        else:
            return lst
    except Exception as e:
        print(str(e))
        return []


def BranchName(request):
    try:
        qry = '{call canteen.bis_Lookup_BranchName(?)}'
        res, k = py_connection.call_prop1(qry, (request['comp_fk'],))
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                UID = view_data['UID']
                Description = view_data['Description']
                lst.append({"UID": UID, "Description": Description, "StateCode": view_data['StateCode']})
            return {"BranchName": lst}
        else:
            return {"BranchName": lst}
    except Exception as e:
        print(str(e))
        return {"BranchName": []}


def Year():
    try:
        qry = '{call canteen.bis_Lookup_FinancialYear}'
        res, k = py_connection.call_prop_col_without_param(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return lst
        else:
            return lst
    except Exception as e:
        print(str(e))
        return []

def UserName(request):
    try:
        qry = '{call canteen.bis_EmployeeM_Select_User(?)}'
        res, k = py_connection.call_prop1(qry, (request['branch_id'],))
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"UserName": lst}
        else:
            return {"UserName": lst}
    except Exception as e:
        print(str(e))
        return {"UserName": []}
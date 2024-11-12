from db_connection import py_connection


def ScreenRightsAsPerEmployee(screen_name, decoded):
    try:
        emp_fk = decoded['emp_fk']
        # emp_fk = 1000029
        # screen_name = 'Material Issue'
        if emp_fk in [1, 2]:
            permissions = {"Add": 1, "Edit": 1, "Delete": 1, "Amend": 1, "View": 1, "Print": 1}
        else:
            permissions = {"Add": 0, "Edit": 0, "Delete": 0, "Amend": 0, "View": 0, "Print": 0}
            permission_map = {
                1: "Add",
                2: "Edit",
                3: "Delete",
                4: "Amend",
                5: "View",
                6: "Print"
            }
            for i in permission_map:
                qry = '{call Core.[Bis_MenuRightsList_Select_ByMenuNameAndOption] (?,?,?)}'
                params = (emp_fk, screen_name, i)
                res, k = py_connection.call_prop1(qry, params)
                if res[0][0] == 1:
                    permissions[permission_map[i]] += 1

        return permissions
    except Exception as e:
        print(str(e))
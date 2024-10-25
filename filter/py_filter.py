from db_connection import py_connection

def department():
    try:
        qry = "select * from dbo.Web_task_department where is_active = 1"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"dept": lst}
        else:
            return {"dept": lst}
    except Exception as e:
        print(str(e))
        return {"dept": []}

def main_menu(decoded):
    try:
        role_fk = decoded.get("role_fk")
        print(role_fk)
        qry = ("select * from dbo.Web_task_menu where is_active = 1 and privilage LIKE "
               "") + "'%" + str(role_fk) + "%'"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"main_menu": lst}
        else:
            return {"main_menu": lst}

    except Exception as e:
        print(str(e))
        return {"main_menu": []}

def get_employee():
    try:
        qry = "select employee_pk,concat(first_name,' ',last_name) as emp_name from dbo.Web_task_employee"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"emp_list": lst}
        else:
            return {"emp_list": lst}

    except Exception as e:
        print(str(e))
        return {"main_menu": []}

def priority_list():
    try:
        qry = "select priority_pk,priority_name from dbo.Web_task_priority where is_active = 1"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"priority_list": lst}
        else:
            return {"priority_list": lst}

    except Exception as e:
        print(str(e))
        return {"priority_list": []}

def get_task_type():
    try:
        qry = "select tasktype_pk,tasktype_name from dbo.Web_task_tasktype where is_active = 1"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"task_type": lst}
        else:
            return {"task_type": lst}

    except Exception as e:
        print(str(e))
        return {"task_type": []}

def status_type():
    try:
        qry = "select status_pk,status_name from dbo.Web_task_taskstatus where is_active = 1"
        res, k = py_connection.get_result_col(qry)
        lst = []
        if res and len(res) > 0:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return {"status_type": lst}
        else:
            return {"status_type": lst}

    except Exception as e:
        print(str(e))
        return {"status_type": []}
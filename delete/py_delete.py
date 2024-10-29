from db_connection import py_connection
from delete import delete_config


def delete_data(request,  decoded):
    try:
        delete_type = request.get('delete_type')
        data = delete_config.delete_config.get(delete_type)
        response = get_proc(data, request, decoded)
        return {"data": response}
    except Exception as e:
        print(str(e))
        return {"message": "Something went wrong!", "rval": 0}


def get_proc(data, request, decoded):
    params = data['params']
    if len(params) > 0:
        data_lst, param_lst = get_params(data['params'], request, decoded)
        proc = "{call canteen." + data["data_source"] + "(" + ','.join(param_lst) + ")}"
        py_connection.put_result(proc, tuple(data_lst))
        return {"message": "Data deleted successfully", "rval": 1}
    else:
        proc = "{call canteen.{0}}".format(data['data_source'])
        py_connection.put_result_with_data(proc)
        return {"message": "Data deleted successfully", "rval": 1}


def get_params(params, request, decoded):
    data_lst = []
    param_lst = []
    for row in params:
        if row['source'] == "request":
            data_lst.append(request[row["label"]])
            param_lst.append('?')
        else:
            data_lst.append(decoded[row["label"]])
            param_lst.append('?')
    return data_lst, param_lst



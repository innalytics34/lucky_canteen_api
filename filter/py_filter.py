from db_connection import py_connection
from filter.config import filter_config


def get_lookup(request,  decoded):
    try:
        print(request, "---------t")
        lookup_type = request.get('lookup_type')
        data = filter_config.get(lookup_type)
        print(data)
        response = get_proc(data, request, decoded)
        return {"data": response}
    except Exception as e:
        print(str(e))


def get_proc(data, request, decoded):
    params = data['params']
    if len(params) > 0:
        data_lst, param_lst = get_params(data['params'], request, decoded)
        proc = "{call canteen." + data["data_source"] + "(" + ','.join(param_lst) + ")}"
        res, k = py_connection.call_prop1(proc, tuple(data_lst))
        lst = []
        if res:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return lst
        else:
            return lst
    else:
        proc = "{{call canteen.{0}}}".format(data['data_source'])
        print(proc)
        res, k = py_connection.get_result_col(proc)
        lst = []
        if res:
            for row in res:
                view_data = dict(zip(k, row))
                lst.append(view_data)
            return lst
        else:
            return lst


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



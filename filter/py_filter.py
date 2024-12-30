from db_connection import py_connection
from filter.config import filter_config
import os
from logger.logger_config import logger
import inspect

directory = os.path.dirname(os.path.abspath(__file__))


def get_lookup(request,  decoded):
    try:
        lookup_type = request.get('lookup_type')
        data = filter_config.get(lookup_type)
        response = get_proc(data, request, decoded)
        return {"data": response}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))



def get_proc(data, request, decoded):
    try:
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
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))


def get_params(params, request, decoded):
    try:
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
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))


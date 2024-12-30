from db_connection import py_connection
from sidebar.user_rights import ScreenRightsAsPerEmployee
from logger.logger_config import logger
import inspect
import os

directory = os.path.dirname(os.path.abspath(__file__))

def GetMenu(decoded):
    try:
        # emp_fk = decoded.get('user_id')
        emp_fk = 1
        if emp_fk in [1, 2]:
            main_menu = GetMenuNames()
            lst = main_menu['main_menu']
        else:
            menus = GetMenuNames()

            def build_menu(menu_list):
                result = []
                for menu in menu_list:
                    text = menu['text']
                    is_menu = GetMenuBasedOnRights(emp_fk, text)

                    if is_menu == 1:
                        if 'items' in menu and menu['items']:
                            items = build_menu(menu['items'])
                            menu_dict = {
                                "text": text,
                                "path": menu['path'],
                                "icon": menu['icon']
                            }
                            if items:
                                menu_dict["items"] = items
                            menu_dict["rights"] = ScreenRightsAsPerEmployee(text, decoded)
                            result.append(menu_dict)
                        else:
                            result.append({
                                "text": text,
                                "path": menu['path'],
                                "icon": menu['icon'],
                                "rights": ScreenRightsAsPerEmployee(text, decoded)
                            })

                return result
            lst = build_menu(menus['main_menu'])
            print(lst)
        return {"main_menu": lst}
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"main_menu": []}


def GetMenuNames():
    try:
        qry = ("SELECT menupk, menu_description as 'text', path, icon, sublist_fk "
               "FROM canteen.SideBar WHERE is_active in (1)"
               "ORDER BY [order] ASC")
        res, k = py_connection.get_result_col(qry)
        menu_dict = {}
        for row in res:
            menu_item = dict(zip(k, row))
            menu_dict.setdefault(row[k.index('sublist_fk')], []).append(menu_item)

        def build_sublist(menu_fk):
            sublist = []
            if menu_fk in menu_dict:
                for item in menu_dict[menu_fk]:
                    item['items'] = build_sublist(item['menupk'])
                    keys = ['menupk', 'sublist_fk']
                    for key in keys:
                        item.pop(key, None)
                    if item['items'] in ([], '', None):
                        item.pop('items')
                    sublist.append(item)
            return sublist

        menu = build_sublist(0)
        return {"main_menu": menu}

    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))
        return {"main_menu": []}


def GetMenuBasedOnRights(emp_fk, menu):
    try:
        qry = '{call canteen.bis_MenuRightsList_Select_ByUserIdAndMenuName (?,?)}'
        res, k = py_connection.call_prop1(qry, (emp_fk, menu))
        if res and len(res) > 0:
            return res[0][0]
        else:
            return 0
    except Exception as e:
        print(str(e))
        function_name = inspect.currentframe().f_code.co_name
        logger.error(directory + '|' + str(function_name) + ': ' + str(e))

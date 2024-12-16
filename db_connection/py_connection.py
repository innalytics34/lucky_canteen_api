import pyodbc
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)


def get_mssql_connection():
    try:

        conn = pyodbc.connect('DRIVER={' + os.getenv("DRIVER") + '};SERVER=' + os.getenv("HOST") + ';DATABASE=' + os.getenv("DB") + ';UID=' + os.getenv("USER") +';PWD=' + os.getenv(
            "PASSWORD") + '')
        return conn
    except Exception as e:
        print("get_mssql_connection " + str(e))


def get_result(query):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query)
    row = cursor_str.fetchall()
    mssql_conn.close()
    return row


def get_result_col(query):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def put_result(query, data):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query, data)
    mssql_conn.commit()
    mssql_conn.close()
    return ''


def put_result_with_data(query):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(query)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def put_result_exe_many(qry, pram):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.executemany(qry, pram)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def call_prop(qry, params):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry, params)
    mssql_conn.commit()
    mssql_conn.close()
    return cursor_str.rowcount


def call_prop_col(qry, params):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry, params)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def call_prop1(qry, params):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry, params)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def call_prop_return_pk(qry, params):
    mssql_conn = get_mssql_connection()
    cursor = mssql_conn.cursor()
    cursor.execute(qry, params)
    output_id = cursor.fetchone()[0]
    mssql_conn.commit()
    mssql_conn.close()
    return output_id


def call_prop_col_without_param(qry):
    mssql_conn = get_mssql_connection()
    cursor_str = mssql_conn.cursor()
    cursor_str.execute(qry)
    row = cursor_str.fetchall()
    column_names = [column[0] for column in cursor_str.description]
    mssql_conn.close()
    return row, column_names


def call_prop_return_pk1(qry, params):
    mssql_conn = get_mssql_connection()
    cursor = mssql_conn.cursor()
    cursor.execute(qry, params)

    results = []
    try:
        # Fetch all rows from the first result set
        if cursor.description:  # Check if there's a result set
            results.append(cursor.fetchall())
        else:
            print("No initial result set.")

        # Process additional result sets
        while cursor.nextset():
            if cursor.description:  # Check if the next result set has rows
                results.append(cursor.fetchall())
                print(cursor.fetchall(), '123')
                # return output_id
            else:
                print("No further result sets.")

        # Fetch the output ID if present
        if cursor.description:  # Final check for a row result
            output_id = cursor.fetchone()[0]
            print(output_id, '011')
        else:
            output_id = None
            print(output_id, '090')
    except pyodbc.ProgrammingError as e:
        print(f"ProgrammingError: {e}")
        output_id = None
    finally:
        mssql_conn.commit()
        mssql_conn.close()

    print(results, output_id, '234567')
    return results, output_id
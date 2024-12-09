from db_connection import py_connection
from datetime import datetime as dt
from login.py_dropdown import Year

def RawMaterialOpeningStock(request, decoded):   # ADDD1 --- decimal, ADDI1 --- int, ADDT1 --- varchar, ADDDT1 -- datetime
    try:                                         # DocumentTypeId: 80100
        print(request, '008')
        if request['type'] == 'Insert':
            sp = 'bis_RawMaterialOpeningStock_Insert'
        else:
            sp = 'bis_RawMaterialOpeningStock_Update'
        qry = ('{call Canteen.'+ sp +' (?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?,?,?,?,'
               '?,?)}')
        params = (request["UID"], decoded["branch_id"], decoded["user_id"], Year()[0]["Yr"], request["LongDocumentNo"],
                  request["DocumentDate"], request["DocumentTypeID"], request["BatchID"], request["ItemID"], request["ItemDescription"],
                  request["PartNo"], request["UOMID"], request["Uom"], request["BaseUOMID"], request["BaseUom"],
                  request["BaseUOMQty"], request["Qty"], request["TotalQty"], request["Price"], request["Remarks"],
                  request["Status"], decoded["user_id"], dt.now(), decoded["user_id"], dt.now(),
                  request["LocationID"], request["Location"], request["ADDD1"], request["ADDD2"], request["ADDD3"],
                  request["ADDD4"], request["ADDD5"], request["ADDI1"], request["ADDI2"], request["ADDI3"],
                  request["ADDI4"], request["ADDI5"], request["ADDT1"], request["ADDT2"], request["ADDT3"],
                  request["ADDT4"], request["ADDT5"], request["ADDDT1"], request["ADDDT2"], request["ADDDT3"],
                  request["ADDDT4"], request["ADDDT5"])
        print(params, '01011')
        res = py_connection.call_prop(qry, params)
        print(res, '---')
        action = "Inserted" if request['type'] == 'Insert' else "Updated"
        status = "Successfully" if res == -1 else "Failed"
        rval = 1 if res == 1 else 0
        return {"message": "Raw Material Opening Stock Details " + str(action) + ' '+ str(status), "rval": rval}
    except Exception as e:
        print(str(e))

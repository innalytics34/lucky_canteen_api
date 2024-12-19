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
        qry = """ 
            DECLARE @return_value int,
            @UID int

            SET NOCOUNT ON; 

            EXEC @return_value = [Canteen].[""" + sp + """]
            @UID = ?, 
            @BranchID = ?, 
            @LogOnUser = ?, 
            @Year = ?, 
            @LongDocumentNo = ?,
            @DocumentDate = ?, 
            @DocumentTypeID = ?, 
            @BatchID = ?, 
            @ItemID = ?, 
            @ItemDescription = ?,
            @PartNo = ?, 
            @UOMID = ?,
            @UOM = ?, 
            @BaseUOMID = ?, 
            @BaseUOM = ?,
            @BaseUOMQty = ?, 
            @Qty = ?, 
            @TotalQty = ?, 
            @Price = ?, 
            @Remarks = ?,
            @Status = ?, 
            @CreatedBy = ?, 
            @CreatedDate = ?, 
            @UpdatedBy = ?,
            @UpdatedDate = ?,
            @LocationID = ?, 
            @Location = ?, 
            @ADDD1 = ?, 
            @ADDD2 = ?, 
            @ADDD3 = ?,
            @ADDD4 = ?, 
            @ADDD5 = ?, 
            @ADDI1 = ?, 
            @ADDI2 = ?,
            @ADDI3 = ?,
            @ADDI4 = ?, 
            @ADDI5 = ?, 
            @ADDT1 = ?, 
            @ADDT2 = ?, 
            @ADDT3 = ?,
            @ADDT4 = ?, 
            @ADDT5 = ?, 
            @ADDDT1 = ?, 
            @ADDDT2 = ?, 
            @ADDDT3 = ?, 
            @ADDDT4 = ?, 
            @ADDDT5 = ?

            SELECT	@UID as N'@UID'
            SELECT	'Return Value' = @return_value
        """
        print(qry, '1234')
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
        print(params, '1234')
        res = py_connection.call_prop_return_pk1(qry, params)
        print(res, '1234567')
        if request['type'] == 'Insert':
            if res and len(res[0]) > 1 and len(res[0][1]) > 0 and res[0][1][0][0]:
                return {"message": "Raw Material Opening Stock Inserted Successfully", "rval": 1}
            else:
                return {"message": "Raw Material Opening Stock Insertion Failed", "rval": 0}
        else:
            if res and len(res[0]) > 1 and len(res[0][0]) > 0 and res[0][0][0][0]:
                return {"message": "Raw Material Opening Stock Updated Successfully", "rval": 1}
            else:
                return {"message": "Raw Material Opening Stock Updation Failed", "rval": 0}

    except Exception as e:
        print(str(e))
        return {"message": "Something Went Wrong ", "rval": 0}

from flask import Flask, request
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/bank/transfer', methods=['PUT'])
def transfer_money():

    fno = int(request.form.get('fromacc'))
    tno = int(request.form.get('toacc'))
    amt = float(request.form.get('amount'))

    dic = {}

    try:
        con = pymysql.connect(host='HOST_NAME',port='PORT_NUM',user='USER_NAME',password='PASSWORD',database='DB_NAME')
        curs=con.cursor()

        curs.execute(f"UPDATE accounts set balance=balance-{amt} WHERE accno={fno}")

        if curs.rowcount == 0:
            return {"message": "From Account Not Found! "}, 404



        # Check Constraint >= 500
        curs.execute(f"UPDATE accounts set balance=balance+{amt} WHERE accno={tno}")

        if curs.rowcount == 0:
            return {"message": "To Account Not Found"}, 404



        con.commit()

        dic['message']= 'Tarnsfer Successful',

        con.close()

    except Exception as e :
        print(e)
        dic['message']= str(e)

    return dic

app.run(debug=True)
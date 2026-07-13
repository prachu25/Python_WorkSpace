from flask import Flask, request
import pymysql

app=Flask(__name__)

@app.route('/doctor/add', methods=['POST'])
def add_doctor():
    did=int(request.form.get("docid"))
    dnm=request.form.get("docnm")
    spl=request.form.get("spec")
    dic={}

    try:
        con = pymysql.connect(host='HOST_NAME',port='PORT_NUM',user='USER_NAME',password='PASSWORD',database='DB_NAME')
        curs=con.cursor()
        curs.execute(f"insert into doctors values({did}, '{dnm}', '{spl}') ")
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'

    
    return dic

app.run(debug=True)




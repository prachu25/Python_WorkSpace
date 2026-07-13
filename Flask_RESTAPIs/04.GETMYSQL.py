from flask import Flask,jsonify
import pymysql

app=Flask(__name__)

@app.route('/patients',methods=['GET'])
def getallpatients():
    con = pymysql.connect(host='HOST_NAME',port='PORT_NUM',user='USER_NAME',password='PASSWORD',database='DB_NAME')
    curs=con.cursor()
    curs.execute("select * from patients")
    data=curs.fetchall()
    curs.close()
    con.close()
    return jsonify(data)

app.run(debug=True)




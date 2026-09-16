from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

@app.route('/account/delete/<_id>', methods = ['DELETE'])
def delete_account(_id):

    try:
        connection = pymysql.connect(                # put  your orginal value
            host="HOST_NAME",
            port="PORT",
            user="USER_NAME",
            password="PASSWORD",
            database="DB_NAME"
            )

        cursor = connection.cursor()
        cursor.execute(
            "delete from accounts where accno = %s", (_id)
        )

        # WE CAN ALSO DELETE THIS WAY.
#       cursor.execute(
#           f"DELETE FROM accounts WHERE accno = {_id}"
#       )


        connection.commit()

        if cursor.rowcount == 0:
            connection.close()
            return jsonify({
                'Erorr': "account Not Found!"
            }), 404


        connection.close()

        return jsonify({
            "msg": "account deleted successfully!"
        })

    except  Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


app.run(debug= True)
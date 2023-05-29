import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/create', methods=['POST'])
def create_cus():
    try:        
        _json = request.json
        first_name = _json['first_name']
        last_name = _json['last_name']
        email = _json['email']
        phone_number = _json['phone_number']
        if first_name and last_name and email and phone_number and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO customers(first_name, last_name, email, phone_number) VALUES(%s, %s, %s, %s)"
            bindData = ( first_name, last_name, email, phone_number)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Customer added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          
     
@app.route('/customers')
def cus():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT customer_id, first_name, last_name, email, phone_number FROM customers")
        cusRows = cursor.fetchall()
        respone = jsonify(cusRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/customers/<int:cus_id>', methods=['GET'])
def cus_details(cus_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT customer_id, first_name, last_name, email, phone_number FROM customers WHERE customer_id =%s", cus_id)
        cusRow = cursor.fetchone()
        respone = jsonify(cusRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/update', methods=['PUT'])
def update_cus():
    try:
        _json = request.json
        customer_id = _json['customer_id']
        first_name = _json['first_name']
        last_name = _json['last_name']
        email = _json['email']
        phone_number = _json['phone_number']
        if customer_id and first_name and last_name and email and phone_number and request.method == 'PUT':			
            sqlQuery = "UPDATE customers SET first_name=%s, last_name=%s, email=%s, phone_number=%s WHERE customer_id=%s"
            bindData = ( first_name, last_name, email, phone_number,customer_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Customer updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/delete/<int:cus_id>', methods=['DELETE'])
def delete_cus(customer_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM emp WHERE customer_id =%s", (customer_id,))
		conn.commit()
		respone = jsonify('Customer deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()
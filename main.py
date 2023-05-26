import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/create', methods=['POST'])
def create_cus():
    try:        
        _json = request.json
        customer_id = _json['name']
        firstname = _json['firstname']
        lastname = _json['lastname']
        email = _json['email']
        phonenumber = _json['phone']
        if customer_id and firstname and lastname and email and phonenumber and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO cus(firstname, lastname, email, phonenumber, customer_id) VALUES(%s, %s, %s, %s)"
            bindData = (customer_id, firstname, lastname, email, phonenumber)            
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
     
@app.route('/cus')
def cus():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT customer_id, firstname, lastname, email, phonenumber FROM cus")
        cusRows = cursor.fetchall()
        respone = jsonify(cusRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/cus/')
def emp_details(cus_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT customer_id, name, email, phone, address FROM cus WHERE id =%s", cus_id)
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
def update_emp():
    try:
        _json = request.json
        customer_id = _json['id']
        firstname = _json['firstname']
        lastname = _json['lastname']
        email = _json['email']
        phonenumber = _json['phonenumber']
        if firstname and lastname and email and phonenumber and customer_id and request.method == 'PUT':			
            sqlQuery = "UPDATE emp SET name=%s, email=%s, phone=%s, address=%s WHERE id=%s"
            bindData = (firstname, lastname, email, phonenumber, customer_id,)
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

@app.route('/delete/', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM emp WHERE id =%s", (id,))
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
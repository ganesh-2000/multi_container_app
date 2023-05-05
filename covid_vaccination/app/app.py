from flask import Flask, request
import os
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify


app = Flask(__name__)


mysql = MySQL()


mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'first'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT']=int('3306')
mysql.init_app(app)

conn = mysql.connect()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        with conn.cursor() as cur:
            cur.execute("""
                SELECT name,vaccinated
                FROM student
                WHERE reg_no = %s
            """, (reg_no,))
            result = cur.fetchone()
            if result:
                name = result[0]
                vaccinated = result[1]
                status = 'vaccinated' if vaccinated else 'not vaccinated'
                return f'{name} with registration number {reg_no} is {status}'
            else:
                return f'Student with registration number {reg_no} is not found'
    else:
        return '''
            <form method="POST">
                <label>Registration Number:</label>
                <input type="text" name="reg_no" required>
                <button type="submit">Submit</button>
            </form>
        '''


"""
@app.route("/")
def main():
    return "Welcome!"


@app.route('/how are you')
def hello():
    return 'I am good, how about you?'


@app.route('/read from database')
def read():
    conn = mysql.connect()


    cursor = conn.cursor(pymysql.cursors.DictCursor)


    cursor.execute("SELECT * FROM employees1")
    row = cursor.fetchone()
    result = []
    while row is not None:
      row = cursor.fetchone()
      result.append(row)


      return ','.join(str(result)[1:-1])
    #   for column in row:
    #       result.append(column)
     
      
    cursor.close()
    conn.close()
    
    # return ','.join(','.join(map(str, l)) for l in result)
    return ",".join(result)


@app.route('/all users')
def users():
    conn = mysql.connect()


    cursor = conn.cursor(pymysql.cursors.DictCursor)


    cursor.execute("SELECT * FROM employees1")


    rows = cursor.fetchall()


    resp = jsonify(rows)
    resp.status_code = 200
    cursor.close()
    conn.close()


    return resp
"""

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')



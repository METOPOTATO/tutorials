from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'linh'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'db_site'


@app.route('/')
def hello_geek():
    cur = mysql.connection.cursor()
    cur.execute('select * from users')
    data = cur.fetchall()
    cur.close()
    return data





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
    
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'amalraj123'
app.config['MYSQL_DATABASE_DB'] = 'mysql'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
@app.route('/', methods=['GET', 'POST'])
def search():
 if request.method == "POST":
 book = request.form['book']
 cursor.execute("SELECT * from finds WHERE name LIKE %s", (book))
 conn.commit()
 data = cursor.fetchall()
 if len(data) == 0 and book == 'all':
 cursor.execute("SELECT * from finds WHERE name LIKE %s", (book))
 conn.commit()
 data = cursor.fetchall()
 return render_template('search.html', data=data)
 return render_template('search.html')
@app.route('/amal', methods=['GET', 'POST'])
def amal():
return render_template('amal.html')
if __name__ == '__main__':
 app.debug = True
app.run()

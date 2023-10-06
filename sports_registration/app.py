from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

SPORTS = ["Tennis", "Football", "Basketball", "Air Rifle Shooting"]

@app.route('/')
def index():
    return render_template('index.html', sports = SPORTS)


@app.route('/register', methods=['POST'])
def register():
    # Server side validation
    name = request.form.get('name')
    sport = request.form.get('sport')
    if name and sport in SPORTS:
        cursor = mysql.connection.cursor()
        cursor.execute("select * from registrant where name=%s and sport=%s", 
                        (name, sport))
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            return render_template('error.html', message = "Already registered")   
        cursor.execute("INSERT INTO registrant (name, sport) VALUES (%s, %s)", 
                        (name, sport))
        mysql.connection.commit()
        cursor.close()
        return redirect('/registrants')
    else:
        if not name:
            return render_template('error.html', message = "Missing name")
        elif not sport:
            return render_template('error.html', message = "Missing sport")
        elif sport not in SPORTS:
            return render_template('error.html', message = "Invalid sport. Stop hacking")
        

@app.route('/registrants')
def registrants():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from registrant")
    registrants = cursor.fetchall()
    cursor.close()
    return render_template('registrants.html', registrants = registrants)


@app.route('/deregister', methods=['POST'])
def deregister():
    id = request.form.get('id')
    if id:
        cursor = mysql.connection.cursor()
        cursor.execute("delete from registrant where id=%s", (id,))
        mysql.connection.commit()
        cursor.close()
        return redirect('/registrants')
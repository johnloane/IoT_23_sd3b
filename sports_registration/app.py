from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
print(os.getenv('MYSQL_USER'))
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'sd3b_sports_registration_23'

mysql = MySQL(app)

SPORTS = ["Tennis", "Football", "Basketball", "Air Rifle Shooting"]
REGISTRANTS = {}
for sport in SPORTS:
    REGISTRANTS[sport] = []

@app.route('/')
def index():
    return render_template('index.html', sports = SPORTS)


@app.route('/register', methods=['POST'])
def register():
    # Server side validation
    name = request.form.get('name')
    sport = request.form.get('sport')
    if name and sport in SPORTS:
        if not name in REGISTRANTS[sport]:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO registrant (name, sport) VALUES (%s, %s)", 
                           (name, sport))
            mysql.connection.commit()
            cursor.close()
        return render_template('registrants.html', registrants=REGISTRANTS)
    else:
        if not name:
            return render_template('error.html', message = "Missing name")
        elif not sport:
            return render_template('error.html', message = "Missing sport")
        elif sport not in SPORTS:
            return render_template('error.html', message = "Invalid sport. Stop hacking")
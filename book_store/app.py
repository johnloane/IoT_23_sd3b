from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

Session(app)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/')
def index():
    # Gursimar suggested taking outside the route and doing once and caching
    # Joseph suggested using database class and keeping the connection open
    # throughout the whole session
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM book')
    books = cursor.fetchall()
    cursor.close()
    return render_template('index.html', books=books)


@app.route("/addtocart", methods=["GET", "POST"])
def addtocart():
    if session.get("cart") is None:
        session["cart"] = []
    if request.method == "POST":
        id = request.form.get("book_id")
        if id:
            session["cart"].append(request.form.get("book_id"))
        return redirect("/addtocart")
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM book where id in %s', [session['cart']])
        books = cursor.fetchall()
        cursor.close()
        return render_template("cart.html", books=books)
    
@app.route("/removefromcart", methods=["POST"])
def removefromcart():
    id = request.form.get("book_id")
    if id:
        session["cart"].remove(id)
        if len(session["cart"]) > 0:
            return 
        else:
            return redirect("/")


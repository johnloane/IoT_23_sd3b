from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Remember that the user logged in
        # Redirect to /
        email = request.form.get("email")
        session["email"] = email
        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session["email"] = None
    return redirect("/")

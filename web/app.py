from flask import Flask, render_template, request, redirect, session
from database import songs
from auth import login_required
from config import ADMIN_USER, ADMIN_PASS

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["user"] == ADMIN_USER and request.form["pass"] == ADMIN_PASS:
            session["user"] = ADMIN_USER
            return redirect("/")
    return render_template("login.html")

@app.route("/")
@login_required
def dashboard():
    data = list(songs.find())
    return render_template("dashboard.html", songs=data)

app.run(host="0.0.0.0", port=8080)

from flask import Flask, request, redirect, render_template, flash
import twilio.twiml
import os
from send_sms import *
from validation import *
from db import *
import psycopg2

# from validation import *

app = Flask(__name__)
app.secret_key = 'some_secret'

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}


@app.route("/", methods=['GET', 'POST'])
def hello():
    """Respond and greet the caller by name."""
    if request.method == "POST":
        from_number = request.values.get('From')
        if from_number in callers:
            message = callers[from_number] + ", thanks for the message!"
        else:
            message = "Thanks for the message!"

        resp = twilio.twiml.Response()
        resp.message(message)

        return str(resp)
    if request.method == "GET":
        return render_template("index.html")

@app.route("/send_message", methods=['GET', 'POST'])
def send_message():
    if request.method == "GET":
        return render_template("send_sms.html")
    if request.method == "POST":
        try:
            send_sms(request.form["your_number"], request.form["recipient_number"], request.form["msg"])
        finally:
            return redirect("/send_message")

@app.route("/login", methods=['GET',"POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(password)
        print(hashedpassword(username))
        bcrypt.checkpw(password.encode("utf-8"), hashedpassword(username).encode("utf-8")) == hashed
        return render_template("register.html")

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        password_confirmation = request.form["password_confirm"]
        if email_is_valid(email) and username_is_valid(username) and password_is_valid(password) and password_confirm(password, password_confirmation):
            try:
                registerUser(email, username, password)
            except psycopg2.IntegrityError as e:
                flash(str(e))
                return redirect("/register")
            return redirect("/login")


@app.route("/schedule", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("schedule.html", events=allEvents())
    else:
        registerEvent(request.form['team1-id'],request.form['team2-id'],request.form['datetime'],request.form['type'])
        return redirect("/")

@app.route("/teams/", methods=["GET", "POST"])
def teams():
    if request.method == "GET":
        return render_template("teams.html", teams=allTeams())
    else:
        registerTeam(request.form['team-name'])
        return redirect("/teams/")

@app.route("/teams/new/", methods=["GET"])
def newTeam():
    return render_template("create.html")

@app.route("/events/new/", methods=["GET"])
def newEvent():
    return render_template("event_form.html")














if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

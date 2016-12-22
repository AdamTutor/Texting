from flask import Flask, request, redirect, render_template, flash, Response
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import twilio.twiml
import os
from send_sms import *
from validation import *
from db import *
import psycopg2
from api import *

# from validation import *

app = Flask(__name__)
app.secret_key = secret_key
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



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
@login_required
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
        user = User.getByUsername(username)
        if bcrypt.checkpw(password.encode("utf-8"), user.hashedpassword.encode("utf-8")):
            login_user(user)
            flash("Login successful")
            return redirect("/schedule")
        else:
            flash("invalid credentials")
            return render_template("login.html")

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
                user = User.create(email, username, password)
                login_user(user)
                flash("logged in succesfully!")
            except psycopg2.IntegrityError as e:
                flash(str(e))
                return redirect("/register")
            return redirect("/login")
        else:
            flash("invalid credentials")
            return redirect("/register")


@app.route("/schedule", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        return render_template("schedule.html", events=Event.allEvents())
    else:
        Event.registerEvent(request.form['team1-id'],request.form['team2-id'],request.form['datetime'],request.form['type'])
        return redirect("/")

@app.route("/teams/", methods=["GET", "POST"])
@login_required
def teams():
    if request.method == "GET":
        return render_template("teams.html", teams=Team.allTeams())
    else:
        Team.registerTeam(request.form['team-name'])
        return redirect("/teams/")

@app.route("/teams/new/", methods=["GET"])
@login_required
def newTeam():
    return render_template("create.html")

@app.route("/events/new/", methods=["GET"])
@login_required
def newEvent():
    return render_template("event_form.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")













if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

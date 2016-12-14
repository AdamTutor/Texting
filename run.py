from flask import Flask, request, redirect, render_template
import twilio.twiml
import os
from send_sms import *
from validation import *

app = Flask(__name__)

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
    if request.method = "GET":
        return render_template("login.html")
    if request.method = "POST":
        return render_template("user.html")

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        render_template(register.html)

@app.route("/validation", methods=['GET', 'POST'])
def validation():
    if request.method = "POST":










if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

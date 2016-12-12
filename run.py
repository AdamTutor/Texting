from flask import Flask, request, redirect, render_template
import twilio.twiml
import os
from send_sms import *

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

@app.route("/", methods=['GET', 'POST'])
def root():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    message_text = request.values
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message, message_text=message_text)

    return render_template("response.html")

@app.route("/send_message", methods=['GET', 'POST'])
def send_message():
    if request.message == "GET":
        render_template("response.html")
    if request.message == "POST":
        send_sms(request.form["your_number"], request.form["recipient's_number"], request.form("msg"))
        return redirect("/send_message")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

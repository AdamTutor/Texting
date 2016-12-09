from flask import Flask, request, redirect
import twilio.twiml
from api import sid, key, number, my_number

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    my_number: "Curious George"
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

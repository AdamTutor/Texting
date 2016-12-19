from api import *

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = sid
auth_token  = key
client = TwilioRestClient(account_sid, auth_token)

# A list of message objects with the properties described above
messages = client.messages.list()

# for m in messages:
#    print(m["from"], m["to"],m["body"])

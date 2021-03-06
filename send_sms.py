from twilio.rest import TwilioRestClient
from api import sid, key, my_number, number
# Find these values at https://twilio.com/user/account
#
# POST https://api.twilio.com/2010-04-01/Accounts/AC123456abc/Messages


account_sid = sid
auth_token = key
client = TwilioRestClient(account_sid, auth_token)

def send_sms(my_phone_number, recipient, msg):
    message = client.messages.create(to=my_phone_number, from_=recipient,
                                     body=msg)


def send_mms(my_nmber, number, media_url):
    message = client.messages.create(to=my_number, from_=number,
                                     body="Hello there!",
                                     media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])

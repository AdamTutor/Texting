import os
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException


class Texting:
    def __init__(self, account_sid, auth_token, sender, recipient):
        try:
            self.client = TwilioRestClient(account_sid, auth_token)
        except:
            print("Incorrect credentials")
        self.sender = sender
        self.recipient = recipient


    def Send_message(self):
        """Takes in a object with proper credentials and sends a text message baised on the objects credentials"""

        msg_body = raw_input('What would you like to say? ')
        self.client.messages.create(body=msg_body,
            to=self.recipient,    # Replace with the number you intend to send the message to.
            from_=self.sender)    # Replace with your twilio number

if __name__ == '__main__':
    # Checks for credentials file, if file exits its read and information is inputed for you.
    if os.path.exists('credentials.txt'):
        with open("credentials.txt", 'r') as Credential_file:
            credentials = Credential_file.readlines()
            T = Texting(credentials[0].strip(),
                        credentials[1].strip(),
                        credentials[2].strip(),
                        credentials[3].strip())
            T.Send_message()
    # If credentials file is nonexistant, info is asked for and a file called "Credentials.txt" is created.
    else:
        account_sid = raw_input('Account SID: ')
        auth_token = raw_input('Auth Token: ')
        sender = raw_input('Sender: ')
        recipient = raw_input('Recipient: ')
        T = Texting(account_sid, auth_token, sender, recipient)
        T.Send_message()
        with open("credentials.txt", "w") as credentials:
            new_text = "{}\n{}\n{}\n{}".format(account_sid, auth_token, sender, recipient)
            credentials.write(new_text)

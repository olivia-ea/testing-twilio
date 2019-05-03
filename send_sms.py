import os
from twilio.rest import Client

account_sid = os.environ['TWILIOSID']
auth_token = os.environ['AUTHTOKEN']

client = Client(account_sid, auth_token)

# outbound SMS (twilio->personal)
client.messages.create(
    to = '+15106487309',
    from_ = '+15106171282',
    body = "This is Twilio!"
    )


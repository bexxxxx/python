#!python2

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "find via site"
# Your Auth Token from twilio.com/console
auth_token  = "find via site"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+18457507037", 
    from_="+15185201324",
    body="Hello from Python, bitch!!!!")

print(message.sid)

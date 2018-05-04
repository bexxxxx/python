#!python2

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "find via site"
# Your Auth Token from twilio.com/console
auth_token  = "find via site"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+1", 
    from_="+1,
    body="Hello from Python")

print(message.sid)

#!python2

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC50d94cc3626fbfd15d96f53b7ab5b350"
# Your Auth Token from twilio.com/console
auth_token  = "430b76e42200f89891610642ac2f40c7"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+18457507037", 
    from_="+15185201324",
    body="Hello from Python, bitch!!!!")

print(message.sid)

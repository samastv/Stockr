import os
from twilio.rest import Client

account_sid = "AC8fd63df00574019dbda6715689f7ff98"
auth_token = "7a15986bc486db56854eaa17e64fa655"

client = Client(account_sid, auth_token)

client.messages.create(
	to="5105095903",
	from_="5109624069",
	body="yo"
)
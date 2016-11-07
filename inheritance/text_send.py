from twilio.rest import TwilioRestClient

account_sid='AC61add779dfcc410c942379f5e188c8d7'
auth_token='df51084d7b6c91289f77a4be05757597'
client = TwilioRestClient(account_sid,auth_token)

message = client.messages.create(to='+16178708718',from_ ='+16175539261',body='你还不去买菜')

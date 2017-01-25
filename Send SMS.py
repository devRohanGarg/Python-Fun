from twilio.rest import TwilioRestClient
# Credentials
ACCOUNT_SID = 'AC3718fb710c140606395e02f699a24913'
AUTH_TOKEN = 'b1a26bddece928470457de13e5e597b3'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
        to = '+919451560054',
        from_ = '+19804043344',
        body = ':)',
)



# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Input phone number and message
to_phone_number = '+1234567890'  # Replace with the recipient's phone number
message = 'Hello, this is a test message.'

# Send the SMS
message = client.messages.create(
    body=message,
    from_='+your_twilio_phone_number',  # Replace with your Twilio phone number
    to=to_phone_number
)

print(f"Message sent with SID: {message.sid}")

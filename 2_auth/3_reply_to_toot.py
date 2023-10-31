'''
    Docs: https://docs.joinmastodon.org/methods/statuses/#create
'''
import requests, os
from environs import Env
from datetime import datetime, timedelta

env = Env().read_env()


# Build our URL:
server      = f'https://mastodon.ie'
url         = f'{server}/api/v1/statuses/'
message     = 'This is the original toot!'
reply       = 'This toot is a reply, to the original toot.'

# Add our status message:
form_data = {
    'status'        : message,
}

# Build our header:
header = {
    'Accept'        : 'application/json',
    'Authorization' : f'Bearer {os.environ.get("MASTOODON_ACCESS_TOKEN")}',
}

# Send request:
response = requests.post(url, data=form_data, headers=header)
print(response.json()['id'])

# Take the ID from the previous toot!
reply_id = response.json()['id']

# Send the reply:
form_data = {
    'status'            : reply,
    'in_reply_to_id'    : reply_id
}

response_reply = requests.post(url, data=form_data, headers=header)

# Print the response to screen:
print(response_reply)
print(response_reply.json())

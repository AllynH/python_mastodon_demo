'''
    Docs: https://docs.joinmastodon.org/methods/statuses/#create
'''
import requests, os
from environs import Env

env = Env().read_env()

# Build our URL:
server      = 'https://mastodon.ie'
params      = ''
url         = f'{server}/api/v1/statuses/{params}'
message     = 'Tooting with Python 🐍 🤖'

# Add our status message:
form_data = {
    'status' : message 
}

# Build our header:
header = {
    'Accept'        : 'application/json',
    'Authorization' : f'Bearer {os.environ.get("MASTOODON_ACCESS_TOKEN")}',
}

# Send request:
response = requests.post(url, data=form_data, headers=header)

# Print the response to screen:
print(response.json())

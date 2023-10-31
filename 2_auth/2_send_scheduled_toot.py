'''
    Docs: https://docs.joinmastodon.org/methods/statuses/#create
'''
import requests, os
from environs import Env
from datetime import datetime, timedelta

env = Env().read_env()

# Schedule time - needs to be >5 minutes:
now = datetime.now()
schedule = datetime.now() + timedelta(minutes=10)

# Build our URL:
server      = f'https://mastodon.ie'
url         = f'{server}/api/v1/statuses/'
message     = f'Sending a scheduled toot: 📆\n Sent at: {now.strftime("%I:%M%p")}\n Displayed at: {schedule.strftime("%I:%M%p")}'

# Add our status message:
form_data = {
    'status'        : message,
    'scheduled_at'  : schedule
}

# Build our header:
header = {
    'Accept'        : 'application/json',
    'Authorization' : f'Bearer {os.environ.get("MASTOODON_ACCESS_TOKEN")}',
}

# Send request:
response = requests.post(url, data=form_data, headers=header)
print(message)

# Print the response to screen:
print(response.json())

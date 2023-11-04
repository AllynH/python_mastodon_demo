'''
    Docs: https://docs.joinmastodon.org/methods/timelines/
'''
import requests

server      = "https://mastodon.ie"
category    = "cats"
local_only  = True
local_param = "&local=true" if local_only else ""

url         = f"{server}/api/v1/timelines/tag/{category}?limit=5{local_param}"
response = requests.get(url)

for status in response.json():
    print(f"ID: {status['id']}")
    print(f"Content: {status['content']}")
    print(f"URI: {status['uri']}")
    print(f"Display_name: {status['account']['display_name']}")
    print(f"Posted time: {status['created_at']}")
    print(f"Bot: {status['account']['bot']}")
    print("")

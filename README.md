# python_mastodon_demo
Demonstrations of interacting with Mastodon via the API, using Python.


## Setup:
Install the requirements:
```
python -m pip install -r requirements.txt
```

##  Register your app:
There are 2 separate ways to register your app:
1. Manually, via the web interface.
2. Automatically via the Mastodon API.
This repo shows examples of both.

Note, for example 1_basic - no auth is needed.

### Examples 1 & 2:
For Examples 1 & 2, you will need to register your app, on your Mastodon server web interface, and get your client ID, client secret and access token.

### Examples using Mastodon.py:
You can skip the above step and just populate your email address and password into the .env file. 

## Populate .env file:
Using the .env_EXAMPLE file, create a .env file with the required environment variables completed.


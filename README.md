# python_mastodon_demo
Demonstrations of interacting with Mastodon via the API, using Python.

## Clone the repo:
You can clone the repo as usual:
```
git clone https://github.com/AllynH/python_mastodon_demo.git
cd python_mastodon_demo
```

### Build and activate a virtual env:
Create a virtual environment and activate it as noraml, for example.
```
python -m venv venv
```
Activate on windows:
```
venv\Scripts\activate
```

Activate on Linux:
```
source venv/Scripts/activate.csh
```

### Setup:
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

### Examples 2:
For Examples 2, you will need to register your app, on your Mastodon server web interface, and get your client ID, client secret and access token.

### Example 3, using Mastodon.py:
You can skip the above step and just populate your email address and password into the .env file. Executing the code in 3_mastodon_py/1_register_app.py will create an app and output your credentials into 2 files: 
1. pycon_ie_clientcred.secret
2. pycon_ie_usercred.secret

These files contain your apps client ID, client secret and access token.
You will use pycon_ie_usercred.secret to login again, via the Mastodon.py code.

## Populate .env file:
Using the .env_EXAMPLE file, create a .env file with the required environment variables completed.

## Running the code:
To run the code, you can run from the repo dir.

To run the first example, 1_read_toots.py, you can do so as below:
```
python 1_basic/1_send_toot.py
```

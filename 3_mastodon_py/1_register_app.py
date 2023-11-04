'''
    Docs: https://mastodonpy.readthedocs.io/en/stable/#module-mastodon

    You need to fill in the following values in your .env to register your app
    MASTODON_EMAIL=email-address-you-registered-with@whomever.com
    MASTODON_PASSWORD=your-super-secret-password

    You only need to run this once - to generate the following files:
    1. pycon_ie_clientcred.secret
    2. pycon_ie_usercred.secret
'''
import os
from environs import Env
from mastodon import Mastodon

env = Env().read_env()

# Register your app! This only needs to be done once (per server, or when
# distributing rather than hosting an application, most likely per device and server).
# Uncomment the code and substitute in your information:
Mastodon.create_app(
    'pycon_ie_app',
    api_base_url = 'https://mastodon.ie',
    to_file = 'pycon_ie_clientcred.secret'
)

# Then, log in. This can be done every time your application starts (e.g. when writing a
# simple bot), or you can use the persisted information:
mastodon = Mastodon(client_id = 'pycon_ie_clientcred.secret',)
mastodon.log_in(
    os.environ.get("MASTODON_EMAIL"),
    os.environ.get("MASTODON_PASSWORD"),
    to_file = 'pycon_ie_usercred.secret'
)

# Note that this won't work when using 2FA - you'll have to use OAuth, in that case.
# To post, create an actual API instance:
mastodon = Mastodon(access_token = 'pycon_ie_usercred.secret')
mastodon.toot('Tooting from Python using #mastodonpy !')

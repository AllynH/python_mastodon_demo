from mastodon import Mastodon, StreamListener
mastodon = Mastodon(access_token = 'pycon_ie_usercred.secret')

class Listener(StreamListener):

    def on_update(self, status):
        # print(f"on_update: {status}")
        print("")
        print(f"ID: {status['id']}")
        print(f"Display_name: {status['account']['display_name']}")
        print(f"Content: {status['content']}")
        print(f"URI: {status['uri']}")
        print(f"Bot: {status['account']['bot']}")
        # on_update: {'id': 109371390226010302, 'content': '<p>Listening to Toots...</p>',
        #  'account': {'id': 109359234895957150, 'username': 'admin'}, ...}

    def on_notification(self, notification):
        print(f"on_notification: {notification}")
        print("")
        # Follow notification:
        # on_notification: {'id': 7, 'type': 'follow',
        #  'account': {'id': 109370544417433130, 'username': 'some_friend'}, ...}


# Streams events that are relevant to the authorized user, i.e. home timeline and notifications.
# mastodon.stream_user(Listener())

# Streams public events. Setting local=True streams only local events:
# mastodon.stream_public(Listener(), local=False)

# Stream for all public statuses for the hashtag ‘tag’ seen by the connected instance.
mastodon.stream_hashtag(tag='cats', listener=Listener(), local=False)

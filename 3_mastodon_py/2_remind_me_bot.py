import re
from mastodon import Mastodon
from datetime import datetime, timedelta

# Login:
mastodon = Mastodon(access_token = 'pycon_ie_usercred.secret')

# Get notifications:
notifications = mastodon.notifications(mentions_only=True)

# Loop through notifications:
for notif in notifications:

    content = notif['status']['content']
    # Get relevant notifications:
    if "!remindme" in content.lower():
        hours = 0
        minutes = 0
        if "hour" in content:
            hours = re.sub(' hour.*$', '', content)
            hours = int(re.sub('^.* ', '', hours))
        if "minutes" in content:
            minutes = re.sub(' minutes.*$', '', content)
            minutes = int(re.sub('^.* ', '', minutes))

        # Create a scheduled time:
        schedule_time = datetime.now() + timedelta(hours=hours, minutes=minutes)
        message = f"Hi there {notif['account']['url']}, here is your reminder!"
        reply_id = notif['status']['id']

        # Send the scheduled toot!
        print(f"Scheduled toot for: {hours} hours + {minutes} minutes, in reply to ID: {reply_id}")
        mastodon.status_post(status=message, scheduled_at=schedule_time, in_reply_to_id=reply_id)

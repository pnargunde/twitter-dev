import tweepy
import json
# Authenticate to Twitter
auth = tweepy.OAuthHandler("ztWu4DaLOB6begUDvLqA6zJRw", "cMtL3VtUfQN6WpBW3SxfqJF5Ay0OQT5lfsqH5GIxur14wBfqz6")
auth.set_access_token("124793231-040zKvhQO3LQQisjq77jEWYBJE1pdOh12ieyKDSX","5N7AIwyijoOrSwGV9ZBms3E7OY49qk0oIV3sKwAYacGI3")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, parser=tweepy.parsers.JSONParser())
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


new_tweets = api.search(
                       q="(@astroonline)",
                       count=20,
                       result_type="recent",
                       include_entities=True,
                       lang="en")


if not new_tweets:
    print("No more tweets found")
#for tweet in new_tweets:
#print(new_tweets)
#json_object = json.dumps(new_tweets)
for items in new_tweets["statuses"]:
    print(items["text"])

import tweepy
import datetime
import os

BEARER_TOKEN = os.environ['BEARER_TOKEN']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

tweet_client = tweepy.Client(bearer_token=BEARER_TOKEN,
                             consumer_key=CONSUMER_KEY,
                             consumer_secret=CONSUMER_SECRET,
                             access_token=ACCESS_TOKEN,
                             access_token_secret=ACCESS_TOKEN_SECRET)

def get_user_id(username):
    response = tweet_client.get_user(username=username)
    user_id = response[0].id
    return user_id


def process_tweet(tweet, username, keywords):
    text = tweet.text.lower()

    contain_keyword = True
    for word in keywords:
        if word not in text:
            contain_keyword = False
            break
    if contain_keyword:
        tweet_url = f'http://twitter.com/{username}/status/{tweet.id}'  # create url
        return tweet_url
    return


def get_tweets_from_user(username, user_id, start_time, keywords):
    data, includes, errors, meta = tweet_client.get_users_tweets(id=user_id, exclude=['retweets'],
                                                                 max_results=100, start_time=start_time)
    if data is None:
        return []
    results = []
    for tweet in data:
        tweet_url = process_tweet(tweet, username, keywords)
        if tweet_url:
            results.append(tweet_url)
    return results


def get_tweets(data, minute_delta):
    now = datetime.datetime.utcnow()
    start_time = now - datetime.timedelta(minutes=minute_delta)
    start_time = start_time.isoformat(timespec='seconds') + 'Z'

    combined_url_list = []

    username_list = [elem for elem in data if elem not in ['CHANNEL_ID', 'MINUTE_INTERVAL']]
    for username in username_list:
        user_id, keywords = data[username]
        url_list = get_tweets_from_user(username, user_id, start_time, keywords)
        combined_url_list = combined_url_list + url_list

    return combined_url_list

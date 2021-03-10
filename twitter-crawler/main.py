import os
import tweepy

twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

twitter_consumer_key = os.environ['TWITTER_CONSUMER_KEY']
twitter_consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']


class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        print('ERROR', status_code)
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

    def on_status(self, status):
        if status.retweeted or not hasattr(status, 'extended_tweet'):
            return None
        print('ID: ', status.id_str)
        print('FULL_TEXT:', status.extended_tweet['full_text'])
        print('HASHTAGS: ', status.entities['hashtags'])
        print('USER_ID:', status.user.id_str)
        print('USER_NAME:', status.user.name)
        print('RETWEET_COUNT: ', status.retweet_count)
        print('REPLY_COUNT: ', status.reply_count)
        print('CREATED AT: ', status.created_at)
        print('======================================')
        


print("CREATE CONNECTION")
twitter_auth = tweepy.OAuthHandler(
    twitter_consumer_key, twitter_consumer_secret)
twitter_auth.set_access_token(
    twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(twitter_auth)

print("CREATE STREAM")
# create stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(
    auth=twitter_api.auth, listener=myStreamListener, tweet_mode='extended')
print("START STREAM")
myStream.filter(
    track=['a'],
    languages=['en'])
print('FILTER HAS BEEN EXECUTED, WAITING FOR STREAM')
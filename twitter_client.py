import os
import base64
import requests
import logging
import json

URL_BASE = os.environ['URL_BASE']
TOKEN_URL = os.environ['TOKEN_URL']
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']
TWITTER_BEARER_TOKEN = os.environ['TWITTER_BEARER_TOKEN']
URL = os.environ['URL']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


def _is_error_response(response):
    if response.status_code != 200:
        logging.error(f'Status Code: {response.status_code} JSON Response: {response.json()}')
        return True
    return False


def extract_urls_from_tweets(max_results, fromDate, toDate):
    tweets = []
    data_str = json.dumps({
            'query': 'from:roselmamendes has:links',
            'maxResults': str(max_results),
            'fromDate': f'{fromDate}0000',  # <yyyymmddhhmm>
            'toDate': f'{toDate}0000'
        })
    response = requests.post(
        URL_BASE + URL,
        headers={"Authorization": f'Bearer {TWITTER_BEARER_TOKEN}'},
        data=data_str
    )

    if not _is_error_response(response):
        tweets_results = response.json()['results']
        for tweet in tweets_results:
            urls = _extract_urls_from(tweet['entities']['urls'])
            retweeted = tweet.get('retweeted_status', None)
            retweeted_text = None
            if retweeted:
                retweeted_text = retweeted['text']
            tweets.append(
                {
                    'created_at': tweet['created_at'],
                    'urls': urls,
                    'name': tweet['user']['name'],
                    'retweeted_status': retweeted_text
                }
            )
    return tweets


def _extract_urls_from(raw_tweet_urls):
    return [url_object['expanded_url'] for url_object in raw_tweet_urls]


def get_bearer_token():
    token = None
    simple_encode = f'{TWITTER_API_KEY}:{TWITTER_API_SECRET}'.encode('utf-8')
    encoded_key_secret = str(base64.b64encode(simple_encode), 'utf-8')
    url = URL_BASE + TOKEN_URL

    print(f'url: {url}')
    print(f'key and secret base64 encoded: {encoded_key_secret}')

    response = requests.post(
        url,
        headers={
            'Authorization': f'Basic {encoded_key_secret}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        data='grant_type=client_credentials'
    )

    if not _is_error_response(response):
        token = response.json()['access_token']
    return token

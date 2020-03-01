import os
import base64
from json import JSONDecodeError

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


def get_tweets_at(max_results, fromDate, toDate):
    tweets = []
    data_str = _build_payload(fromDate, max_results, toDate)

    response = requests.post(
        URL_BASE + URL,
        headers={"Authorization": f'Bearer {TWITTER_BEARER_TOKEN}'},
        data=data_str
    )

    if not _is_error_response(response):
        tweets = response.json()
    return tweets


def _build_payload(fromDate, max_results, toDate):
    return json.dumps({
        'query': 'from:roselmamendes has:links',
        'maxResults': str(max_results),
        'fromDate': f'{fromDate}0000',  # <yyyymmddhhmm>
        'toDate': f'{toDate}0000'
    })


def get_bearer_token():
    token = None
    simple_encode = f'{TWITTER_API_KEY}:{TWITTER_API_SECRET}'.encode('utf-8')
    encoded_key_secret = str(base64.b64encode(simple_encode), 'utf-8')
    url = URL_BASE + TOKEN_URL

    logger.info(f'url: {url}')
    logger.info(f'key and secret base64 encoded: {encoded_key_secret}')

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


def get_tweet(tweet_id):
    response = requests.get(
        f'{URL_BASE}1.1/statuses/show.json?id={tweet_id}',
        headers={"Authorization": f'Bearer {TWITTER_BEARER_TOKEN}'}
    )

    if not _is_error_response(response):
        return response.json()


def _is_error_response(response):
    response_json = None
    if response.status_code != 200:
        try:
            response_json = response.json()
            logging.error(f'Status Code: {response.status_code} JSON Response: {response.json()}')
        except JSONDecodeError as e:
            logging.error(f'Status Code: {response.status_code}')

        return True
    return False

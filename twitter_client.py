import os
import base64
import requests

URL_BASE = os.environ['URL_BASE']
TOKEN_URL = os.environ['TOKEN_URL']
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']


def get_bearer_token():
    token = None
    simple_encode = f'{TWITTER_API_KEY}:{TWITTER_API_SECRET}'.encode('utf-8')
    encoded_key_secret = base64.b64encode(simple_encode)

    print(f'Bearer token: {encoded_key_secret}')

    response = requests.post(
        URL_BASE + TOKEN_URL,
        headers={'Authorization': f'Basic {encoded_key_secret}'}
    )

    if response.status_code != 200:
        print(response.json())
    else:
        token = response.json()['access_token']

    return token
import os
import requests

URL_BASE = os.environ['URL_BASE']
URL = os.environ['URL']
TWITTER_BEARER_TOKEN = os.environ['TWITTER_BEARER_TOKEN']


bearer_token = TWITTER_BEARER_TOKEN

response = requests.post(
    URL_BASE + URL,
    headers={"Authorization": f'Bearer {bearer_token}'},
    data={
        'query': '',
        'max_results': '100',
        'fromDate': '20200101',
        'toDate': '20200131'
    }
)

print(response)
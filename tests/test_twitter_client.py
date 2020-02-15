import unittest
import requests_mock
from twitter_client import extract_urls_from_tweets


class TestTwitterClient(unittest.TestCase):
    @requests_mock.mock()
    def test_should_search_for_tweets(self, m):
        m.post(
            'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json',
            json={
                'results': [
                    {
                        "created_at": "Wed Oct 10 20:19:24 +0000 2018",
                        "entities": {
                            "urls": [{"expanded_url": "https://some-url"}]
                        },
                        "user": {"name": "Someone name"}
                    },
                    {
                        "created_at": "Wed Oct 11 20:19:24 +0000 2018",
                        "entities": {
                            "urls": [{"expanded_url": "https://some-url2"}]
                        },
                        "user": {"name": "Someone name"},
                        "retweeted_status": {"text": "some retweet"}
                    }
                ]
            }
        )
        urls = extract_urls_from_tweets(2, '20200101', '20200131')

        self.assertEqual(
            [
                {
                    "created_at": "Wed Oct 10 20:19:24 +0000 2018",
                    "urls": ["https://some-url"],
                    "name": "Someone name",
                    "retweeted_status": None
                },
                {
                    "created_at": "Wed Oct 11 20:19:24 +0000 2018",
                    "urls": ["https://some-url2"],
                    "name": "Someone name",
                    "retweeted_status": "some retweet"
                }
            ],
            urls
        )

    @requests_mock.mock()
    def test_should_treat_errors_from_twitter_api(self, m):
        m.post(
            'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json',
            status_code=500,
            json={'error':
                      {'message': 'There were errors processing your request: Invalid json, could not parse.',
                       'sent': '2020-02-15T20:53:54+00:00',
                       'transactionId': '00dad8870086daf3'
                       }
                  }
        )

        urls = extract_urls_from_tweets(10, '', '')

        self.assertEqual([], urls)

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
                            "urls": [{"url": "https://some-url"}]
                        }
                    },
                    {
                        "created_at": "Wed Oct 11 20:19:24 +0000 2018",
                        "entities": {
                            "urls": [{"url": "https://some-url2"}]
                        }
                    }
                ]
            }
        )
        tweets = extract_urls_from_tweets(2, '20200101', '20200131')

        self.assertEqual(
            [
                {
                    "created_at": "Wed Oct 10 20:19:24 +0000 2018",
                    "urls": ["https://some-url"]
                },
                {
                    "created_at": "Wed Oct 11 20:19:24 +0000 2018",
                    "urls": ["https://some-url2"]
                }
            ],
            tweets
        )


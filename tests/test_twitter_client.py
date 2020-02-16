import unittest
import requests_mock
from tests import json_for_tests
from twitter_client import extract_urls_from_tweets


class TestTwitterClient(unittest.TestCase):
    @requests_mock.mock()
    def test_should_search_for_tweets(self, m):
        m.post(
            'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json',
            json=json_for_tests.with_regular_tweets
        )
        urls = extract_urls_from_tweets(2, '20200101', '20200131')

        self.assertEqual(
            json_for_tests.with_regular_tweets_assert,
            urls
        )

    @requests_mock.mock()
    def test_should_treat_errors_from_twitter_api(self, m):
        m.post(
            'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json',
            status_code=500,
            json=json_for_tests.with_error
        )

        urls = extract_urls_from_tweets(10, '', '')

        self.assertEqual([], urls)

    @requests_mock.mock()
    def test_if_is_retweet_extract_link_from_original_tweet(self, m):
        m.post(
            'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json',
            json=json_for_tests.with_retweet
        )

        urls = extract_urls_from_tweets(10, '20181011', '20181011')

        self.assertEqual(
           json_for_tests.with_retweet_assert,
            urls
        )

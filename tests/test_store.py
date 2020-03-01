import unittest
import os
from store.store import Store
from tests import json_for_tests
from pathlib import Path


class TestStore(unittest.TestCase):
    def tearDown(self):
        _remove_test_database()

    def test_should_save_tweets_with_urls_in_a_file(self):
        store = Store('test_file')

        store.save(json_for_tests.with_model_url)

        saved_tweet = store.list()[0]

        self.assertEqual('1235', saved_tweet.tweet_id)
        self.assertEqual('Wed Oct 10 20:19:24 +0000 2018', saved_tweet.created_at)
        self.assertEqual('https://some-url', saved_tweet.url)


def _remove_test_database():
    actual_folder_path = os.getcwd()
    directory_path = Path(actual_folder_path)
    for each_file_path in directory_path.glob('test*.db'):
        print(f'removing {each_file_path}')
        each_file_path.unlink()


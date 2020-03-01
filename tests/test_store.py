import unittest
import os
from store.store import Store
from tests import json_for_tests


class TestStore(unittest.TestCase):
    def test_should_create_file_if_it_doesnt_exist(self):
        Store('test_create_file.json')

        open('test_create_file.json')

        os.remove('test_create_file.json')

    def test_should_save_tweets_with_urls_in_a_file(self):
        store = Store('test_file.json')

        store.save(json_for_tests.with_regular_tweets)

        saved_tweets = store.list()

        self.assertEqual(json_for_tests.with_regular_tweets, saved_tweets)


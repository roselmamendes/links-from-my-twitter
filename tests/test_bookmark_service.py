import unittest
import requests_mock
from app.bookmark_service import generate_bookmark_from_twitter
from app.model.bookmark import Bookmark
from tests import json_for_tests


class TestBookmarkService(unittest.TestCase):
    @requests_mock.mock()
    def test_should_generate_bookmark_from_twitter(self, m):
        m.post(
            'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json',
            json=json_for_tests.with_regular_tweets
        )
        expected_bookmark = Bookmark(
            source_id='1235',
            source='twitter',
            created_at='Wed Oct 10 20:19:24 +0000 2018',
            urls=['https://some-url'],
            source_fields={'retweeted_status': None}
        )

        actual_bookmark = generate_bookmark_from_twitter(1, '20181010', '20181010')

        self.assertEqual(expected_bookmark.urls, actual_bookmark[0].urls)
        self.assertEqual(expected_bookmark.source, actual_bookmark[0].source)
        self.assertEqual(expected_bookmark.source_id, actual_bookmark[0].source_id)
        self.assertEqual(expected_bookmark.created_at, actual_bookmark[0].created_at)
        self.assertEqual(expected_bookmark.source_fields, actual_bookmark[0].source_fields)


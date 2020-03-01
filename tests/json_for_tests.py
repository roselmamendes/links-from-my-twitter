from app.model.bookmark import Bookmark

with_retweet = {
    'results': [
        {
            "id_str": "1234",
            "created_at": "Wed Oct 11 20:19:24 +0000 2018",
            "entities": {
                "urls": [{"expanded_url": ""}]
            },
            "user": {"name": "Someone name"},
            "retweeted_status": {
                "text": "some retweet",
                "entities": {"urls": [{"expanded_url": "https://fromretweet"}]}
            }
        }
    ]
}

with_retweet_bookmark_assert = [{
    "id_str": "1234",
    "created_at": "Wed Oct 11 20:19:24 +0000 2018",
    "urls": ["https://fromretweet", ""],
    "name": "Someone name",
    "retweeted_status": "some retweet"
}]

with_error = {'error':
                  {'message': 'There were errors processing your request: Invalid json, could not parse.',
                   'sent': '2020-02-15T20:53:54+00:00',
                   'transactionId': '00dad8870086daf3'
                   }
              }

with_regular_tweets = {
    'results': [
        {
            "id_str": "1235",
            "created_at": "Wed Oct 10 20:19:24 +0000 2018",
            "entities": {
                "urls": [{"expanded_url": "https://some-url"}]
            },
            "user": {"name": "Someone name"}
        },
        {
            "id_str": "1236",
            "created_at": "Wed Oct 11 20:19:24 +0000 2018",
            "entities": {
                "urls": [{"expanded_url": "https://some-url2"}]
            },
            "user": {"name": "Someone name"}
        }
    ]
}

with_regular_bookmark_assert = [
    {
        "id_str": "1235",
        "created_at": "Wed Oct 10 20:19:24 +0000 2018",
        "urls": ["https://some-url"],
        "name": "Someone name",
        "retweeted_status": None
    },
    {
        "id_str": "1236",
        "created_at": "Wed Oct 11 20:19:24 +0000 2018",
        "urls": ["https://some-url2"],
        "name": "Someone name",
        "retweeted_status": None
    }
]

with_bookmark = Bookmark(
    source_id='1235',
    source='twitter',
    created_at='Wed Oct 10 20:19:24 +0000 2018',
    urls=['https://some-url'],
    source_fields={'retweeted_status': None}
)

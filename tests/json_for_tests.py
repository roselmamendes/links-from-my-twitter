with_retweet = {
    'results': [
        {
            "created_at": "Wed Oct 11 20:19:24 +0000 2018",
            "entities": {
                "urls": []
            },
            "user": {"name": "Someone name"},
            "retweeted_status": {
                "text": "some retweet",
                "entities": {"urls": [{"expanded_url": "https://fromretweet"}]}
            }
        }
    ]
}

with_retweet_assert = [{
    "created_at": "Wed Oct 11 20:19:24 +0000 2018",
    "urls": ["https://fromretweet"],
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
            "user": {"name": "Someone name"}
        }
    ]
}

with_regular_tweets_assert = [
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
        "retweeted_status": None
    }
]

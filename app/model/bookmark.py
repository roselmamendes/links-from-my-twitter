class Bookmark:
    def __init__(self, source_id, source, created_at, urls, source_fields=None):
        self.source_fields = source_fields
        self.urls = urls
        self.created_at = created_at
        self.source_id = source_id
        self.source = source

    @staticmethod
    def build_urls_list(tweets_results):
        bookmarks = []

        for tweet in tweets_results['results']:
            expanded_urls = Bookmark._extract_urls_from(tweet['entities']['urls'], tweet.get('retweeted_status', None))
            retweeted_text = Bookmark._extract_retweeted_text(tweet.get('retweeted_status', None))
            bookmarks.append(
                Bookmark(
                    source='twitter',
                    source_id=tweet['id_str'],
                    created_at=tweet['created_at'],
                    urls=expanded_urls,
                    source_fields={'retweeted_status': retweeted_text}
                )
            )

        return bookmarks

    @staticmethod
    def _extract_urls_from(raw_tweet_urls, retweeted_status):
        urls = []
        if retweeted_status:
            urls += ([url_object['expanded_url'] for url_object in retweeted_status['entities']['urls']])

        urls += ([url_object['expanded_url'] for url_object in raw_tweet_urls])

        return urls

    @staticmethod
    def _extract_retweeted_text(retweeted_status):
        retweeted_text = None
        if retweeted_status:
            retweeted_text = retweeted_status['text']

        return retweeted_text

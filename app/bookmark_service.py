from app.model.bookmark import Bookmark
from app.twitter.client import get_tweets_at


def generate_bookmark_from_twitter(max_results, fromDate, toDate):
    tweets = get_tweets_at(max_results, fromDate, toDate)

    bookmarks = Bookmark.build_urls_list(tweets)

    return bookmarks
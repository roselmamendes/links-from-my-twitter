from app.bookmark_service import generate_bookmark_from_twitter

# 30, '20200210', '20200215'
def print_bookmark_from_twitter(max_results, fromDate, toDate):
    bookmark_from_twitter = generate_bookmark_from_twitter(max_results, fromDate, toDate)

    print(bookmark_from_twitter)


def create_html_bookmark_from_twitter(max_results, fromDate, toDate):
    bookmark_from_twitter = generate_bookmark_from_twitter(max_results, fromDate, toDate)

    _generate_html_with(bookmark_from_twitter)


def _generate_html_with(bookmark_from_twitter):
    pass

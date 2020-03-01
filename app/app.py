from app.bookmark_service import generate_bookmark_from_twitter
from app.view.bookmark import generate_html_with

# 30, '20200210', '20200215'
def print_bookmark_from_twitter(max_results, fromDate, toDate):
    bookmark_from_twitter = generate_bookmark_from_twitter(max_results, fromDate, toDate)

    for bookmark in bookmark_from_twitter:
        print(bookmark.source_fields)
        print(bookmark.urls)


def create_html_bookmark_from_twitter(max_results, fromDate, toDate):
    bookmark_from_twitter = generate_bookmark_from_twitter(max_results, fromDate, toDate)

    generate_html_with(f'{fromDate}_{toDate}', bookmark_from_twitter)


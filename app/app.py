from app.bookmark_service import generate_bookmark_from_twitter
from jinja2 import Environment, FileSystemLoader

# 30, '20200210', '20200215'
def print_bookmark_from_twitter(max_results, fromDate, toDate):
    bookmark_from_twitter = generate_bookmark_from_twitter(max_results, fromDate, toDate)

    for bookmark in bookmark_from_twitter:
        print(bookmark.source_fields)
        print(bookmark.urls)


def create_html_bookmark_from_twitter(max_results, fromDate, toDate):
    bookmark_from_twitter = generate_bookmark_from_twitter(max_results, fromDate, toDate)

    _generate_html_with(f'{fromDate}_{toDate}', bookmark_from_twitter)


def _generate_html_with(date_range, bookmark_from_twitter):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(f'twitter_bookmark.html')
    output_from_parsed_template = template.render(
        date_range=date_range,
        bookmarks=bookmark_from_twitter
    )
    print(output_from_parsed_template)

    # to save the results
    with open(f'{date_range}_bookmarks.html', "w") as html_file:
        html_file.write(output_from_parsed_template)

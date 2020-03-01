from app.bookmark_service import generate_bookmark_from_twitter
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import requests

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


def extract_metatags_from(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    metas = soup.find_all('meta')
    print("metas: " + str(metas))
    url_image = None
    url_title = None
    for meta in metas:
        if 'property' in meta.attrs:
            if meta.attrs['property'] == 'og:image':
                url_image = meta.attrs['content']

            if meta.attrs['property'] == 'og:title':
                url_title = meta.attrs['content']

    print(f'Titulo: {url_title}')
    print(f'Imagem: {url_image}')

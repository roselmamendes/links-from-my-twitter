from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import requests


def generate_html_with(date_range, bookmark_from_twitter):
    output_from_parsed_template = _get_parsed_template(bookmark_from_twitter, date_range)

    with open(f'{date_range}_bookmarks.html', "w") as html_file:
        html_file.write(output_from_parsed_template)


def _get_parsed_template(bookmark_from_twitter, date_range):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('twitter_bookmark.html')
    output_from_parsed_template = template.render(
        date_range=date_range,
        bookmarks=bookmark_from_twitter
    )
    return output_from_parsed_template


def extract_metatags_from(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    metas = soup.find_all('meta')
    print("metas: " + str(metas))
    url_image = None
    url_title = None
    for meta in metas:
        if 'property' in meta.attrs:
            url_image, url_title = _extract_image_and_title(meta, url_image, url_title)

    print(f'Titulo: {url_title}')
    print(f'Imagem: {url_image}')


def _extract_image_and_title(meta, url_image, url_title):
    if meta.attrs['property'] == 'og:image':
        url_image = meta.attrs['content']
    if meta.attrs['property'] == 'og:title':
        url_title = meta.attrs['content']
    return url_image, url_title
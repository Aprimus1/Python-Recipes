import requests
from bs4 import BeautifulSoup


def zip_file_links_generator(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for link in soup.find_all('a', href=True):
        if link['href'].endswith(('.zip', '.ZIP')):
            yield link['href']

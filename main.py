import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
params = {
    'q': 'Python Developer',
    'l': 'New York State',
    'vjk': '71acc67a281f6838'
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.66 (KHTML, like Gecko)'
                         'Chrome/95.0.4638.54 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)
# print(res.status_code)  # status kode 200 berhasil, status kode 403 tidak berhasil


def get_total_pages():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        'vjk': '71acc67a281f6838'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    # Scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul', 'pagination-list')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

        total = int(max(total_pages))
        return total


def get_all_items():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        'vjk': '71acc67a281f6838'
    }

    res = requests.get(url, params=params, headers=headers)

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    soup = BeautifulSoup(res.text, 'html.parser')

    # scraping proses


if __name__ == '__main__':
    get_total_pages()

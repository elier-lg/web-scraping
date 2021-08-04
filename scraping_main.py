from os import readlink
from utils import consts, funcs
import csv
import requests
from bs4 import BeautifulSoup


def scrap(url, links):
    len_links = len(links)
    print(consts.SCRAP_LEN_MESSAGE.format(len=len_links, url=url))
    file_name = url.replace(consts.URL_PREFIX, '').replace('.com', '').replace('/', '_')
    f = open(f'{consts.OUTPUT_PATH}{file_name}.csv', 'w')
    writer = csv.writer(f)
    for link in links:
        writer.writerow([link.text])
    f.close()


def get_site_content(url):
    response = requests.get(url)
    print(consts.START_SCRAP_MESSAGE.format(url=url))
    if response.status_code == requests.codes.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select('.details__header--title,bold > a')
        len_links = len(links)
        if len_links:
            scrap(url, links)
        else:
            links = soup.select('.product-title-desktop,ui > a')
            len_links = len(links)
            if len_links:
                scrap(url, links)
            else:
                print(f'Not possible to scrap on {url}')
        


def get_json_object():
    jsObj = {}
    line_count = 0
    nf = open(consts.URLS_PATH, "r")
    csv_reader = csv.reader(nf, delimiter=',')
    for row in csv_reader:
        get_site_content(row[0])
        line_count += 1
    return jsObj


if __name__ == "__main__":
    funcs.ensure_folder(consts.OUTPUT_PATH)
    get_json_object()

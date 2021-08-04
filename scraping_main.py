from utils import consts
import csv
import requests

def get_site_content(url):
  response = requests.get(url)
  print(response.text)

def get_json_object():
    jsObj = {}
    line_count = 0
    nf = open(consts.URLS_PATH, "r")
    csv_reader = csv.reader(nf, delimiter=',')
    for row in csv_reader:
        print(row[0])
        get_site_content(row[0])
        line_count += 1
    return jsObj

if __name__ == "__main__":
    get_json_object()


import re
import requests
import urllib.request
import urllib.error

BASE_URL=f"https://www.instagram.com/"
USER=""
LOCAL_DIR = '/etc/'

res = requests.get(BASE_URL + USER + '/')
if res.status_code >= 300:
    raise

def download_file(url, local_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(local_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            pass
        else:
            print(e)
            raise
    except BaseException as e:
        print(e)
        raise

for article_num in range(START_ARTICLE_NUM, END_ARTICLE_NUM + 1):
    article_str = str(article_num).zfill(4)
    for article_suffix in ['', '_2', '_3']:
        url = BASE_URL + f"{article_str}{article_suffix}.jpg"
        local_path = LOCAL_DIR + f"{article_str}{article_suffix}.jpg"
        download_file(url, local_path)

import json
from numpy import full
import requests
import time
import os

def strip_html(text):
    import re
    a = text.replace('&gt;', '>')
    b = a.replace('&quot;', '\"')
    c = b.replace('&#039;','\'')
    d = c.replace('<br>', '\n')
    clean = re.compile('<.*?>')
    fully_cleaned = re.sub(clean, '', d)
    return fully_cleaned

def get_posts():
    while True:
        try:
            r = requests.get('https://a.4cdn.org/pol/catalog.json')
            r = r.json()
            os.system('cls||clear')
            country = r[0]['threads'][2]['last_replies'][0]['country_name']
            text = r[0]['threads'][2]['last_replies'][0]['com']
            formatted_reply =strip_html(text.replace('<br>', '\n') + '\n')
            print(formatted_reply)
            f = open('replies.txt', 'a')
            f.write(formatted_reply)
            f.close()
            time.sleep(5)
        except KeyError:
            time.sleep(5)

get_posts()
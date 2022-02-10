import json
from numpy import full
import requests
import time
import os



def replace_html_characters(text):
    a = text.replace('&gt;', '>')
    b = a.replace('&quot;', '\"')
    c = b.replace('&#039;','\'')
    d = c.replace('<br>', '\n')
    return d.replace('<br>', '\n')


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    fully_cleaned = re.sub(clean, '', text)
    return replace_html_characters(fully_cleaned)



while True:
    try:
        r = requests.get('https://a.4cdn.org/pol/catalog.json')
        r = r.json()
        os.system('cls||clear')
        country = r[0]['threads'][2]['last_replies'][0]['country_name']
        text = r[0]['threads'][2]['last_replies'][0]['com']
        print(country + '\n\n' + remove_html_tags(text.replace('<br>', '\n')))
        time.sleep(5)
    except KeyError as keyerror:
        print('No comment')
        time.sleep(5)


# write request to json
with open('sample.json', 'w') as f:
    for items in r:
        for thread in items['threads']:
            j = json.dumps(thread, indent = 4)
            f.write(j)


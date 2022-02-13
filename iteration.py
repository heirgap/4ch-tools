import json
from numpy import full
import requests
import time
import os

r = requests.get('https://a.4cdn.org/pol/catalog.json')
r = r.json()
os.system('cls||clear')

def strip_html(text):
    import re
    a = text.replace('&gt;', '>')
    b = a.replace('&quot;', '\"')
    c = b.replace('&#039;','\'')
    d = c.replace('<br>', '\n')
    clean = re.compile('<.*?>')
    fully_cleaned = re.sub(clean, '', d)
    return fully_cleaned   


for threads in r:
    for posts in threads:
        print(posts[1])
        
    






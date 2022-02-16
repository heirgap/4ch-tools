from concurrent.futures import thread
from matplotlib.pyplot import get
from numpy import full
import requests
import os
import sys
import re
from os import path
from wordcloud import WordCloud

def cloud_generator():
    stopwords = ["youtube", "https", "you", "the", "and", 
                "youtu", "com", "this", "of", "is", "on", 
                "in", "a", "to", "I", "all", "for", "do", 
                "it", "twitter", "www", "what", "but", "http",
                "with", "thread", "threads", "be", "are", "or",
                "well", "so", "that", "from," "watch", "not", 
                "watch v", "they", "as", "their", "embed", "your",
                "at", "org", "pastebin", "can", "go", "topic", "board",
                "if", "how", "into", "from", "will", "people", "rumble"]

    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    try:
        text = open(path.join(d, 'replies.txt'), encoding = 'cp1252').read()
    except UnicodeDecodeError:
        text = open(path.join(d, 'replies.txt'), encoding = 'utf-8').read()
    wordcloud = WordCloud(stopwords = stopwords, scale = 5, max_font_size = 72, max_words = 2000, background_color = (16, 16, 16), mode = 'RGBA', relative_scaling = .5).generate(text)
    image = wordcloud.to_image()
    image.show()

def strip_html(text):
    a = text.replace('&gt;', '>')
    b = a.replace('&quot;', '\"')
    c = b.replace('&#039;','\'')
    d = c.replace('<br>', '\n')
    clean = re.compile('<.*?>')
    fully_cleaned = re.sub(clean, '', d)
    return fully_cleaned   
    
def get_OPs(board):
    r = requests.get('https://a.4cdn.org/{}/catalog.json'.format(board))
    r = r.json()
    try:
        f = open('replies.txt', 'w', encoding='utf-8')
    except UnicodeDecodeError:
        f = open('replies.txt', 'w', encoding='cp1252')
    for thread in r[0]['threads']:
        try: 
            os.system('cls||clear')
            f.write(strip_html(thread['com']))
        except KeyError:
            print('')
    f.close()

def get_word_cloud(board, thread_no):
    
    r = requests.get('https://a.4cdn.org/{}/thread/{}.json'.format(board, thread_no))
    r = r.json()
    try:
        f = open('replies.txt', 'w', encoding='utf-8')
    except UnicodeDecodeError:
        f = open('replies.txt', 'w', encoding='cp1252')
    for post in r['posts']:
        try: 
            #os.system('cls||clear')
            f.write(strip_html(post['com']))
        except KeyError:
            print('')
    f.close()
    cloud_generator()

def get_images(board, thread_no):
    r = requests.get('https://a.4cdn.org/{}/thread/{}.json'.format(board, thread_no))
    r = r.json()
    domain = 'https://i.4cdn.org/{}/'.format(board)
    i = 1
    thread_name = strip_html(r['posts'][0]['semantic_url'])
    try:
        #path = os.path.join('/Pictures/4ch/', str(thread_name))
        user_relative_picture_folder = os.path.expanduser('~/Pictures/4ch/')
        path = user_relative_picture_folder + str(thread_name)
        os.makedirs(path)
        print('Created folder {}'.format(thread_name))
    except:
        print('Did not create folder.')
    for post in r['posts']:
        try:
            img = str(post['tim']) + str(post['ext'])
            try:
                file_name = post['filename']
            except:
                file_name = img
            url = domain + img
            response = requests.get(url)
            
            save_path = path + '/' + file_name + str(post['ext'])
            with open(save_path, 'wb') as f:
                f.write(response.content)
            #os.system('cls||clear')
            print('Downloading {}'.format(i))
            i += 1
        except KeyError:
            pass

def main():
    url = sys.argv[2]
    url = url.split('/')
    if sys.argv[1] == '-i':
        get_images(url[3], url[5])
    if sys.argv[1] == '-wc':
        get_word_cloud(url[3], url[5])

main()

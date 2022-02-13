import os
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'replies.txt')).read().replace('will', '')
wordcloud = WordCloud(scale = 10, max_font_size=72, max_words=2000, background_color='black', mode = 'RGB', relative_scaling=.5).generate(text.replace('people', ''))
image = wordcloud.to_image()
image.show()
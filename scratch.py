from cgi import test

def remove_html_tags(text):
    import re
    a = text.replace('&gt;', '>')
    b = a.replace('&quot;', '\"')
    c = b.replace('&#039;','\'')
    d = c.replace('<br>', '\n')
    clean = re.compile('<.*?>')
    fully_cleaned = re.sub(clean, '', d)
    return fully_cleaned


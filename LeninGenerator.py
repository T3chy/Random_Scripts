from bs4 import BeautifulSoup
import requests
import re
response = requests.get('https://www.marxists.org/archive/lenin/quotes.htm')
soup = BeautifulSoup(response.text, 'html.parser')
quotes = []
pos = 0
for i in soup.findAll('p'):
    p = soup.findAll('p')[pos].next_siblings
    if pos == 0 or pos == 1 or pos == 2:
        pos = pos + 1
        continue
    if soup.findAll('p')[pos].get_text() == []:
        continue
    print(p)
    print(type(p))
    re.search('<p>([\s\S]*?)<br\/>',p).group(0)
    print(str(re.search('<p>([\s\S]*?)<br\/>',p).group(0))[0])
    quotes.append(re.search('<p>([\s\S]*?)<br\/>',p).group(0))
    pos = pos + 1
print(quotes[20])

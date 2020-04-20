from bs4 import BeautifulSoup
import requests
import re
import string as str
def scrapequotes():
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
        quotes.append(i.get_text())
        pos = pos + 1
    pos = 0
    with open('lenin.txt','w') as de:
        for i in quotes:
            for j in i.splitlines():
                if "Lenin" in j:
                    break
                de.write(j + "\n")

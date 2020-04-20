## give a breifing on the top news from today, weighting twoards more polarized
from bs4 import BeautifulSoup
import requests
import re
from textblob import TextBlob
# def getheadlines():
#     allheadlines = []
#     print('Fetching Business Insider...')
#     request = requests.get('https://www.reuters.com/finance')
#     soup = BeautifulSoup(request.text, 'html.parser')
#     headlines = soup.findAll('h3',"story-title")
#     titles = []
#     titles.append('reuters')
#     for i in headlines:
#         titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
#     allheadlines.append(titles)
#     request = requests.get('https://www.businessinsider.com/')
#     soup = BeautifulSoup(request.text, 'html.parser')
#     headlines = soup.findAll('a',"tout-title-link")
#     titles = []
#     titles.append('businessinsider')
#     for i in headlines:
#         titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
#     allheadlines.append(titles)
#     print('Fetching NY Times...')
#     request = requests.get('https://www.nytimes.com/section/business')
#     soup = BeautifulSoup(request.text, 'html.parser')
#     headlines = soup.findAll('h2',"css-y3otqb e134j7ei0")
#     titles = []
#     titles.append('NyTimes')
#     for i in headlines:
#         titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
#     allheadlines.append(titles)
#     print('Fetching The Washington Post...')
#     request = requests.get('https://www.washingtonpost.com/business/?itid=nb_hp_business')
#     soup = BeautifulSoup(request.text, 'html.parser')
#     headlines = soup.findAll('div',{'class':"flex-stack normal-air col-lg-8 col-md-8 col-sm-8 col-xs-8 flex-stack-text"})
#     titles = []
#     titles.append('WaPo')
#     for i in headlines:
#         titles.append(i.get_text().strip(re.search('By.*',i.get_text()).group(0)).strip('\n').strip('\t').strip(' '))
#     allheadlines.append(titles)
#     print('Fetching The Guardian...')
#     request = requests.get('https://www.theguardian.com/us/business')
#     soup = BeautifulSoup(request.text, 'html.parser')
#     headlines = soup.findAll('a',"u-faux-block-link__overlay js-headline-text")
#     titles = []
#     titles.append('TheGuardian')
#     for i in headlines:
#         titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
#     allheadlines.append(titles)
#     return(allheadlines)
def getheadlines():
    allheadlines = []
    print('Fetching Business Insider...')
    request = requests.get('https://www.reuters.com/finance')
    soup = BeautifulSoup(request.text, 'html.parser')
    headlines = soup.findAll('h3',"story-title")
    titles = []
    titles.append('reuters')
    for i in headlines:
        titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
    allheadlines.append(titles)
    request = requests.get('https://www.businessinsider.com/')
    soup = BeautifulSoup(request.text, 'html.parser')
    headlines = soup.findAll('a',"tout-title-link")
    for i in headlines:
        titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
    allheadlines.append(titles)
    print('Fetching NY Times...')
    request = requests.get('https://www.nytimes.com/section/business')
    soup = BeautifulSoup(request.text, 'html.parser')
    headlines = soup.findAll('h2',"css-y3otqb e134j7ei0")
    for i in headlines:
        titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
    allheadlines.append(titles)
    print('Fetching The Washington Post...')
    request = requests.get('https://www.washingtonpost.com/business/?itid=nb_hp_business')
    soup = BeautifulSoup(request.text, 'html.parser')
    headlines = soup.findAll('div',{'class':"flex-stack normal-air col-lg-8 col-md-8 col-sm-8 col-xs-8 flex-stack-text"})
    for i in headlines:
        titles.append(i.get_text().strip(re.search('By.*',i.get_text()).group(0)).strip('\n').strip('\t').strip(' '))
    allheadlines.append(titles)
    print('Fetching The Guardian...')
    request = requests.get('https://www.theguardian.com/us/business')
    soup = BeautifulSoup(request.text, 'html.parser')
    for i in headlines:
        titles.append(i.get_text().strip(re.search('By.*',i.get_text()).group(0)).strip('\n').strip('\t').strip(' '))
    allheadlines.append(titles)
    return(titles)
news = getheadlines()
wordlist = []
nouns = ['NN','NNS','NNP','NNPS']
prev = [0,0]
print(len(news))
for headline in news:
    for word in headline.split():
        word = word.lower()
        wordlist.append(word)
for word in wordlist:
    word = TextBlob(word)
    if word.tags == []:
        continue
    if word.tags[0][1] in nouns:
        if wordlist.count(word) > prev[1]:
            prev = [word.tags[0][1],wordlist.count(word)]
print(prev)
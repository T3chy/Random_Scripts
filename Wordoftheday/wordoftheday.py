## give a breifing on the top news from today, weighting twoards more polarized
from bs4 import BeautifulSoup
import requests
import re
from textblob import TextBlob
from tkinter import *
def main(top):
    def hidethisstuff():
        pass
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
        request = requests.get('https://www.reuters.com/')
        soup = BeautifulSoup(request.text, 'html.parser')
        headlines = soup.findAll('h2',"story-title")
        titles = []
        for i in headlines:
            titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
        headlines = soup.findAll('h2',"story-title")
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
        request = requests.get('https://www.nytimes.com')
        soup = BeautifulSoup(request.text, 'html.parser')
        headlines = soup.findAll('h2',"css-1vvhd4r esl82me0")
        for i in headlines:
            titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
        allheadlines.append(titles)
        print('Fetching The Washington Post...')
        request = requests.get('https://www.washingtonpost.com/')
        soup = BeautifulSoup(request.text, 'html.parser')
        headlines = soup.findAll('div',{'class':"headline"})
        for i in headlines:
            titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
        allheadlines.append(titles)
        print('Fetching The Guardian...')
        request = requests.get('https://www.theguardian.com/us')
        soup = BeautifulSoup(request.text, 'html.parser')
        headlines = soup.findAll('a',{'class':"u-faux-block-link__overlay js-headline-text"})
        for i in headlines:
            titles.append(i.get_text().strip('\n').strip('\t').strip(' '))
        allheadlines.append(titles)
        return(titles)
    def findmostusedword(excluded):
        wordlist = []
        nouns = ['NN','NNS','NNP','NNPS']
        prev = [0,0]
        for headline in news:
            for word in headline.split():
                word = word.lower()
                wordlist.append(word)
        for word in wordlist:
            if not word in nouse:
                word = TextBlob(word)
                if word.tags == []:
                    continue
                if word.tags[0][1] in nouns:
                    if wordlist.count(word) > prev[1]:
                        prev = [word.tags[0][0],wordlist.count(word)]             
        return(prev)
    news = getheadlines()
    nouse = ['—','i']
    mostused = []
    print("Counting Occurences...")
    for i in range(top):
        mostused.append(findmostusedword(nouse))
        nouse.append(mostused[i][0])
    return(mostused)
def gettopx(x):
    return(main(x))
#print("Right now, the most used word in article titles is " + mostused[0] + ", being used " + str(mostused[1]) + " times!")
# again = input("return the next most used? [y]/n")
# while again == "y" or again == "":
#     mostused = findmostusedword(nouse)
#     print("Right now, the next most used word in article titles is " + mostused[0] + ", being used " + str(mostused[1]) + " times!")
#     nouse.append(mostused[0])
#     again = input("return the next most used? [y]/n")
# print("Thank you for Using the 'word of the day' script!")
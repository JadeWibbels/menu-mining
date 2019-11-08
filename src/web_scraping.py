import urllib
import requests
#from urllib import request

from bs4 import BeautifulSoup


class Digger:
    def __init__(self, countries):
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
        self.countries = countries
        self.data_leak_words = ["b'", 'b"', 'a', 'the', 'and', 'for', 'about', 'to', 'in', 'is', 'or', 'so', 'i', 'greek', 'german', 'filipino', 'indian', 'indonesian', 'cajun', 'carribean', 'italian', 'mexican', 'chinese', 'thai', 'vietnamese', 'french', 'japanese', 'irish', 'koren', 'russian', '(tm)', 'categories', 'v8.04', 'recipe', 'via', 'meal master', 'mealmaster', 'v8.03', 'v8.02', 'v8.01', 'exported', 'from', 'mastercook', 'title', 'philippine', 'philippina', 'v7.02\r', '\r']

    def dig_soup(self, c):
        print(c)
        response = requests.get(self.countries[c]['link'], self.header)
        soup = BeautifulSoup(response.content, "html.parser")
        for li in soup.findAll('ol'):
            for link in li.findAll('a'):
                child_url = self.countries[c]['link'].replace('indexall.html', '') + link.get('href')
                plain_text = self.dig_plain_text(child_url)
                #print(child_url)
                self.countries[c]['recipes'].append(self.digger_soup(plain_text))
        print(c, ': ', len(self.countries[c]['recipes']))
    
    def dig_plain_text(self, url):
        core = 'https://www.recipesource.com'
        response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        try:
            soup = BeautifulSoup(response.content, "html.parser")
        except:
            soup = BeautifulSoup(request.urlopen(request.Request(url, headers= {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'})).read(), "lxml")
        plain = soup.find_all('p', attrs={'class': 'plainlink'})
        #print(plain)
        for div in plain:
            links = div.findAll('a')
            for a in links:
                return core + a['href']
            
    def digger_soup(self, url):
        #print(url)
        response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        try:
            soup = BeautifulSoup(response.content, "html.parser")
        except:
            soup = BeautifulSoup(request.urlopen(request.Request(url, headers= {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'})).read(), "lxml")
        #print(response.content)
        r_init = str(response.content)
        r_clean = self.remove_leak_words(r_init)
        return r_clean
    
    def remove_leak_words(self, r):
        r = r.lower()
        rwords = r.split()
        clean_words = []
        for word in rwords:
            clean_word = word.replace('\\n', ' ').replace('-', ' ').replace('mmmmm', ' ').replace('*', ' ').replace('\r', ' ').replace(':', ' ').replace(',', ' ')
            if clean_word.strip() not in self.data_leak_words:
                clean_words.append(clean_word)
        result = ' '.join(clean_words)
        while '  ' in result:
            result = result.replace('  ', ' ').strip()
        return result
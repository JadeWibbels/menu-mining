from urllib import request
import requests

from bs4 import BeautifulSoup

# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}


def dig_soup(url, recipe_list):
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.findAll('a'):
        if link.get('href') == 'indexall.html':
            child_url = url+ '/indexall.html'
            all_r = dig_soup(child_url, recipe_list)
    for li in soup.findAll('ol'):
        for link in li.findAll('a'):
            child_url = url+ link.get('href')
            #print(child_url)
            recipe_list.append(digger_soup(child_url))
    print(recipe_list)
    return recipe_list
            
            
def digger_soup(url):
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    print(url)
    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except:
        soup = BeautifulSoup(request.urlopen(request.Request(url, headers=HEADERS)).read(), "lxml")
    for r in soup.findAll('pre'):
        r = str(r).strip()
        r = create_recipe(r)
        return r

def create_recipe(r):
    r = r.replace('<pre>', '').replace('</pre>', '').replace('\n', '').replace('\t', '').replace('-', ' ')
    r = r.replace('MMMMM', '').strip()
    while '  ' in r:
        r = r.replace('  ', ' ')
    return r
    
r = dig_soup('https://recipesource.com/ethnic/europe/irish', [])
#print(r)
        
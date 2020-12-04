import requests
from bs4 import BeautifulSoup


def getHotSearch():
    url = 'https://www.ghpym.com/'
    source_code = requests.get(url)
    source_code.encoding = 'UTF-8'
    soup = BeautifulSoup(source_code.content, 'html.parser')
    div = soup.find('div', class_='widget widget_lastest_news')
    ul = div.find('ul')
    lilist = ul.find_all('li')
    for li in lilist:
        a = li.find('a')
        href = a.get('href')
        source_code2 = requests.get(href)
        source_code2.encoding = 'UTF-8'
        soup2 = BeautifulSoup(source_code2.content, 'html.parser')
        timeel = soup2.find('time', class_='entry-date published')
        datetime = timeel.get('datetime')
        print(datetime.split('T')[0] + '\n' + a.string + '\n' + href)


getHotSearch()

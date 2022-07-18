import requests
from bs4 import BeautifulSoup
url4 = 'https://www.goodreads.com/book/show/54578818-fuse'
r4 = requests.get(url4)
source4 = r4.content
soup4 = BeautifulSoup(source4, 'html.parser')
rating4 = soup4.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate4 = soup4.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate4)
rating_s34= soup4.find('a', class_ = 'gr-hyperlink')
rate_s4 = soup4.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s4)
review4 = soup4.find('a', class_ = 'gr-hyperlink')
rev4 = soup4.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev4)
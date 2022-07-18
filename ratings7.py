import requests
from bs4 import BeautifulSoup
url7 = 'https://www.goodreads.com/book/show/46144864-a-map-is-only-one-story'
r7 = requests.get(url7)
source7 = r7.content
soup7 = BeautifulSoup(source7, 'html.parser')
rating7 = soup7.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate7 = soup7.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate7)
rating_s7= soup7.find('a', class_ = 'gr-hyperlink')
rate_s7 = soup7.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s7)
review7 = soup7.find('a', class_ = 'gr-hyperlink')
rev7 = soup7.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev7)
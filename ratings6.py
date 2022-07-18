import requests
from bs4 import BeautifulSoup
url6 = 'https://www.goodreads.com/book/show/54578811-letters-from-johnny'
r6 = requests.get(url6)
source6 = r6.content
soup6 = BeautifulSoup(source6, 'html.parser')
rating6 = soup6.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate6 = soup6.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate6)
rating_s6= soup6.find('a', class_ = 'gr-hyperlink')
rate_s6 = soup6.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s6)
review6 = soup6.find('a', class_ = 'gr-hyperlink')
rev6 = soup6.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev6)
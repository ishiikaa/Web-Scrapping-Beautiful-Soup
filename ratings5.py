import requests
from bs4 import BeautifulSoup
url5 = 'https://www.goodreads.com/book/show/40030311-almost-american-girl'
r5 = requests.get(url5)
source5 = r5.content
soup5 = BeautifulSoup(source5, 'html.parser')
rating5 = soup5.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate5 = soup5.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate5)
rating_s5= soup5.find('a', class_ = 'gr-hyperlink')
rate_s5 = soup5.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s5)
review5 = soup5.find('a', class_ = 'gr-hyperlink')
rev5 = soup5.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev5)
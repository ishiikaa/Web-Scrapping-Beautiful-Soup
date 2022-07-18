import requests
from bs4 import BeautifulSoup
url10 = 'https://www.goodreads.com/book/show/52568667-tales-from-the-bottom-of-my-sole'
r10 = requests.get(url10)
source10 = r10.content
soup10 = BeautifulSoup(source10, 'html.parser')
rating10 = soup10.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate10 = soup10.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate10)
rating_s10= soup10.find('a', class_ = 'gr-hyperlink')
rate_s10 = soup10.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s10)
review10 = soup10.find('a', class_ = 'gr-hyperlink')
rev10 = soup10.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev10)
import requests
from bs4 import BeautifulSoup
url8 = 'https://www.goodreads.com/book/show/54578815-the-language-we-were-never-taught-to-speak'
r8 = requests.get(url8)
source8 = r8.content
soup8 = BeautifulSoup(source8, 'html.parser')
rating8 = soup8.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate8 = soup8.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate8)
rating_s8= soup8.find('a', class_ = 'gr-hyperlink')
rate_s8 = soup8.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s8)
review8 = soup8.find('a', class_ = 'gr-hyperlink')
rev8 = soup8.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev8)
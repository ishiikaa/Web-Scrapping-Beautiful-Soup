import requests
from bs4 import BeautifulSoup
url9 = 'https://www.goodreads.com/book/show/45010953-a-nail-the-evening-hangs-on'
r9 = requests.get(url9)
source9 = r9.content
soup9 = BeautifulSoup(source9, 'html.parser')
rating9 = soup9.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate9 = soup9.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate9)
rating_s9= soup9.find('a', class_ = 'gr-hyperlink')
rate_s9 = soup9.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s9)
review9 = soup9.find('a', class_ = 'gr-hyperlink')
rev9 = soup9.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev9)
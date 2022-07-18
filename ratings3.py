import requests
from bs4 import BeautifulSoup
url3 = 'https://www.goodreads.com/book/show/53029244-obit'
r3 = requests.get(url3)
source3 = r3.content
soup3 = BeautifulSoup(source3, 'html.parser')
rating3 = soup3.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate3 = soup3.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate3)
rating_s3 = soup3.find('a', class_ = 'gr-hyperlink')
rate_s3 = soup3.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s3)
review3 = soup3.find('a', class_ = 'gr-hyperlink')
rev3 = soup3.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev3)

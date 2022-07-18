import requests
from bs4 import BeautifulSoup
url2 = "https://www.goodreads.com/book/show/54578808-why-do-you-look-at-me-and-see-a-girl"
r2 = requests.get(url2)
source2 = r2.content
soup2 = BeautifulSoup(source2, 'html.parser')
rating2 = soup2.find('div', id = 'metacol', class_ = 'last col').find('div', id = 'bookMeta', class_ = 'uitext stacked')
rate2 = soup2.find('span', itemprop = 'ratingValue').get_text(strip = True)
print(rate2)
rating_s2 = soup2.find('a', class_ = 'gr-hyperlink')
rate_s2 = soup2.find('meta', itemprop = 'ratingCount').get_text(strip = True)
print(rate_s2)
review2 = soup2.find('a', class_ = 'gr-hyperlink')
rev2 = soup2.find('meta', itemprop = 'reviewCount').get_text(strip = True)
print(rev2)


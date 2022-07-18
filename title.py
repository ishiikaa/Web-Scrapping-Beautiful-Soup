from bs4 import BeautifulSoup
import requests

url = "https://www.goodreads.com/list/show/147668.E_J_Koh_s_Books_to_Celebrate_Asian_American_Fiction_Non_Fiction_Memoir_Graphic_Novel_and_Poetry"
r = requests.get(url)
source = r.content
soup = BeautifulSoup(source, 'html.parser')
books = soup.find('table', class_= "tableList js-dataTooltip").find_all('tr')
"""print(len(books))"""
for book in books:
    name = book.find("a", class_ = "bookTitle").get_text(strip=True)
    print(name)
    
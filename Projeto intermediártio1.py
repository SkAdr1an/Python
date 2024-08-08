Scraper Web.py 
Venezuela news 31/07
-----------------------------------
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://g1.globo.com'  

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('a', href=True)
    
    with open('venezuela_news.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Link'])  

        for article in articles:
            link = article['href']
            if '/noticia/' in link:
                title = article.get_text(strip=True)
                
                if 'Venezuela' in title or 'Venezuela' in link:
                    writer.writerow([title, link])

    print('Dados salvos em venezuela_news.csv')
else:
    print('Falha ao acessar o site:', response.status_code)
--------------------------------------------------------------------------------------------
Leitura de arquivo csv.

import csv

csv_file_path = 'venezuela_news.csv'

def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            data.append(row)
    return data

news_data = read_csv(csv_file_path)


print("Notícias sobre a Venezuela:")
for title, link in news_data:
    print(f"Title: {title}")
    print(f"Link: {link}\n")


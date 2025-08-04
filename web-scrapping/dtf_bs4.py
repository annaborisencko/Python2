import requests
import bs4
import json

response = requests.get('https://dtf.ru/games')
soup = bs4.BeautifulSoup(response.text, features='lxml')

articles = soup.find('div', class_='content-list')
articles_list = articles.find_all('div', class_='content content--short')

parsed_data = []
for article in articles_list:
    link = 'https://dtf.ru' + article.find('a', class_='content__link')['href']
    response = requests.get(link)
    article_soup = bs4.BeautifulSoup(response.text, features='lxml')
    title = article_soup.find('h1').text.strip()
    time = article_soup.find('time')['datetime']
    text = article_soup.find('article', class_='content__blocks').text.strip()
    parsed_data.append({
        'title': title,
        'link': link,
        'text': text,
        'time': time
    })

with open('articles.json', 'w') as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)


# from fake_headers import Headers
#
# headers = Headers(browser='chrome', os='mac').generate()
# response = requests.get('https://hh.ru/', headers=headers)
# print(response.text)
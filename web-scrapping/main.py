## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

## Ваш код
import time
from time import  sleep
from pprint import pprint

from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, Keys, ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import re

# Функция для гарантии загрузки страницы до начала поиска элементов
def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None


chrome_path = ChromeDriverManager().install()
# Для запуска браузера без графического интерфейса
options = ChromeOptions()
# options.add_argument('--headless=new') 
service = Service(executable_path=chrome_path)
browser = Chrome(service=service, options=options)



browser.get('https://habr.com/ru/all/')
sleep(1)

articles_list = browser.find_elements(by=By.CSS_SELECTOR, value='article.tm-articles-list__item')

# Ищем подходящие статьи по вхождению слов из KEYWORDS в preview тексте статей
def find_word_in_preview(articles_list):
# Ищем подходящие статьи по вхождению слов из KEYWORDS в тексте превью
    match_articles_list = []
    for article in articles_list:        
        match_link_list = [] #Список статей, которые уже были пройдены и добавлены в подходящие
        #Поучаем текст превью статьи
        preview_text = wait_element(browser=article, by=By.CSS_SELECTOR, value='div.tm-article-snippet.tm-article-snippet').text.lower().strip()
        #Проверяем наличие слова из заданного списка в тексте превью
        for word in KEYWORDS:
            article_info = {}
            # Ищем только слова из KEYWORDS и их формы, исключаем слово дизайнер 
            pattern = r"\b" + word + r"(?!ер)\w*\b"
            result = re.findall(pattern, preview_text)
            #Если слово найдено в тексте превью статьи, добавляем ее в список подходящих
            if len(result) != 0:
                article_info['date'] = wait_element(browser=article, by=By.TAG_NAME, value='time').get_attribute('datetime')
                article_info['title'] = wait_element(browser=article, by=By.TAG_NAME, value='h2').text
                article_info['link'] = wait_element(browser=article, by=By.CSS_SELECTOR, value='a.tm-title__link').get_attribute('href')
                if not article_info['link'] in match_link_list:
                    match_link_list.append(article_info['link'])
                    match_articles_list.append(article_info)
                else:
                    print(f"Статья \"{article_info['title']}\" уже добавлена с список")
    return match_articles_list

# Ищем подходящие статьи по вхождению слов из KEYWORDS в полном тексте статей
def find_word_in_fulltext(articles_list):
    article_link_list = []
    for article in articles_list:
        link = wait_element(browser=article, by=By.CSS_SELECTOR, value='a.tm-title__link').get_attribute('href')
        article_link_list.append(link)

    match_article_list = []
    match_article_link = []
    for article_link in article_link_list:
        browser.get(article_link)
        text = wait_element(browser, by=By.TAG_NAME, value='article').text.lower().strip()
        for word in KEYWORDS:
            article_info = {}
            # Ищем только слова из KEYWORDS и их формы, исключаем слово дизайнер 
            pattern = r"\b" + word + r"(?!ер)\w*\b"
            result = re.findall(pattern, text)
            if len(result) != 0:
                article_info['date'] = wait_element(browser, by=By.TAG_NAME, value='time').get_attribute('datetime')
                article_info['title'] = wait_element(browser, by=By.TAG_NAME, value='h1').text
                article_info['link'] = article_link    

                if not article_link in match_article_link:
                    match_article_link.append(article_link)
                    match_article_list.append(article_info)

    return match_article_list

# Ищем подходящие статьи по вхождению слов из KEYWORDS в полном тексте статей при значении preview_only=False или в preview тексте статей при значении preview_only=True
def find_word_in_article(articles_list, keywords, preview_only=True):
    article_info = {}
    article_info_list = []

    #Получаем основную информацию о статьях 
    for article in articles_list:
        article_info={
            'link': wait_element(browser=article, by=By.CSS_SELECTOR, value='a.tm-title__link').get_attribute('href'),
            'date': wait_element(browser=article, by=By.TAG_NAME, value='time').get_attribute('datetime'),
            'title': wait_element(browser=article, by=By.TAG_NAME, value='h2').text,
            'text': wait_element(browser=article, by=By.CSS_SELECTOR, value='div.tm-article-snippet.tm-article-snippet').text.lower().strip()
        }
        article_info_list.append(article_info)
    
    #Получаем полный текст статьи для поиска ключевых слов, если preview_only == False
    if preview_only == False:
        for info in article_info_list:
            browser.get(info['link'])
            browser_link = browser.find_element(by=By.CSS_SELECTOR, value='div.tm-misprint-area__wrapper')
            info['text'] = wait_element(browser=browser_link, by=By.TAG_NAME, value='article').text.lower().strip()

    #Ищем ключевые слова в полученном тексте и собираем подходящие статьи
    match_article_list = []
    match_article_link_list = []
    for info in article_info_list:
        # print(info['text'])
        for word in keywords:

            # Ищем только слова из KEYWORDS и их формы, исключаем слово дизайнер 
            pattern = r"\b" + word + r"(?!ер)\w*\b"
            result = re.findall(pattern, info['text'])

            #Если слово найдено в тексте или превью статьи, добавляем ее в список подходящих
            if len(result) != 0 and info['link'] not in match_article_link_list:
                match_article_link_list.append(info['link'])
                match_article_list.append(info)
    
    return match_article_list


# match_articles = find_word_in_preview(articles_list)            
# for article in match_articles:
#     print(f"{article['date']} - {article['title']} - {article['link']}")

# match_articles = find_word_in_fulltext(articles_list)            
# for article in match_articles:
#     print(f"{article['date']} - {article['title']} - {article['link']}")

match_articles = find_word_in_article(articles_list, KEYWORDS, preview_only=False)
for article in match_articles:
    print(f"{article['date']} - {article['title']} - {article['link']}")
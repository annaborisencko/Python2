import json
import time
from time import  sleep


from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait_element(browser, delay=3, by=By.TAG_NAME, value=None):
    try:
        return WebDriverWait(browser, delay).until(
            expected_conditions.presence_of_element_located((by, value))
        )
    except TimeoutException:
        return None


chrome_path = ChromeDriverManager().install()
service = Service(executable_path=chrome_path)
browser = Chrome(service=service)

browser.get('https://dtf.ru/games')
sleep(1)

# # articles_list = articles.find_all('div', class_='content content--short')
# articles_list = browser.find_elements(by=By.CSS_SELECTOR, value='div.content--short')
#
# link_list = []
# for article in articles_list:
#     # link = 'https://dtf.ru' + article.find('a', class_='content__link')['href']
#     link = (wait_element(browser=article, by=By.CSS_SELECTOR, value='a.content__link')
#             .get_attribute('href'))
#     link_list.append(link)
#
# parsed_data = []
# for link in link_list:
#     # response = requests.get(link)
#     # article_soup = bs4.BeautifulSoup(response.text, features='lxml')
#     browser.get(link)
#
#     # title = article_soup.find('h1').text.strip()
#     title = wait_element(browser, by=By.TAG_NAME, value='h1').text.strip()
#
#     # time = article_soup.find('time')['datetime']
#     time = wait_element(browser, by=By.TAG_NAME, value='time').get_attribute('datetime')
#
#     # text = article_soup.find('article', class_='content__blocks').text.strip()
#     text = (wait_element(browser, by=By.CSS_SELECTOR, value='article.content__blocks')
#             .text.strip())
#
#     parsed_data.append({
#         'title': title,
#         'link': link,
#         'text': text,
#         'time': time
#     })
#
# with open('articles2.json', 'w') as f:
#     json.dump(parsed_data, f, ensure_ascii=False, indent=4)


search_button = wait_element(browser,
                             by=By.CSS_SELECTOR,
                             value='button.search__button')
search_button.click()
time.sleep(3)
input_field = wait_element(browser,
                           by=By.CSS_SELECTOR,
                           value='input.text-input')
input_field.send_keys('hollow knight')
input_field.send_keys(Keys.ENTER)
time.sleep(10)


# chrome_path = ChromeDriverManager().install()
# options = ChromeOptions()
# options.add_argument('--headless')
# service = Service(executable_path=chrome_path)
# browser = Chrome(service=service, options=options)

# Для запуска браузера без графического интерфейса
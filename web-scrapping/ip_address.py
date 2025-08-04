# http://jursite.garant.ru/legal-issues/big-data-and-intellectual-property-a-systematic-study-of-scraping-as-part-of-a-common-internet-law-methodology
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/actions_api/test_wheel.py#L11-L14
# https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/actions_api/test_mouse.py#L24-L27
# https://iqss.github.io/dss-webscrape/filling-in-web-forms.html
# https://stepik.org/course/575/syllabus

# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install fake_headers
# pip install selenium
# pip install webdriver-manager


'''
<span class="table-ip4-home">
                           92.38.87.60                           </span>
'''

import requests
import bs4

response = requests.get('https://www.iplocation.net/')
# print(response.text.xml)

soup = bs4.BeautifulSoup(response.text, features='lxml')
# span_ip = soup.find('span', attrs={'class': 'table-ip4-home'})
span_ip = soup.find('span', class_='table-ip4-home')
# print(span_ip)
print(span_ip.text.strip())

# span_ip = soup.select_one('span.table-ip4-home')
# print(span_ip.text.xml.strip())



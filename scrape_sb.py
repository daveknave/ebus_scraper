import db_connector
import requests, time, json
from bs4 import BeautifulSoup as bs

def grab_data():
   pass

def find_next_page(soup, identifier_string):
   pagelink = soup.select_one(identifier_string).find_next_sibling()
   hyper_link = pagelink.find('a', recursive=False)
   return hyper_link.attrs.get('href')

def load_article_data(soup, identifier_string):
   for pagelink in soup.select(identifier_string):
      article_url = pagelink.find('a', recursive=False).attrs.get('href')
      article_data = requests.get(article_url)


def add_article_to_db(soup, identifier_string):
   pass



result = requests.get('https://www.sustainable-bus.com/category/electric-bus/')
main_soup = bs(result.content)

### Pagination
while True:
   time.sleep(1)
   next_page_url = find_next_page(main_soup, '.pagination__item.is-active')
   print(next_page_url)
   if not next_page_url: break

   next_page = requests.get(next_page_url)

   if not next_page.status_code in [200, 300, 301, 302]:
      print(next_page.status_code, next_page.reason)
      break

   main_soup = bs(next_page.content)
   load_article_data(main_soup, '')




grab_data()

# import db_connector
import datetime as dt
import requests, time, json, pandas as pd
from bs4 import BeautifulSoup as bs
import sqlite3
import hashlib
import markdownify as mdy

def grab_data():
   pass

def find_next_page(soup, identifier_string):
   pagelink = soup.select_one(identifier_string).find_next_sibling()
   hyper_link = pagelink.find('a', recursive=False)
   return hyper_link.attrs.get('href')

def load_article_data(soup, identifier_string, memory_arr):
   for pagelink in soup.select(identifier_string):
      article_url = pagelink.select_one('.item__link', recursive=True).attrs.get('href')

      article_data = {}
      article_data['title'] = pagelink.select_one('.item__title', recursive=False).text.strip('\t\r\n')
      article_data['date'] = dt.datetime.strptime(
         pagelink.select_one('.item__data.item__data--date', recursive=False).text.strip('\t\r\n '),
         '%d %B %Y'
      )
      keywords_arr = pagelink.select_one('.item__category', recursive=False).text.strip('\t\r\n').split(',')
      article_data['tags'] = ';'.join(keywords_arr)

      ### Open Article Page
      article = requests.get(article_url)
      article_soup = bs(article.content)
      article_data['text'] = mdy.markdownify(str(article_soup.select_one('.prose')))

      name_date_str = article_data['title'] + article_data['date'].strftime('%Y-%m-%d')
      uid = hashlib.md5(name_date_str.encode()).hexdigest()
      memory_arr[uid] = article_data
      time.sleep(1)
   return memory_arr


def add_article_to_db(soup, identifier_string):
   pass



result = requests.get('https://www.sustainable-bus.com/category/electric-bus/')
main_soup = bs(result.content)

article_list = {}

load_article_data(main_soup, 'article.item', article_list)
### Pagination
while True:
   next_page_url = find_next_page(main_soup, '.pagination__item.is-active')
   print(next_page_url)
   if not next_page_url: break

   next_page = requests.get(next_page_url)

   if not next_page.status_code in [200, 300, 301, 302]:
      print(next_page.status_code, next_page.reason)
      break

   main_soup = bs(next_page.content)
   load_article_data(main_soup, 'article.item', article_list)

   con = sqlite3.connect('scraping_01.db')
   articles_df = pd.DataFrame(data=article_list)
   articles_df.transpose().to_sql('articles', con, if_exists='replace')
   con.close()

   break


grab_data()

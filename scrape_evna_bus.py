# import db_connector
import datetime as dt
import requests, time, json, pandas as pd
from bs4 import BeautifulSoup as bs
import sqlite3
import hashlib
import markdownify as mdy


def load_article_data(soup, identifier_string, memory_arr):
   for pagelink in soup.select(identifier_string):
      article_url = 'https://insideevs.com' + pagelink.select_one('.thumb', recursive=True).attrs.get('href')
      print(article_url)
      article_data = {}
      article_data['title'] = pagelink.select_one('h3', recursive=False).text.strip('\t\r\n')
      article_data['date'] = dt.datetime.strptime(
         pagelink.select_one('span.date', recursive=False).text.strip('\t\r\n '),
         '%d %B %Y'
      )
      keywords_arr = ''
      article_data['tags'] = ';'.join(keywords_arr)
      article_data['source'] = 'evna_bus'
      ### Open Article Page
      article = requests.get(article_url)
      article_soup = bs(article.content)
      for s in article_soup.select('script'):
         s.extract()
      for s in article_soup.select('div.share-list'):
         s.extract()
      article_data['text'] = str(article_soup.select_one('.postContent'))
      name_date_str = article_data['title'] + article_data['date'].strftime('%Y-%m-%d')
      uid = hashlib.md5(name_date_str.encode()).hexdigest()
      memory_arr[uid] = article_data
      time.sleep(0.5)
   return memory_arr

def scrape():
   page = 1

   while True:
      article_list = {}
      print('https://insideevs.com/news/category/bus?p=' + str(page))
      result = requests.get('https://insideevs.com/news/category/bus?p=' + str(page))
      main_soup = bs(result.content)

      try:
         load_article_data(main_soup, 'div.item.wcom', article_list)
      except AttributeError as e:
         break

      con = sqlite3.connect('scraping_01.db')
      articles_df = pd.DataFrame(data=article_list)
      articles_df.transpose().to_sql('articles', con, if_exists='append')
      con.close()

      page+=1


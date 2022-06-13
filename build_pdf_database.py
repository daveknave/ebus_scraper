import sqlite3
from urllib.parse import urlencode

import pandas as pd
import os.path
import markdown, pdfkit, os
import datetime as dt
import bs4

from sklearn.preprocessing import MinMaxScaler


def generate_pdf(data):
    # config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'load-error-handling' : 'ignore'
    }
    wordcloud = '<ul style="list-style:none;">'
    country_counts = pd.read_json(data['location']).reset_index()
    sc = MinMaxScaler()
    country_counts['count'] = sc.fit_transform(country_counts[['count']])

    for idx, country in country_counts.iterrows():
        wordcloud = wordcloud + '<li style="font-size:' + str(1.0+country['count']) + 'em">' + country['index'] + '</li>'

    wordcloud = wordcloud + '</ul>'

    mdo = '<h1>' + data['title'] + '</h1>' + data['date'].split(' ')[0] + '  |  ' + data['tags'] + '<br/><br/>'+ wordcloud + '<br/>' + data['text']

    mdo = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style type="text/css">
                body {
                    font-family: sans, Arial;
                }
                img {
                    width: 50%%;
                    height: auto !important;
                    margin-right: 20px;
                    margin-top: 20px;
                    margin-bottom: 20px;
                    float: left;                  
                }
                hr, .userRThumb {
                    display: none;
                }
                .parent-shareBox, .tip-us-email-container {
                    display: none;
                }
                
            </style>            
        </head>
        <body>   
        %s
        </body>
        <html>
    """ % (mdo)
    if not os.path.isdir(data['source']):
        os.mkdir(data['source'])

    print(os.path.join(os.getcwd(), data['source'], data['date'] + '_' + data['title'].replace('/', '') + '.pdf'))

    curr_soup = bs4.BeautifulSoup(mdo)
    for img in curr_soup.findAll('img'):
        if '...' in img['src']:
            img.decompose()

    pdfkit.from_string(str(curr_soup), output_path=os.path.join(os.getcwd(), urlencode(data['source'], data['date'].split(' ')[0] + '_' + data['title'][:16]) + '.pdf'))


def export_to_pdf():
    con = sqlite3.connect('scraping_01.db')
    articles_df = pd.read_sql("""select distinct * from searchable_articles where
                               searchable_articles MATCH 'tender* ' ||
                                                         'OR order* ' ||
                                                         'OR buy_ ' ||
                                                         'OR win_ ' ||
                                                         'OR won ' ||
                                                         'OR rollout ' ||
                                                         'OR aqui* ' ||
                                                         'OR deliver*' ||
                                                         'OR purchase_'
    order by date""", con)

    con.close()
    articles_df.apply(lambda c: generate_pdf(c), axis=1)


export_to_pdf()

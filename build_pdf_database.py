import sqlite3
import pandas as pd
import os.path
import markdown, pdfkit, os
import datetime as dt
#%%
def export_to_pdf():
    # os.chdir(r'C:\Users\David\PycharmProjects\ebus_scraper')
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    con = sqlite3.connect('scraping_01.db')
    articles_df = pd.read_sql('SELECT DISTINCT * FROM articles', con)

    con.close()
    #%%

    def generate_pdf(data):
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        # mdo = markdown.markdown('#' + data['title'] + '\n' + data['date'].split(' ')[0] + '  |  ' + data['tags'] + '\n\n' + data['text'], output_format='html5')
        mdo = '<h1>' + data['title'] + '</h1>' + data['date'].split(' ')[0] + '  |  ' + data['tags'] + '<br/><br/>' + data['text']
        print(mdo)
        mdo = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style type="text/css">
                    img {
                        width: 50%%;
                        height: auto !important;
                        margin-right: 20px;
                        margin-top: 20px;
                        margin-bottom: 20px;
                        float: left;                  
                    }
                    hr {
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
        """ % mdo
        if not os.path.isdir(data['source']):
            os.mkdir(data['source'])
        pdfkit.from_string(mdo, data['source'] + '/' + data['date'] + '_' + data['title'].replace('/', '') + '.pdf', options=options)
    articles_df.apply(lambda c: generate_pdf(c), axis=1)
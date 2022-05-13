import sqlite3
import pandas as pd
import markdown, pdfkit, os


os.chdir(r'C:\Users\David\PycharmProjects\ebus_scraper')

config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')

con = sqlite3.connect('scraping_01.db')
articles_df = pd.read_sql('SELECT DISTINCT * FROM articles', con)

con.close()
os.chdir('pdf_out')
#%%

def generate_pdf(data):
    mdo = markdown.markdown(('#' + data['title'] + '\n' + data['text']).replace('\n', '<br>'), output_format='html4')
    pdfkit.from_string(mdo, data['index'] + '.pdf')
articles_df.apply(lambda c: generate_pdf(c), axis=1)
import sqlite3
import pandas as pd
import os.path
import markdown, pdfkit, os
import datetime as dt
from bs4 import BeautifulSoup
import spacy
from spacy import displacy

con = sqlite3.connect('scraping_01.db')
articles_df = pd.read_sql('SELECT DISTINCT * FROM articles', con)
articles_df = articles_df.drop(columns='level_0')
con.close()

def determine_place(d):
    global articles_df
    print('Article', d.name, 'of', articles_df.shape[0])
    ### https://medium.com/spatial-data-science/how-to-extract-locations-from-text-with-natural-language-processing-9b77035b3ea4
    nlp = spacy.load("en_core_web_sm")
    # nlp = spacy.load("xx_ent_wiki_sm")
    tmp_soup = BeautifulSoup(d['text'])
    doc = nlp(tmp_soup.text)
    locs = pd.DataFrame([c.text for c in doc.ents if c.label_ in ['LOC', 'GPE']])
    if locs.empty: return ''
    locs = locs.rename(columns={0 : 'location'})
    locs['location'] = locs['location'].str.replace('.', '')
    locs['location'] = locs['location'].str.replace(r'   .+', '', regex=True)
    locs['location'] = locs['location'].str.lower()
    locs = locs.rename(columns={0 : 'location'})
    loc_counts = locs.groupby('location', as_index=False).apply(lambda a: pd.Series({'location' : a.location.iloc[0], 'count' : a.shape[0]}))

    loc_counts = loc_counts.sort_values(by=['count'], ascending=False).head(10).reset_index()

    return loc_counts.set_index('location').drop(columns='index').to_json(orient='columns')


articles_df['location'] = articles_df.apply(lambda a: determine_place(a), axis=1)
#%%
con = sqlite3.connect('scraping_01.db')
articles_df.to_sql('articles', con, if_exists='replace')
con.close()
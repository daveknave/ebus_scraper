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
locations = pd.read_sql('SELECT DISTINCT * FROM locations', con)
con.close()
#%%
def determine_place(d):
    global locations
    ### https://medium.com/spatial-data-science/how-to-extract-locations-from-text-with-natural-language-processing-9b77035b3ea4
    # nlp = spacy.load("en_core_web_sm")
    nlp = spacy.load("xx_ent_wiki_sm")
    tmp_soup = BeautifulSoup(d['text'])
    doc = nlp(tmp_soup.text)
    locs = pd.DataFrame([c.text for c in doc.ents if c.label_ in ['LOC']])
    locs[0] = locs[0].str.replace('.', '')
    locs[0] = locs[0].str.replace(r'   .+', '', regex=True)
    locs = locs.rename(columns={0 : 'location'})
    loc_counts = locs.groupby('location', as_index=False).apply(lambda a: (a['location'], a.count()))
    loc_counts = loc_counts.sort_values(by=['location']).head(3)




locs_df = articles_df.head(1).apply(lambda a: determine_place(a), axis=1)
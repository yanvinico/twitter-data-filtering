from logging import info
import pandas as pd
from os import path, getcwd

def all_movies():
    info("Starting movies search")
    columns = ['tconst','titleType','startYear']
    FILE_PATH = path.join(getcwd(), 'csv', 'title.basics.tsv.gz')
    movies_df = []
    load = pd.read_table(FILE_PATH, compression='gzip', usecols=columns, sep='\t', dtype= {'titleType': 'category', 'startYear': 'string'}, chunksize=100000, low_memory= False)
    info("Reading table title basics")
    for chunk in load:
        df =chunk
        df['startYear'] = df['startYear'].replace(['\\N'], '0000')
        df['startYear'] = df['startYear'].astype(int)
        df = df.loc[(df['titleType'] == 'movie') & (df['startYear'] >= 2012)]
        df = df['tconst']
        if not df.empty:
            movies_df.append(df)
    info("Ending movies search")
    all_movies_df = pd.concat(movies_df)
    info("Movies were Found")
    return all_movies_df



from logging import info
from os import path, getcwd
import pandas as pd

def actors_id(movies_id):
    info("Starting ids search")
    columns = ['tconst','nconst','category']
    FILE_PATH = path.join(getcwd(), 'csv', 'title.principals.tsv.gz')
    actors_id_df = []
    load = pd.read_table(FILE_PATH,compression='gzip', sep='\t', usecols=columns, dtype={'category': 'string', 'tconst': 'string', 'nconst': 'string'}, chunksize=100000, low_memory= False)
    info("Reading table title principals")
    for chunk in load:
        df = chunk
        df_category = df.loc[(df['category'] == 'actor') | (df['category'] == 'actress')]
        df_actors_merge = pd.merge(movies_id, df_category, on=[('tconst')])
        df_top = df_actors_merge['nconst']
        if not df_top.empty:
            actors_id_df.append(df_top)
    info("Ending ids search")
    actors = pd.concat(actors_id_df)
    info("Actors id were found")
    return actors

def top_id(actors, index_top):
    df =pd.DataFrame(actors)
    top_list = df.groupby(['nconst']).value_counts().index.tolist()[:index_top]
    info(f"top {index_top}: {top_list}")
    return top_list

def name_list(top_list):
    info("Starting names search")
    columns = ['nconst', 'primaryName']
    FILE_PATH = path.join(getcwd(), 'csv', 'name.basics.tsv.gz')
    load = pd.read_table(FILE_PATH, compression='gzip', usecols=columns, sep='\t', low_memory=False, dtype={'primaryName': 'string', 'nconst': 'string'}, chunksize=10000)
    actors_list = []
    info("Reading table name basics")
    for chunk in load:
        for reference in top_list:
            name = chunk[chunk['nconst'] == reference]
            actors_list.append(name)
    info("ending names search")
    id_actors = pd.concat(actors_list)
    list_actor_names = id_actors['primaryName'].to_list()
    info(f"top actors list name: {list_actor_names}")
    return list_actor_names






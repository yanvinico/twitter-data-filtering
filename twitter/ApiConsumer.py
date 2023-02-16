import pandas as pd
from os import path, mkdir, getcwd, remove
import tweepy
from twitter import Tokens
from logging import info

def search_actors_tweets(list):
    info("Searching tweets")
    client = tweepy.Client(bearer_token=Tokens.BEARER_TOKEN)
    dic_tweets = {}
    for name in list:
        tweets = []
        response = client.search_recent_tweets(query='{} -is:retweet'.format(name), max_results=10)
        if(not(response.data is None)):
            for tweet in response.data:
                tweets.append(tweet.text)
        dic_tweets[name] = tweets
    df =pd.DataFrame.from_dict(dic_tweets, orient='index')
    df = df.T.melt().dropna()
    df = df.explode('value')
    info("Tweets were found")
    return df
def download_result(df):
    path_dir = path.join(getcwd(), 'result')
    path_file = path.join(path_dir, 'results.csv')
    if not path.isdir(path_dir): mkdir(path_dir)
    if path.exists(path_file): remove(path_file)
    df.to_csv(path_file, index=False, sep='\t')
    info(f"The tweets were saved in the path: {path_file}")






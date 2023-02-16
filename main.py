import sys
from imdb import Names, Download
from twitter import ApiConsumer
from logging import basicConfig, INFO, FileHandler, StreamHandler

def main():
    basicConfig( level=INFO, format="%(asctime)s :: %(message)s", handlers=[FileHandler("records.log"), StreamHandler(sys.stdout)])
    Download.download_url()
    list_actors = Names.get_actors_imdb()
    result_actors = ApiConsumer.search_actors_tweets(list_actors)
    ApiConsumer.download_result(result_actors)

if __name__ == '__main__':
    main()
from logging import info
from urllib import request
from os import path, getcwd, mkdir

URL_NAME_BASICS = 'https://datasets.imdbws.com/name.basics.tsv.gz'
FILE_NAME_BASICS = 'name.basics.tsv.gz'

URL_TITLE_BASICS = 'https://datasets.imdbws.com/title.basics.tsv.gz'
FILE_TITLE_BASICS = 'title.basics.tsv.gz'

URL_TITLE_PRINCIPALS = 'https://datasets.imdbws.com/title.principals.tsv.gz'
FILE_TITLE_PRINCIPALS = 'title.principals.tsv.gz'

data_source = path.join(getcwd(), r'csv')

def download_url():
    name_basics_file = path.join(getcwd(), 'csv', FILE_NAME_BASICS)
    if not path.isdir(data_source): mkdir(data_source)
    info('Downloading file: ' + FILE_NAME_BASICS)
    request.urlretrieve(URL_NAME_BASICS, name_basics_file)

    title_basics_file = path.join(getcwd(), 'csv', FILE_TITLE_BASICS)
    if not path.isdir(data_source): mkdir(data_source)
    info('Downloading file: ' + FILE_TITLE_BASICS)
    request.urlretrieve(URL_TITLE_BASICS, title_basics_file)

    title_principals_file = path.join(getcwd(), 'csv', FILE_TITLE_PRINCIPALS)
    if not path.isdir(data_source): mkdir(data_source)
    info('Downloading file: ' + FILE_TITLE_PRINCIPALS)
    request.urlretrieve(URL_TITLE_PRINCIPALS, title_principals_file)


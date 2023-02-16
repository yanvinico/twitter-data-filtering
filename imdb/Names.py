from imdb import Actors
from imdb import Movies

def get_actors_imdb():
    get_movies = Movies.all_movies()
    get_actors_id = Actors.actors_id(get_movies)
    get_actors_names = Actors.top_id(get_actors_id, 10)
    get_top_name_list = Actors.name_list(get_actors_names)
    return get_top_name_list

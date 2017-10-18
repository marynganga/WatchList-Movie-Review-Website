from app import app 
import urllib.request,json
from models import movie
Movie = movie.Movie

# Getting api key
api_key = app.config['MOVIE_API_KEY']

# Getting the movie base url
base_url = app.config['MOVIE_API_KEY_BASE_URL']

def get_movies(category):
	'''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)
from Project2_Flask import main_functions
import requests


def request_key():
    apiDict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_keys.json")
    return apiDict['key']

def request_word(word):
    url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query="+word+"&api-key="+request_key()
    response = requests.get(url).json()
    return response

def request_reviewers(reviewer):
    url2 = "https://api.nytimes.com/svc/movies/v2/critics/"+reviewer+".json?api-key="+request_key()
    response2 = requests.get(url2).json()
    return response2

def request_picks(picks):
    url3 = "https://api.nytimes.com/svc/movies/v2/reviews/"+picks+".json?api-key="+request_key()
    response3 = requests.get(url3).json()
    return response3
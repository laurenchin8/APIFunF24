import requests # a lib for making http requests
import json # a lib for qorking with json

url = "https://itunes.apple.com/search?media=movie&entity=movie&term=Thor"

# iTunes documentation
# media: type of media to search for (ie: movie)
# entity: type of results you want for media specified (ie: movie (for movie title))
# attribute: attribute you want to search for in the stores (ie: movieTerm)
# term: URL-encoded text string you want to search for
# country: default is US
response = requests.get(url=url)

# first thing, check the response's status_code
print(response.status_code)
if response.status_code == 200:
    # status OK
    # we can extract the prediction from the response's JSON text
    json_object = json.loads(response.text)
    # get list of movies
    movies = json_object["results"]
    # iterate through each movie in the results
    for movie in movies:
        movie_name = movie["trackName"] # Movie name
        duration_in_seconds = movie["trackTimeMillis"] / 1000  # Duration in seconds
        
        # convert duration to hours, minutes, and seconds
        hours = int(duration_in_seconds / 3600)
        min = int((duration_in_seconds % 3600) / 60)
        sec = int(duration_in_seconds % 60)
        
        # print movie name and duration
        print("Movie:", movie_name)
        print(f"Duration: {hours} hours, {min} minutes, {sec} seconds")
        print("\n")
else:
    print(f"Error: Unable to fetch data (status code {response.status_code})")
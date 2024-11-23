import requests # a lib for making http requests
import json # a lib for qorking with json

url = "https://itunes.apple.com/search?media=movie&entity=movie&attribute=movieTerm&term=Thor"

# iTunes documentation
# media: type of media to search for (ie: movie)
# entity: type of results you want for media specified (ie: movie (for movie title))
# attribute + term: attribute you want to search for
response = requests.get(url=url)

# first thing, check the response's status_code
print(response.status_code)
if response.status_code == 200:
    # status OK
    # we can extract the prediction from the response's JSON text
    json_object = json.loads(response.text)
    print(json_object)
    # prediction = json_object["prediction"]
    # print("prediction:", prediction)
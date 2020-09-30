#print ("This is Brian Pitts Challenge 2")

import json
import requests

url = "https://api.chucknorris.io/jokes/random"

results = requests.get(url).json()
print(results["value"])
#print(json.dumps(results, indent=2, sort_keys=True, default=str))


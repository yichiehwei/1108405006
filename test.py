import requests
import json

url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/
"

payload  = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

data = json.loads(response.text)

print(data)

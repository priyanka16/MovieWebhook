import requests
url = 'https://api.mlab.com/api/1/databases/movies_info/collections/movie?q={%27vote_average%27:%20{%27$gt%27:%208}}&apiKey=fjncPgZ9bcpr20VRml5x50zKVDV1IDa2'
print (requests.__version__)
response = requests.get(url, headers={"Content-Type": "application/json", "Accept": "*", "Access-Control-Allow-Origin" :"true", "Upgrade-Insecure-Requests":"1"})
print(response.json())

import requests

url = 'http://127.0.0.1:5000/'

params = {'keyword' : 'football'}

r = requests.post(url = url, params = params)

thing = r.text

print(thing)
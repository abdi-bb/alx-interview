#!/usr/bin/python3
'''
Star War API
'''

import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python script.py <Movie_ID>")
    sys.exit(1)

movie_id = sys.argv[1]

url = f"https://swapi.dev/api/films/{movie_id}/"

response = requests.get(url)

if response.status_code != 200:
    print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
    sys.exit(1)

movie_data = response.json()
characters = movie_data['characters']

for character_url in characters:
    character_response = requests.get(character_url)
    character_data = character_response.json()
    print(character_data['name'])

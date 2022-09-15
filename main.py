import json
import requests
website ='https://v3.football.api-sports.io/'

URL = ('https://v3.football.api-sports.io/countries?''name=spain')

header = {
    'x-rapidapi-host':"v3.football.api-sports.io",
    'x-rapidapi-key': "API_KEY"
}

# Api_key = "API_KEY"
# print(f"Your API key is {Api_key}")

# response = requests.request("GET" , URL , headers = header).json()
# print(json.dumps(response , indent=4))

#leagues

# league_url = website + "leagues?" + "name=premier league"
# print(league_url)
# response = requests.request("GET" , league_url, headers = header).json()
# print(json.dumps(response , indent = 4))

#rounds
# fixture_url = website + "fixtures/rounds?" +'season=2019&''league=39&''current=FALSE'
# print(fixture_url)
# response = requests.request("GET" , fixture_url, headers = header).json()
# print(json.dumps(response , indent = 4))

def url(website):
    response = requests.request("GET" , website , headers = header).json()
    json_data = (json.dumps(response))
    with open("top.json" , "w") as outfile:
        outfile.write(json_data)
    
# url('https://v3.football.api-sports.io/teams?'
#      'name=manchester united')

#url('https://v3.football.api-sports.io/teams/statistics?season=2019&team=33&league=39')

# url('https://v3.football.api-sports.io/teams?''search=india')
#url('https://v3.football.api-sports.io/teams?search=manchester')
#url('https://v3.football.api-sports.io/players?team=33&search=ronaldo')

url('https://v3.football.api-sports.io/players/topscorers?season=2021&league=61')
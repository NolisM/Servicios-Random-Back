import requests


apiKeyYelp = '7n1lWjsAK14D-G4vGbgDiroATN8iTfsltWsjnc9m1HzymqYUox4ynLd2fY6U6YPNGXG4ZA7FSs69t7xmxwUZRsc47_DxRUPlk3BUHyxDiimnXnoZYQ72KMgXHht-ZnYx'
apiYelpUrl = 'https://api.yelp.com/v3/events/awesome-event'
headersYelp = {
    'accept': 'application/json',
    'authorization': f'Bearer {apiKeyYelp}',
}

response_yelp = requests.get(apiYelpUrl, headers=headersYelp)
print("Yelp status code:", response_yelp.status_code)
print("Yelp response:", response_yelp.json())


apiUrl = 'https://api.foursquare.com/v3/places/search'
apiKeyFoursquare = 'fsq3buQ3sQjU/VUhFJxh7dVe8/1AMnf65GT0l4vUU+iWqFg='
headersFoursquare = {
    'accept': 'application/json',
    'Authorization': f'Bearer {apiKeyFoursquare}',
}

params = {
    'll': '-31.4167,-64.1833',
    'radius': 100000,
    'v': '20220101',
}

response_foursquare = requests.get(apiUrl, headers=headersFoursquare, params=params)
print("Foursquare status code:", response_foursquare.status_code)
print("Foursquare response:", response_foursquare.json())

#Handels API calls
import requests
from config import API_key

#Make city_name into latitudes and longitudes
def get_coordinates(city):
   url1 = (f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_key}')
   response1 = requests.get(url1)
   try:
    if response1.status_code == 200:
     data = response1.json()
     if data:
      return data[0]['lat'], data[0]['lon']
     return None, None
    else:
     print("The city is invalid . Data not found.")
   except Exception as e:
     print("Error occured", e)

#Takes weather through latitude and longitude
def get_weather(lat, lon):
  url2 = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric')
  try:
    response2 = requests.get(url2)
    if response2.status_code == 200:
      return response2.json()
    else:
      return None
    
  except Exception as e:
      print("Error occured:", e)


import requests
import tkinter as tk
from tkinter import Toplevel, Label
API_key = '1718e920bbe90fb4153d19901ad8097e'
def next_window(lat, lon):
    url2 = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metrics')
    try:
     response2 = requests.get(url2)
     if response2.status_code == 200:
      weather_data = response2.json()
      next_window = Toplevel()
      next_window.title("weather result")
      next_window.geometry("300x200")
      city = weather_data['name']
      temp = weather_data['main']['temp']
      kl = 273
      conversion = temp - kl
      description = weather_data['weather'][0]['description']
      Label(next_window, text= f"city: {city}").grid(pady= 5)
      Label(next_window, text= f"temprature: {conversion}").grid(pady= 5)
      Label(next_window, text= f"description: {description}").grid(pady= 5)
   
     else:
      print("No data found")
    except Exception as e:
      print("Error occured:", e)

def get_weather():
   city_name = search_var.get()
   if not city_name:
      print("Enter a city name")
      return

   url1 = (f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_key}')
   response1 = requests.get(url1)
   if response1.status_code == 200:
    data = response1.json()
   if data:
    lat = data[0]['lat']
    lon = data[0]['lon']
    next_window(lat,lon)
   else:
    print("The city is invalid . Data not found.")


root = tk.Tk()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm ,text= "Weather", background= "white").grid(column= 0, row= 0)
search_var = tk.StringVar()
search_entry = tk.Entry(frm, textvariable= search_var, width= 50)
search_entry.grid(pady=10)
search_button = tk.Button(frm, text= "Search city", command =get_weather)
search_button.grid()
root.mainloop()
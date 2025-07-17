#MAKE GUI
import tkinter as tk
from tkinter import Toplevel, Label
from BACKEND import get_coordinates, get_weather

#Makes a pop up window to show result
def show_weather(city , temprature, description):
     next_window = Toplevel()
     next_window.title("weather result")
     next_window.geometry("300x200")

     Label(next_window, text= f"city: {city}").grid(pady= 5)
     Label(next_window, text= f"temprature: {temprature}").grid(pady= 5)
     Label(next_window, text= f"description: {description}").grid(pady= 5)

#makes first window to search the city
def run_app():
     root = tk.Tk()
     frm = tk.Frame(root)
     frm.grid()
     tk.Label(frm ,text= "Weather", background= "white").grid(column= 0, row= 0)
     search_var = tk.StringVar()
     entry = tk.Entry(frm, textvariable= search_var, width= 50)
     entry.grid(pady=10)
     
     # present data from backend
     def search_weather():
      city = search_var.get()
      if not city:
            print("Please enter a city name")
            return
      lat,lon = get_coordinates(city)
      if lat and lon:
            data = get_weather(lat, lon)
            if data:
             temp_kelvin = data['main']['temp']
            show_weather(data['name'], f"{temp_kelvin}°C", data['weather'][0]['description'])
      else:
       print("Weather data not found.")
           

     tk.Button(frm, text= "Search city", command = search_weather).grid()
     root.mainloop()
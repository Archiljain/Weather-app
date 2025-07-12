import requests
import tkinter as tk
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
   else:
    print("The city is invalid . Data not found.")
   
   def get_weather():
     city_name =search_var.get()
     if city_name == "":
       result_label.config(text= "please enter the city name")
       return
   url2 = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metrics')
   response2 = requests.get(url2)
   if response2.status_code == 200:
     weather_data = response2.json()
     if weather_data:
      temp = weather_data['main']['temp']
      unit = 273
      conversion = temp - unit 
      desc = weather_data['weather'][0]['description']
      result_label.config(text= f"{conversion}°C, {desc}")
   else:
     print("No data found")

root = tk.Tk()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm ,text= "Weather", background= "white").grid(column= 0, row= 0)
search_var = tk.StringVar()
search_entry = tk.Entry(frm, textvariable= search_var, width= 50)
search_entry.grid(pady=10)
search_button = tk.Button(frm, text= "Search city", command =get_weather,)
search_button.grid()
result_label = tk.Label(frm, text="", background= "white", font= ("arial", 12))
result_label.grid(columnspan= 2, row= 4, pady=10)
API_key = '1718e920bbe90fb4153d19901ad8097e'
root.mainloop()
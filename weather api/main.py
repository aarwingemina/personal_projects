#BUILD GUI
import tkinter as tk
import requests


def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit


window = tk.Tk()
window.title("Weather App")
window.geometry("400x400")

city_entry = tk.Entry(window, font = ("Arial", 12))
city_entry.pack(pady = 10)
user_input = city_entry.get()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e44467089842cdc80dc55275cf1de2e2"
CITY = user_input

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
curr_temp_k = response["main"]["temp"]
curr_temp = kelvin_to_fahrenheit(curr_temp_k)

display_curr_temp = tk.Label(window, text = f"Current temperature: {curr_temp:.2f}", font = ("Arial", 14))
display_curr_temp.pack(pady = 20)

window.mainloop()


"""

import tkinter as tk

window = tk.Tk()
window.title("Weather App")
window.geometry("400x400")

city_entry = tk.Entry(window, font = ("Arial", 12))
city_entry.pack(pady = 10)

output_label = tk.Label(window, text ="", font = ("Arial", 12))
output_label.pack(pady = 5)

def show_input():
    user_input = city_entry.get()
    output_label.config(text = f"you ented: {user_input}")

button = tk.Button(window, text = "Enter", command = show_input())
button.pack(pady = 10)

window.mainloop()
"""

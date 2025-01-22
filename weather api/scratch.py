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
    

button = tk.Button(window, text = "Enter", command = show_input)
button.pack(pady = 10)


window.mainloop()


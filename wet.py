import json
import requests
from tkinter import *
from PIL import ImageTk, Image

# Initialize the main window
root = Tk()
root.geometry("400x400")
root.title("Weather App")
root.configure(bg='#f2f2f2')

# Load and display the icon image
img = ImageTk.PhotoImage(Image.open('um.png'))
panel = Label(root, image=img, bg='#f2f2f2')
panel.place(x=150, y=10)

# Title Label
title_label = Label(root, text="Weather App", width=20, bg='#f2f2f2', font=("bold", 20), fg='brown')
title_label.place(x=60, y=100)

# City Entry Field
city_names = StringVar()
entry_1 = Entry(root, textvariable=city_names, width=25, font=("Arial", 12))
city_names.set("Enter City Here ...")
entry_1.place(x=100, y=150)

# Labels for Weather Info
temp_label = Label(root, text="Temperature (°C):", width=20, bg='#f2f2f2', font=("Arial", 10), fg='blue')
temp_label.place(x=50, y=230)
pressure_label = Label(root, text="Pressure (mb):", width=20, bg='#f2f2f2', font=("Arial", 10), fg='blue')
pressure_label.place(x=50, y=260)
description_label = Label(root, text="Description:", width=20, bg='#f2f2f2', font=("Arial", 10), fg='blue')
description_label.place(x=50, y=290)

# Dynamic Labels to Display Results
lable_temp = Label(root, text="...", width=10, bg='#f2f2f2', font=("Arial", 10), fg='blue')
lable_temp.place(x=220, y=230)
lable_pres = Label(root, text="...", width=10, bg='#f2f2f2', font=("Arial", 10), fg='blue')
lable_pres.place(x=220, y=260)
lable_desc = Label(root, text="...", width=20, bg='#f2f2f2', font=("Arial", 10), fg='blue')
lable_desc.place(x=220, y=290)

# Function to Fetch Weather Details
def getTemp():
    api_key = "af416a596912802e0930122d1c7507c4"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_1.get().strip()  # Trim whitespace
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    # Fetching Data from the API
    response = requests.get(complete_url)
    x = response.json()

    # Check if 'cod' key in response indicates success
    if x.get("cod") == 200:
        y = x["main"]
        current_temperature = round(y["temp"] - 273.15, 2)  # Convert Kelvin to Celsius
        current_pressure = y["pressure"]
        weather_description = x["weather"][0]["description"].capitalize()

        # Update Labels with Data
        lable_temp.configure(text=f"{current_temperature} °C")
        lable_pres.configure(text=f"{current_pressure} mb")
        lable_desc.configure(text=weather_description)
    else:
        # If the city is not found or other error occurs
        lable_temp.configure(text="N/A")
        lable_pres.configure(text="N/A")
        lable_desc.configure(text="City Not Found")

# Submit Button
submit_btn = Button(root, text="Submit", width=12, bg='brown', fg='white', font=("Arial", 10), command=getTemp)
submit_btn.place(x=160, y=190)

# Instruction Label
instruction_label = Label(root, text="Temperature in Celsius and Pressure in mb", width=40, bg='#f2f2f2', font=("Arial", 9), fg='brown')
instruction_label.place(x=60, y=340)

# Run the Application
mainloop()

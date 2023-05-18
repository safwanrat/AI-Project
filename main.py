'''
119 Safwan Rahman, 105 Sarvesh Chandrakumar, 131 Olivier Vannier

This program uses the Chat GPT API to function as a travel advisor app with features such as obtaining the weather, recommending hotels, and checking the price of food within a city.
'''



import tkinter as tk
from tkinter import messagebox
import openai
import requests

openai.api_key = 'MY_API_KEY'

def chat_with_gpt(message):
    # return GPT's response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=None
    )
    reply = response.choices[0].text.strip()
    return reply

def get_weather(city):
    # get weather data from api and send it
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openai.api_key}'
    response = requests.get(url)
    data = response.json()
    weather = data['weather'][0]['description']
    return weather

def recommend_hotel(city):
    return f"Hotel {city} is a great hotel! 5 stars"

def get_food_price(city):
    return "The average price of food in the city is $25 per meal."

def send_message():
    user_input = entry.get().strip()

    if user_input.lower() == 'exit':
        window.destroy()
    else:
        response = chat_with_gpt(user_input)

        if 'weather' in user_input:
            city = user_input.split('weather')[1].strip()
            try:
                weather = get_weather(city)
                messagebox.showinfo("Response", f"The weather in {city} is {weather}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        elif 'hotel' in user_input:
            city = user_input.split('hotel')[1].strip()
            hotel = recommend_hotel(city)
            messagebox.showinfo("Response", hotel)

        elif 'food price' in user_input:
            city = user_input.split('food price')[1].strip()
            food_price = get_food_price(city)
            messagebox.showinfo("Response", food_price)

        else:
            messagebox.showinfo("Response", response)

# create window, add the widgets, and start the application
window = tk.Tk()
window.title("ChatGPT Travel Advisor")

label = tk.Label(window, text="Welcome to the GPT Travel Advisor!")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

button = tk.Button(window, text="Send", command=send_message)
button.pack()

window.mainloop()

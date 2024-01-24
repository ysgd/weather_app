import requests
import json
import pyttsx3

text_speech = pyttsx3.init()

city = input('enter name of the city: ')

url = f"https://api.weatherapi.com/v1/current.json?key=6bf90bc786dc479f9d585223242301&q={city}"

r = requests.get(url)
weather_dict = json.loads(r.text)
text_speech_inp = input("What do you want to know?: '1. temperature in celsius'/ '2. temperature in fahrenheit'/ '3. condition'/ '4. wind mph'/ '5. wind kph'").lower()
temp_cel = weather_dict["current"]["temp_c"]
temp_f = weather_dict['current']['temp_f']
if text_speech_inp == '1':
  text_speech.say(f"The current temperature at {city} in celsius is {temp_cel}")
  text_speech.runAndWait()
elif text_speech == '2':
    text_speech_inp.say(f"The current temperature at {city} in fahrenheit is {temp_f}")

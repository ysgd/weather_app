import requests
import json
import pyttsx3

text_speech = pyttsx3.init()

print("Welcome to Weather App")
print("enter name of the city below and select options. To exit the app just type 'exit'")
while True:
  city = input('enter name of the city: ')
  if city.lower() == 'exit':
    break
  url = f"https://api.weatherapi.com/v1/current.json?key=6bf90bc786dc479f9d585223242301&q={city}"

  r = requests.get(url)
  weather_dict = json.loads(r.text)
  text_speech_inp = input("What do you want to know?: '1. temperature   in celsius'/ '2. temperature in fahrenheit'/ '3. time'/ '4.   latitude'/ '5. longitude': ").lower()
  temp_cel = weather_dict["current"]["temp_c"]
  temp_f = weather_dict['current']['temp_f']
  time = weather_dict['location']['localtime']
  lat = weather_dict['location']['lat']
  long = weather_dict['location']['lon']
  if text_speech_inp == '1':
    print(f"Current temperature at {city} in celsius: {temp_cel}")
    text_speech.say(f"The current temperature at {city} in celsius is   {temp_cel}")
    text_speech.runAndWait()
  elif text_speech_inp == '2':
    print(f"Current temperature at {city} in fahrenheit: {temp_f}")
    text_speech.say(f"The current temperature at {city} in fahrenheit   is {temp_f}")
    text_speech.runAndWait()
  elif text_speech_inp == '3':
    print(f"Current local time at {city} is {time}")
    text_speech.say(f"Current local time at {city} is {time}")
    text_speech.runAndWait()
  elif text_speech_inp == '4':
    print(f"Latitude of {city} : {lat}")
    text_speech.say(f"Latitude of {city} is {lat}")
    text_speech.runAndWait()
  elif text_speech_inp == '5':
    print(f"Longitude of {city} : {long}")
    text_speech.say(f"Longitude of {city} is {long}")
    text_speech.runAndWait()
  else:
    print("incorrect selection")
  


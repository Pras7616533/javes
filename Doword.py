import datetime
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyjokes
import random
import wikipedia
import pywhatkit
import pyautogui
import requests
import json

def sptext():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
  recognizer.adjust_for_ambient_noise(source)
  audio = recognizer.listen(source)
  try:
    print("Recognizing...")
    data = recognizer.recognize_google(audio)
    print("You said: " + data)
    return data
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
    print("Google Speech Recognition service; {0}".format(e))
    return "" 
      
def speak(text):
  engine = pyttsx3.init()
  voice = engine.getProperty('voices')
  engine.setProperty('voice', voice[0].id)
  rate = 200
  engine.setProperty('rate',rate)
  engine.say(text)
  engine.runAndWait()

def wishme():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning!")
  elif hour>=12 and hour<18:
    speak("Good Afternoon!")
  else:
    speak("Good Evening!")
  speak("I am Jarvis. How may I help you?")

def sendEmail(to, content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login('pd7616533@gmail.com', 'prash555@')
  server.sendmail('tugrp@example.com', to, content)
  server.close()

def joke():
  speak(pyjokes.get_joke(language="en", category="all"))

def ram():
  exit = False
  user_points = 0
  computer_points = 0

  while exit == False:
      options = ["rock", "paper" , "scissors"]
      user_input = input("Choose rock, paper, scissors or exit: ")
      computer_input = random.choice(options)

      if user_input == "exit" :
          print("Game ended")
          print("You won a total score of "+str(user_points))
          print("the computer total score is " +str(computer_points))
          exit = True

      if user_input == "rock":
          if computer_input == "rock":
              print("Your input is rock")
              print("computer input is rock")
              print("It is a tie!")
          elif computer_input == "paper":
              print("Your input is rock")
              print("computer input is paper")
              print(" computer wins")
              computer_points += 1
          elif computer_input == "scissors":
              print("Your input is rock")
              print("computer input is scissors")
              print("you win")
              user_points += 1

      elif user_input == "paper":
          if computer_input == "rock":
              print("Your input is paper")
              print("computer input is rock")
              print("you win!")
              user_points += 1
          elif computer_input == "paper":
              print("Your input is paper")
              print("computer input is paper")
              print("it's a tie!")
          elif computer_input == "scissors":
              print("Your input is paper")
              print("computer input is scissors")
              print("computer wins")
              computer_points += 1

      elif user_input == "scissors":
          if computer_input == "rock":
              print("Your input is scissors")
              print("computer input is rock")
              print("computer win!")
              computer_points += 1
          elif computer_input == "paper":
              print("Your input is scissors")
              print("computer input is paper")
              print("you win")
              user_points += 1
          elif computer_input == "scissors":
              print("Your input is scissors")
              print("computer input is scissors")
              print("its a tie")

      elif user_input != " rock" or user_input != "paper" or user_input != "scissors":
          print("Invalid Input")


def wiki():
  speak("Searching Wikipedia...")
  query = sptext()
  results = wikipedia.summary(query, sentences=2)
  speak("According to Wikipedia")
  print(results)
  speak(results)

def youtube():
  speak("What do you want to search on Youtube?")
  query = sptext()
  url = ("https://www.youtube.com/results?search_query="+query)
  webbrowser.open(url)

def google():
  speak("What do you want to search on Google?")
  query = sptext()
  url = ("https://www.google.com/search?q="+query)
  webbrowser.open(url)

def play():
  speak("What song do you want to play?")
  song = sptext()
  pywhatkit.playonyt(song)

def screenshot():
  img = pyautogui.screenshot()
  img.save("C:\\Users\\Admin\\Desktop\\screenshot.png")

def weather():
  api_key = "your-api-key"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  speak("What is the city name?")
  city_name = sptext()
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  response = requests.get(complete_url)
  x = response.json()
  if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    speak(" Temperature in kelvin unit is " + str(current_temperature) +
          "\n humidity in percentage is " + str(current_humidiy) +
          "\n description  " + str(weather_description))
  else:
    speak(" City Not Found ")

def run():
 while True:
    data = sptext().lower()
    if 'wikipedia' in data:
      wiki()
    elif 'youtube' in data:
      youtube()
    elif 'google' in data:
      google()
    elif 'play' in data:
      play()
    elif 'screenshot' in data:
      screenshot()
    elif 'weather' in data:
      weather()
    elif 'joke' in data:
      joke()
    elif 'ram' in data:
      ram()
    elif 'exit' in data:
      speak("Exiting...")
      break
    else:
      speak("Please say that again")




if __name__ == "__main__":
  wishme()
  while True:
    data = sptext().lower()
    if sptext().lower() == "javes":
      if 'open youtube' in data:
        webbrowser.open("youtube.com")
      elif 'open google' in data:
        webbrowser.open("google.com")
      elif 'open stackoverflow' in data:
        webbrowser.open("stackoverflow.com")
      elif 'the time' in data:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
      
      elif 'email' in data:
        try:
          speak("What should trying to say?")
          content = sptext()
          to = "tugrp@example.com"
          sendEmail(to, content)
          speak("Email has been sent!")
        except Exception as e:
          print(e)
          speak("Sorry my friend, I am not able to send this email")
      elif 'quit' in data:
        speak("Thanks for using me")
        exit()
      else:
        run()
    else:
      speak("Sorry, I am not able to do that")

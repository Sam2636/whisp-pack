import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125) 
engine.say("I will speak this text")
"""VOICE"""
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
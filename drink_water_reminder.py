## Exercise 11 - Drink Water Reminder
# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

# macOS
# import os
# import time

# REPEAT_INTERVAL = 10  # repeat frequency in second

# while True:
#     command = "sleep 2; osascript -e \'say \"Hey Pranav Drink Water!\"\'; osascript -e \'display alert \"Hey Pranav Drink Water\"\'"
#     os.system(command)
#     time.sleep(REPEAT_INTERVAL)
    
    
# Window
import time
import ctypes
import pyttsx3

REPEAT_INTERVAL = 3600  # seconds 1 hr = 60 min = 60*60 sec = 3600 second

engine = pyttsx3.init()

while True:
    # Speak the message
    engine.say("Hey Pranav Drink Water!")
    engine.runAndWait()

    # Show popup alert
    ctypes.windll.user32.MessageBoxW(0, "Hey Pranav Drink Water!", "Reminder", 1)

    time.sleep(REPEAT_INTERVAL)


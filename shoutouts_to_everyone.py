# from os import system

# names = ["raj", "ram", "jay", "shiv"]

# for name in names:
#     system(f"say Shoutouts to {name}")


import pyttsx3

names = ["raj", "ram", "jay", "shiv"]

engine = pyttsx3.init()

for name in names:
    engine.say(f"Shoutouts to {name}")
    engine.runAndWait()


# cd F:\Python\CWH_Python\Python_Day88
# python shoutouts_to_everyone.py

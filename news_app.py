# Exercise 10
# Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
# Go to: https://newsapi.org/
# and explore the various options to build you application


import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-08&sortBy=publishedAt&apiKey=dbe52d33805c4445b196e6f5c5c4ab00"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print("Title : ",article["title"])
    print("Description : ",article["description"])
    print("---------------------------------------------------------------------")
    
    
    
    
    
    
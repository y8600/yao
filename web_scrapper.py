import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
bs = BeautifulSoup(response.text,"lxml")
print(bs.find("p").text)

#write the output to a file
with open("output.txt","w") as file:
    file.write(bs.find("p").text)

file.close()
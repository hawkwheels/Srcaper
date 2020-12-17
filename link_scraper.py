# Importing
from bs4 import BeautifulSoup
import requests 

# replace testurl.com with the url you want to use.
# requests.get downloads the webpage and stores it as a variable
html = requests.get('http://yourtargetsite/index.html') 

# this parses the webpage into something that beautifulsoup can read over
soup = BeautifulSoup(html.text, "lxml")
# lxml is just the parser for reading the html 

# this is the line that grabs all the links # stores all the links in the links variable
links = soup.find_all('a') 
#print (links)
for link in links:      
    # prints each link which has the atrribute 'href' 
    if "href" in (link.attrs): 
      print(link.attrs["href"])
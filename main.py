import requests
from bs4 import BeautifulSoup

#Opens local file ("html"), "r" for read, variable html_file
with open("home.html", "r") as html_file:
    # Reads html
    content = html_file.read()
    
    # Uses lxml parser on content
    soup = BeautifulSoup(content, "lxml")

    # Gets first tag with h5 in it then stops
    tags = soup.find("h5")
    # Gets all tags with h5 in it then stops
    tags = soup.find_all("h5")
    print(tags)

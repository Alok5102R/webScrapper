import requests
from bs4 import BeautifulSoup

req = requests.get("https://ioflood.com/blog/python-activate-venv/")

soup = BeautifulSoup(req.content, "html.parser")

# print(soup) # Raw website page

# print(soup.prettify()) # Organized website page

# print(soup.get_text()) # Website text content

# print(soup.title.prettify()) # Website perticular attribute (ex: <title>)

print(soup.title.get_text()) # Website perticular attribute's text content (ex: <title>)


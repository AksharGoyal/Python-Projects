# importing the necessary modules
import requests
from bs4 import BeautifulSoup as bs 

# get the github username
github_user = input('Input Github Username: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')

# get the pic
repo = soup.find('img', {'alt' : 'Avatar'})['src']
print(repo)
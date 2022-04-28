# importing the necessary modules
import requests
from bs4 import BeautifulSoup as bs 

# get the github username
github_user = input('Input Github Username: ')
url = 'https://github.com/' + github_user # create the link
r = requests.get(url) # get the content of the link
soup = bs(r.content, 'html.parser') # get the content in html format

try:
    # if everything works out great, we will get the link of the profile picture
    repo = soup.find('img', {'alt' : 'Avatar'})['src']
except:
    print('Invalid User! Showing you pic of someone handsome instead!')
    r = requests.get('https://github.com/AksharGoyal')
    soup = bs(r.content, 'html.parser')
    repo = soup.find('img', {'alt' : 'Avatar'})['src']
# get the pic

print(f"Click on the link to view the profile pic: {repo}")

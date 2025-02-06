import requests
from bs4 import BeautifulSoup

# Function to scrape a webpage and check for a specific button
def check_button_in_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        return False
    
    soup = BeautifulSoup(response.text, 'html.parser')
    button = soup.find( string="Je dépose mon dossier")
    
    return button is not None



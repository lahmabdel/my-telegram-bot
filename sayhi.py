import requests
from bs4 import BeautifulSoup
import time
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Fetch environment variables from Render dashboard
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def check_button_in_page(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            logging.error("Failed to fetch page: %s", url)
            return False
        
        soup = BeautifulSoup(response.text, 'html.parser')
        button = soup.find( string="Je dépose mon dossier")
        
        return button is not None
    except Exception as e:
        logging.error("Error while scraping: %s", str(e))
        return False
    


# Function to send a message
def send_telegram_message(nada=0):
    url_to_check = "https://www.arpej.fr/fr/residence/nicolas-appert-residence-etudiante-ivry-sur-seine/"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    if check_button_in_page(url_to_check):
        message = f"a jrrrrrrrrrriiii There is a logement available: {url_to_check}"
        payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
            }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                logging.info("Message sent successfully")
            else:
                logging.error("Failed to send message: %s", response.text)
        except Exception as e:
            logging.error("Error sending message: %s", str(e))
    elif nada:
        message = f"still running yazbi 3yit"
    else:
        return 0
    

    payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message
        }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logging.info("Message sent successfully")
        else:
            logging.error("Failed to send message: %s", response.text)
    except Exception as e:
        logging.error("Error sending message: %s", str(e))


start_time = time.time()
if __name__ == "__main__":
    while True:
        send_telegram_message()
        
        current_time = time.time()
        if current_time - start_time > 1800:
            send_telegram_message(1)
            start_time = current_time  # Reset the timer
        time.sleep(600)  # Wait 30 minutes before running again

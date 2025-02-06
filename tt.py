import requests

# Telegram bot token
TOKEN = ""

def get_chat_id():
    """Fetch updates and print the chat ID of the last message sender."""
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url).json()

    try:
        chat_id = response["result"][-1]["message"]["chat"]["id"]
        print(f"Your Chat ID: {chat_id}")
        return chat_id
    except (KeyError, IndexError):
        print("No messages found. Send a message to your bot and try again.")

if __name__ == "__main__":
    get_chat_id()

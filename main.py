from flask import Flask, request, Response
import requests

# Telegram bot token
TOKEN = ""

app = Flask(__name__)

# Function to extract chat_id and text from the message
def tel_parse_message(message):
    try:
        chat_id = message['message']['chat']['id']
        print(chat_id)
        text = message['message']['text']
        return chat_id, text
    except:
        return None, None

# Function to send a response message
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

@app.route('/', methods=['POST'])
def index():
    msg = request.get_json()
    chat_id, text = tel_parse_message(msg)

    if chat_id and text and text.lower() == "hi":
        tel_send_message(chat_id, "Hi world")

    return Response('ok', status=200)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

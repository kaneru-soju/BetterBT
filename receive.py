from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import config
from twilio.rest import Client
from pyngrok import ngrok

from MapScraper import MapScraper

app = Flask(__name__)
client = Client(config.account_SID, config.auth_token)


@app.route('/bot', methods=['POST'])
def bot():
    user = request.values.get('From', '')
    resp = MessagingResponse()

    print(f"Got a message from: {user}")

    message = request.form["Body"]

    print(message)

    scraper = MapScraper()
    scraper.schedule_query(message, client, user)

    print("Message was: " + request.form["Body"])

    return str(resp)


def start_ngrok():
    url = ngrok.connect(5000).public_url
    print('*Tunnel URL:', url)

    incoming_list = client.incoming_phone_numbers.list(phone_number=config.phone_number)
    print(f"Length of list: {len(incoming_list)}")
    for number in incoming_list:
        number.update(sms_url=url + "/bot")
        print(f"Number: {number.phone_number}")


if __name__ == '__main__':
    start_ngrok()
    app.run(debug=True)

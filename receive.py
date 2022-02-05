from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    print(number + ", " + message_body)
    resp.message('Hello {}, you said: {}'.format(number, message_body))


if __name__ == "__main__":
    app.run(debug=True)

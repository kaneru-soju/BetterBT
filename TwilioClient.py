
import twilio
from twilio.rest import TwilioRestClient
import config
from config import *

class TwilioClient():
    def __init__(self):
        self.client = TwilioRestClient(config.account_SID, config.auth_token)

    def send_message(number, msg):
        self.client.messages.create(from_=config.phone_number,
                               to=number,
                               body=msg)
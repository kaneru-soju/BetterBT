
import twilio
from twilio.rest import TwilioRestClient
import config
from config import *

class TwilioClient():
    def __init__(self):
        self.client = TwilioRestClient(config.account_SID, config.auth_token)

    def send_text(self, to_number, from_number):
        client.messages.create(to="+15404437433")
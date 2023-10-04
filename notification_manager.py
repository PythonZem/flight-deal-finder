from twilio.rest import Client


class NotificationManager:
    def __init__(self, KEY: str, TOKEN: str, text_sms: str):
        self.account_sid = KEY
        self.auth_token = TOKEN
        self.text_sms = text_sms
        self.send_sms()

    def send_sms(self):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            to='+380503962864',
            body=self.text_sms
        )

    pass
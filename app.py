"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
import os
import sys
import logging

app = Flask(__name__)
if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

ACCESS_TOKEN = "EAAB79k2TrWEBALuTJICA6v6nFI2tWGLhU58HH9fMK0RZCF4pS1LhwZCEXS1CbrGHi3M1fy0W7K3YobFS9ZBDN4X3W1rUv1wX6szMTVVyPrdOuya0DQWpyZB5PQNqALQT3Kqr6p2z5CGiIa0dGFl3DgOR4J2Ftr23T8sYh02L2VfcAKpJd7aI"
VERIFY_TOKEN = "english"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(debug=True)

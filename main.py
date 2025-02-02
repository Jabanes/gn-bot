from flask import Flask
import schedule
import time
from twilio.rest import Client
from dotenv import load_dotenv
import os
from threading import Thread

# Load environment variables from .env file
load_dotenv()

# Set up Flask app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bot is running'

# Twilio API setup
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
RECIPIENT_NUMBER = os.getenv('RECIPIENT_NUMBER')

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_good_night():
    message = client.messages.create(
        body="Good night!",
        from_=TWILIO_WHATSAPP_NUMBER,
        to=RECIPIENT_NUMBER
    )
    print(f"Message sent: {message.sid}")

# Schedule the message at 10:00 PM every day
schedule.every().day.at("22:00").do(send_good_night)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    # Start the background task in a separate thread
    thread = Thread(target=run_schedule)
    thread.start()

    # Run Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)

from twilio.rest import Client
import schedule
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twilio credentials from environment variables
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER")

# Function to send message
def send_good_night():
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=RECIPIENT_NUMBER,
        body="Erez says: Good night! 😴✨❤️"
    )
    print(f"Message sent: {message.sid}")


# Schedule it to run every night at 10:00 PM
schedule.every().day.at("22:00").do(send_good_night)

print("Bot is running... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again

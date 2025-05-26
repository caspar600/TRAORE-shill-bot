import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE_NUMBER")

client = TelegramClient('session_name', API_ID, API_HASH)

async def main():
    await client.send_message('me', '🚀 TRAORE shill bot is live!')

with client:
    client.loop.run_until_complete(main())
Add main.py

import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond("TRAORE Shill Bot is now online and running!")

async def main():
    print("Bot is up and running...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())

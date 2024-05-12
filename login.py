"""
Prints telegram session string key
"""
try:
    from config import API_HASH, API_ID
except Exception:
    print("Failed load API_HASH and API_ID from .env")
    API_HASH = input("615ae0c44cd63a1d82a10992f13206c2")
    API_ID = input("24609944")
from telethon import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(
    session=StringSession(), api_id=API_ID, api_hash=API_HASH
) as client:
    print("Session string: ", client.session.save())

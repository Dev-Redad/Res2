# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "25771966")
API_HASH = os.getenv("API_HASH", "33039415ffad9db7056892ed652ac1d0")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7730081012:AAFZ0Y16OwmHK02vLKTG_uVgXhppAEkj8nc")
MONGO_URI = os.getenv("MONGO_DB", "mongodb+srv://Sinchu:Sinchu@sinchu.qwijj.mongodb.net/?retryWrites=true&w=majority&appName=Sinchu")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "6418117720").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002565738939")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002535991950")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "5"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "5000"))

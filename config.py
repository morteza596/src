# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "66102"))
API_HASH = getenv("API_HASH", "b6da542ebc418c1f282d372152d40664")
BOT_TOKEN = getenv("BOT_TOKEN", "7179303938:AAGwNkCqj8pBVpM-H8rkTLWYULxjVAxgmco")
OWNER_ID = list(map(int, getenv("OWNER_ID", "579247196").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002233950303")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002233950303"))

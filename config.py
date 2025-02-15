from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", 21857983)
if API_ID is not None:
    API_ID = int(API_ID)
else:
    raise ValueError("API_ID environment variable is not set or invalid")

API_HASH = getenv("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")

BOT_TOKEN = getenv("BOT_TOKEN", "7621093704:AAE8sMZFjuZzMPuJtL-jk7Bq14AW6UJ5SXU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", 6893672657))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION","BQCr238AxK8u4TNQMXCWCINCPdausckaAtVI1M7O29k824HBk9iyOBf3g37SrB95AYMaHav6P7aLy_T9lboFOD-EbuHPhBoXIvqwjjqXioQdFgY8_FhxvjVfT8lyqxZPwJfuTfh8gJRLVLGFCtZQ4mHGmsBJo4FtTNd-hDTSEmxehbCdIy_K4f7NRFlpPsfqgCsq4PeexvuQ9vvjIsg3DdVIQnlgq6iNrp-KeaiRVXOlQusNH3TZLq763YTWoK3x0YnrJlBf5JvXkecLKOdim5ISRfIj6Wt85oj2eunbGAPfzy7xOhLoesfE5MBsfBESx1MS-pQl5Yp9eFU9QGg80s1iRX67EAAAAAFA0UrVAA")
#SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/alphonzMusic")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/alpha_botnetwork")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "833465134").split()))

FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

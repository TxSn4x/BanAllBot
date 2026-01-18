import os
class Config:
    API_ID="26657288"
    API_HASH="00536e431477dbb16583d5b85813aa72"
    TOKEN="8322614110:AAH3BjISKBM1YGHoUdJpeSy4oNp7Skvb4UI"
    SUDO = list(int(i) for i in os.environ.get("SUDO", "8158464263").split(" "))
    START_IMG="https://graph.org/file/6d30f418db49172de15dc-7abbc00b7db69788f9.jpg"
    BOT_ID=8322614110
    BOT_USERNAME="BanAllRbot"
    BOT_NAME="banall"

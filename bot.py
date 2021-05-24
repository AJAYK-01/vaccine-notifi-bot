import time
import subprocess
import requests
import os

botId = os.environ.get('botId')
# https://t.me/chatIDrobot
chatId = os.environ.get('chatId')
agelimit = os.environ.get('ageLimit')
district = os.environ.get('districtId')


def run_job():
    print("Checking for slots in " + district)
    op = subprocess.check_output(
        f'python3 vaccine.py {district} {agelimit}', shell=True)
    message = str(op.decode("utf-8"))
    # print(message)
    if op:
        try:
            requests.get("https://api.telegram.org/bot"+botId+"/" +
                         "sendMessage?chat_id="+chatId+"&"+"text="+message)
        except Exception as e:
            print(str(e))


while True:
    run_job()
    time.sleep(60)

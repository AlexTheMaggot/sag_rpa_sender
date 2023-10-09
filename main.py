import time
import requests
import os
from config import *
import datetime
import traceback


file_path = DIRECTORY + os.listdir(DIRECTORY)[-1]

while True:
    try:
        r = requests.post(
            f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument?chat_id={CHAT_ID}',
            files={'document': open(file_path, 'rb')}
        )
        if r.status_code == 200:
            with open('log.txt', 'a') as log:
                log.write(f'[{datetime.datetime.now()}] - Succesful sending file\n')
                break
        else:
            with open('log.txt', 'a') as log:
                log.write(f'[{datetime.datetime.now()}] - Telegram Error ({r.json()["description"]})\n')
                break
    except requests.exceptions.ConnectionError:
        with open('log.txt', 'a') as log:
            log.write(f'[{datetime.datetime.now()}] - Connection Error\n')
            time.sleep(10)
    except:
        with open('log.txt', 'a') as log:
            backslash = '\n'
            try:
                log.write(f'[{datetime.datetime.now()}] - Other Error ({traceback.format_exc().split(backslash)[-2]})\n')
            except:
                log.write(f'[{datetime.datetime.now()}] - Other Error (No detailed information)\n')
            break

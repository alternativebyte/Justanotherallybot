import string
import requests
from random import randint, choice
import time
import threading
import os
import sys
import aiohttp

from dotenv import load_dotenv
load_dotenv()

# config
cookie = os.getenv('COOKIE')
group = os.getenv('GROUP')
allies = os.getenv('TYPE')
delay = os.getenv('DELAY')
threads = os.getenv('THREADS')
type = os.getenv('TYPE')

if cookie == "":
    print("Please set .roblosecurity cookie in .env file (COOKIE)")
    sys.exit(0)
if group == "":
    print("Please set the Group ID in .env file (GROUP)")
    sys.exit(0)
if delay == None:
    print("Delay not set, defaulting to 5 seconds.")
    delay = 5
if threads == None:
    print("Threads not set, defaulting to 1 thread")
    threads = 1
if type not in ['allies', 'enemies']:
    print("Type not set or invalid, defaulting to allies.")
    type = "allies"

def groupally():
    while True:
        try:
            random = randint(15000000, 16010000)
            cookies = {'.ROBLOSECURITY': cookie}

            gathtoken = requests.post(
                'https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            headers = {'x-csrf-token': token}

            sendally = requests.post(
                f'https://groups.roblox.com/v1/groups/{group}/relationships/{allies}/{random}', headers=headers, cookies=cookies)

            if sendally.status_code == 200:
                print(f'Ally sent to {random} | ')
            elif sendally.status_code == 429:
                print('Rate limited')
                time.sleep(5)
            else:
                print(f'Failed to send {allies} request to {random}')
        except:
            print(f'Error')
        time.sleep(int(delay))

def main():
    print("Forked off of https://github.com/BananaJeanss/roblox-ally-bot-outdev")
    print("Working as of 05/01/2025")
    time.sleep(0.5)
    print("Starting in 1 second.")
    time.sleep(1)
    for i in range(int(threads)):
        t = threading.Thread(target=groupally)
        t.start()

if __name__ == "__main__":
    main()

import time
import pyautogui

import random
import datetime
import requests
import json
import os
import PIL as p
import numpy as n


def crop():
    image = pyautogui.screenshot()
    print(image)
    image = n.asarray(image)
    print(type(image), image.shape)


def click_btn(btnname):
    btnlocation = pyautogui.locateOnScreen(btnname, confidence=0.9)
    pyautogui.moveTo(btnlocation)
    pyautogui.leftClick()

def click_last_btn(btnname):
    *_, last = pyautogui.locateAllOnScreen(btnname, confidence=0.9)
    pyautogui.moveTo(last)
    pyautogui.leftClick()


def perform_actions():
    click_btn('local.png')
    time.sleep(1.5)
    pyautogui.moveTo(36, 108)
    pyautogui.leftClick()
    time.sleep(1)
    click_btn('message_declan.png')

if __name__ == '__main__':
    limit = int(input("Quanti link vuoi pubblicare? "))
    if limit > 10:
        limit = 10
    print(f'Pubblico {limit} link')
    shutdown = input("Vuoi spegnere il pc alla fine? (y/n) ")
    time.sleep(2)
    i = 0
    url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=30"
    time.sleep(5)

    # cwd = os.getcwd()
    # button7location = pyautogui.locateOnScreen('nft.png', confidence=0.9)
    # local_btn = os.path.join(cwd, "nft.png")

    publish_time = datetime.datetime.now() + datetime.timedelta(seconds=15)
    time_string = publish_time.strftime("%H:%M:%S")
    while i < limit:
        print(f'Entro nel ciclo {i} - Ora sono le {datetime.datetime.now()} ({publish_time})')
        time.sleep(2)
        while True:
            actual_time = datetime.datetime.now().strftime("%H:%M:%S")
            if actual_time == time_string:
                response = requests.request("GET", url)
                data = json.loads(response.content)
                permalink_list = []

                for d in data['assets']:
                    permalink_list.append(d['permalink'])

                choosen_one = random.choice(permalink_list)
                minutes = random.randrange(30, 35, 1)
                seconds = random.randrange(0, 59, 1)

                # milliseconds = random.randrange(0, 999, 1)
                # microseconds = random.randrange(0, 999, 1)

                waiting_time = datetime.timedelta(minutes=minutes, seconds=seconds)
                publish_time += waiting_time
                time_string = publish_time.strftime("%H:%M:%S")
                perform_actions()
                pyautogui.write(choosen_one, interval=0.01)
                pyautogui.press('enter')
                time.sleep(2)
                click_last_btn('publish.png')
                print(f'{choosen_one} \n\n Pubblicato alle: {actual_time} \n\n Prossimo alle {time_string} ')
                time.sleep(1)
                click_btn('fufuncity.png')
                i += 1
                break

    if shutdown == 'n':
        exit()
    else:
        os.system("shutdown /s /t 1")

# web_hook = 'https://discordapp.com/api/webhooks/896848295895379999/6ZooX1oJOPFrLXTsVDTXhzX25226Glz3Tkxvd9r8H5g3Gv3uj-QaakRiYW35US4xpr7U'

# r = requests.post(web_hook, data=json.dumps(values), headers={'Content-type': 'application/json'})

# i = 0
#
# for link in permalink_list:
#     time.sleep(5)
#     values = {
#         'username': f'Wapto_000{str(i)}',
#         'content': permalink_list[i]
#     }
#     r = requests.post(web_hook, data=json.dumps(values), headers={'Content-type': 'application/json'})
#     i += 1

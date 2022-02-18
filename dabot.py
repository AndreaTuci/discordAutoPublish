import logging
import time
import pyautogui

import random
import datetime
import requests
import json
import os
import PIL as p
import numpy as n
import win32gui
import win32con
import sys

# Opzioni per il logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# Classe che contiene i valori per accendere / spegnere il monitor

class Mode():
    STAND_BY = 1
    TURN_ON = -1
    TURN_OFF = 2

SC_MONITORPOWER = 0xF170


def start_up():
    print('Funzione start_up')
    os.startfile(r"C:\Users\User\AppData\Local\Discord\app-1.0.9003\\Discord.exe")
    time.sleep(10)
    opening_message = True
    while True:
        if pyautogui.locateOnScreen('fufuncity.png', confidence=0.9):
            click_btn('fufuncity.png')
            break
        else:
            if opening_message:
                print('Sto aprendo Discord...')
                opening_message = False
        time.sleep(1)

    time.sleep(1)
    click_btn('markeplace.png')
    time.sleep(2)


def click_btn(btnname):
    print('click_btn', btnname)
    clicked = False
    message = True
    while True:
        if pyautogui.locateOnScreen(btnname, confidence=0.9):
            if clicked == False:
                btnlocation = pyautogui.locateOnScreen(btnname, confidence=0.9)
                pyautogui.moveTo(btnlocation)
                pyautogui.leftClick()
                clicked = True
                # print('click')
                # print('ora esco dal ciclo')
                time.sleep(3)
                break
        else:
            if message:
                print('In attesa...')
                message = False
        time.sleep(1)
    # print('ora esco dalla funzione')

def click_last_btn(btnname):
    print('click_last_btn', btnname)
    clicked = False
    message = True
    while True:
        if pyautogui.locateOnScreen(btnname, confidence=0.9):
            if clicked == False:
                *_, last = pyautogui.locateAllOnScreen(btnname, confidence=0.9)
                pyautogui.moveTo(last)
                pyautogui.leftClick()
                clicked = True
                # print('click')
                # print('ora esco dal ciclo')
                time.sleep(1)
                break
        else:
            if message:
                print('In attesa...')
                message = False
        time.sleep(1)
    # print('ora esco dalla funzione')


def perform_actions():
    # print('Funzione perform_actions_1')
    click_btn('local.png')
    time.sleep(3)
    # print('Funzione perform_actions_2')
    click_btn('daclan_note.png')
    time.sleep(3)
    # print('Funzione perform_actions_3')
    click_btn('message_declan.png')
    # print('fine actions')


if __name__ == '__main__':

    try:
        limit = int(input("Quanti link vuoi pubblicare? "))
        if limit > 10:
            limit = 10
        print(f'Pubblico {limit} link')
        shutdown = input("Vuoi spegnere il pc alla fine? (y/n) ")
        start_up()
        i = 0
        url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=30"
        publish_time = datetime.datetime.now() + datetime.timedelta(seconds=15)
        time_string = publish_time.strftime("%H:%M:%S")
        while i < limit:
            print(f'Link {i+1}/{limit} - Sono le {datetime.datetime.now()}, pubblico alle {publish_time}')
            time.sleep(2)
            while True:
                actual_time = datetime.datetime.now().strftime("%H:%M:%S")
                if actual_time == time_string:
                    pyautogui.press('esc')
                    time.sleep(5)
                    response = requests.request("GET", url)
                    data = json.loads(response.content)
                    permalink_list = []

                    for d in data['assets']:
                        permalink_list.append(d['permalink'])

                    choosen_one = random.choice(permalink_list)
                    minutes = random.randrange(30, 35, 1)
                    seconds = random.randrange(0, 59, 1)
                    waiting_time = datetime.timedelta(minutes=minutes, seconds=seconds)
                    publish_time += waiting_time
                    time_string = publish_time.strftime("%H:%M:%S")
                    perform_actions()
                    # print('ora scrivo')
                    pyautogui.write(choosen_one, interval=0.01)
                    pyautogui.press('enter')
                    time.sleep(5)
                    click_last_btn('publish.png')
                    print(f'{choosen_one} \n\n Pubblicato alle: {actual_time} \n\n')
                    time.sleep(5)
                    click_btn('fufuncity.png')
                    time.sleep(2)
                    i += 1
                    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER,
                                         Mode.TURN_OFF)
                    break

        if shutdown == 'y':
            os.system("shutdown /s /t 1")
        else:
            sys.exit()

    except Exception as e:
        logger.error(e)
        with open('log.txt', 'w') as f:
            error = logger.error(e)
            for line in error:
                f.write(line)

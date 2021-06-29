import codecs
import pyautogui
import time
import pywinauto.keyboard as pwak
import os
import re


list_dir = os.listdir('директория/с/текстами/в/.txt')
for el in list_dir:
    if not re.match(r'.+\.txt', el):
        list_dir.remove(el)

pyautogui.PAUSE = 0.02

def main(list):
    for i in range(len(list)):
        print(f'{i}. {list[i]}')

    file_number = input('Номер текста: ')
    file_number = int(file_number)
    f = codecs.open(f'D:/Python/requests/{list[file_number]}')
    t = f.read()
    time.sleep(2)
    for i in range(len(t)):
        el = t[i]
        if el == ' ':
            pyautogui.press('space')
        else:
            pwak.send_keys(f'{el}')


main(list_dir)

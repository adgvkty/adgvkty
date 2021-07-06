import codecs
import pyautogui
import time
import pywinauto.keyboard as pwak
import os
import re

# путь к папке с .txt файлами
path_to_txt = ''

# получаением список всех файлов в директории
list_dir = os.listdir(path_to_txt)

# циклом перебираем все названия файлов
for el in list_dir:
    
    # если в названии нет .txt - удаляем название из списка
    if not re.match(r'.+\.txt', el):
        list_dir.remove(el)

pyautogui.PAUSE = 0.03

def main(list):
    
    # циклом выводим все оставшиеся названия
    for i in range(len(list)):
        print(f'{i}. {list[i]}')

    # просим юзера ввести нужный нам номер текста
    file_number = input('Номер текста: ')
    
    # переводим номер из str() в int()
    file_number = int(file_number)
    
    # открываем и читаем файл
    f = codecs.open(os.path.join(path_to_txt, list[file_number]))
    t = f.read()
    time.sleep(2)
    
    # циклом печатаем все символы
    for i in range(len(t)):
        el = t[i]
        if el == ' ':
            pyautogui.press('space')
        else:
            pwak.send_keys(f'{el}')


main(list_dir)

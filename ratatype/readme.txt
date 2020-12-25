# понадобиться скачать codecs, pyautowin и pyautogui

# Также естественно надо что бы скрипт и txtшки были в одной папке

import codecs 
import pyautogui
import time
import pywinauto.keyboard as pwak


txt = ['Reef', 'Bear', 'Brazil', 'Niggers', 'Cave', 'Sol'] # список с именами файлов
text = [] # пустой список для букв


def main():

    global text

    print(f'Выберите текст: \n '
          f'1. {txt[0]} \n '
          f'2. {txt[1]} \n '
          f'3. {txt[2]} \n '
          f'4. {txt[3]} \n '
          f'5. {txt[4]} \n '
          f'6. {txt[5]}')
    file_number = input('Номер текста: ')
    file_number = int(file_number)
    f = codecs.open(f'{txt[file_number - 1]}.txt', encoding="utf-8")
    
    тут используется кодек утф-8 по одной простой причине - питон почти не умеет в кириллицу
    а битовое поле вместо символов как бы не читабельно
    
    file_number - 1 -- это гениальный способ найти индекс текста в списке, потому что по print у Reef номер 1, а по txt - 0
    
    t = f.read()
    time.sleep(2)
    
    это время ожидания между тем, как текст готов к использованию и началом непосредственно ввода
    сюда можно добавить авто переключение на нужное окно, но кому оно надо?
    
    for i in range(len(t)): # t - это наш прочитанный текст
        el = t[i]           # el присваиваем iтый элемент из t
        if el == ' ':       # если пробел
            pyautogui.press('space') # то мы пользуемся pyautogui
        else:
            pwak.send_keys(f'{el}') # в любом ином случае просто печатаем абсолютно любой символ


main()

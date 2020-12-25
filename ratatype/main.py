import codecs
import pyautogui
import time
import pywinauto.keyboard as pwak


txt = ['Reef', 'Bear', 'Brazil', 'Niggers', 'Cave', 'Sol']
text = []


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
    t = f.read()
    time.sleep(2)
    for i in range(len(t)):
        el = t[i]
        if el == ' ':
            pyautogui.press('space')
        else:
            pwak.send_keys(f'{el}')


main()

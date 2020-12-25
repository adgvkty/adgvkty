from tkinter import *
from decimal import *            #float не работает
from math import *               #для cos, sin и пр.

root = Tk()                              #главное окно
root.title('Калькулятор')                #название проекта
root.resizable(False, False)             #запрет на изменение размера окна

buttons = ( ('M', 'm-', 'm+', 'mc'),
            ('Sqrt', 'X^2', 'Sin', 'Cos'),
            ('7', '8', '9', '/'),         #"кортеж" для
            ('4', '5', '6', '*'),         #обозначение кнопок
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
          )

activeStr = ''   #хранение набираемого числа
stack = []       #числа и операции которые надо совершить
memory = 0       #перменная памяти
wdth = 6         #переменная ширины кнопок

def calculate():                                #логика калькулятора

    global stack
    global label
    global memory

    result = 0
    
    operand2 = Decimal(stack.pop())             #поочередное "вынимание" из стопки
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
            if operand1 == 0 or operand2 == 0:  #запрещает делить на 0
                result = 'Nice Try'     
            else:
                result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2

    if operation == 'Sqrt':                     #"одночисельные" операции
        result = sqrt(operand1)
    if operation == 'X^2':
        result = operand1 ** 2
    if operation == 'Sin':
        result = sin(operand1)
    if operation == 'Cos':
        result = cos(operand1)
    if operation == 'M':
        memory = operand1
        result = 'Memorized'                    #текст гласящий о том, что сохранилось
    if operation == 'm-':
        if operand1 == 0:
            result = 'Memory is empty'          #текст в случае, если попытались отнять у пустой памяти
        else:
            result = memory - operand1
    if operation == 'm+':
        result = memory + operand1

    label.configure(text=str(result))           #отображение результата
    activeStr = str(result)

def click(text):                                #обработка нажатий клавиши

    global activeStr
    global stack
    global memory

    if text == 'CE':                            #в качестве аргумента - текст с кнопки
        stack.clear()                  
        activeStr = ''
        label.configure(text='0')
    elif text == 'mc':                          #чистка памяти
        memory = 0
        stack.clear(0)
        activeStr = ''
        label.configure(text='sector clear')
    elif text == 'Del':
        if len(activeStr) == 1:                 #del - просто удаляет последний символ из строки
            label.configure(text='0')           #если попытаться удалить один символ, 
        else:                                   #то будет отображаться 0
            activeStr = activeStr[:-1]
            label.configure(text=activeStr)
    elif '0' <= text <= '9':
        activeStr += text             
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:           #если в строке нет точки, то она становится
            activeStr += text                   #во всех других случаях - ничего
            label.configure(text=activeStr)
    elif text in ('Sqrt', 'X^2', 'Cos', 'Sin', 'M', 'm+', 'm-', 'mc'): #список "одночисельных операций"
        if len(stack) != 1:                                            #эта проверка нужна на случай
            stack.append(label['text'])                                #если пользователь проводит операцию
            stack.append(text)                                         #без ввода, собственно, числа
            stack.append(0)                                         
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
        else:
            stack.clear()
            activeStr = ''
            label.configure(text='Error')
    else:
        if len(stack) >= 2:                     #заставляет проводить операцию         
            stack.append(label['text'])         #если юзер пытается впихнуть третье чисто
            calculate()                         #или просто проводит операцию, если text == '='
            stack.clear()       
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text='0')

label = Label(root,                                             #поле ввода
              text = '0',
              font = ("Times New Roman", 15, "bold"),
              bg = "#f6f8f9",
              foreground = "#455660",
              width = 14) 

label.grid(row=1,                                               #и его конфиг. в сетке
           column = 0,
           columnspan = 2,
           sticky = "nsew")          

button = Button(root,                                           #кнопка CE (отдельно чтобы быть в row c label)
                text = 'CE',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#F30000",
                command = lambda text = 'CE': click(text))      #command'у присваивается функция
                                                                #которая обрабатывает нажатие
button.grid(row = 1,
            column = 3)                                         

button = Button(root,                                           #del отдельно по той же причине что и CE
                text = 'Del',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#F30000",
                command = lambda text = 'Del': click(text))     #lambda нужна чтобы не писать отдельные функции
                                                                #для каждой кнопки, а сразу их передавать
button.grid(row = 1,
            column = 2)

for row in range(6):                                            #с помощью цикла строится сетка кнопок
    for col in range(4):
        button = Button(root,
                        width = wdth,
                        font = ("Times New Roman", 15, "bold"),
                        bg = "#e5ebee",
                        foreground = '#215b7a',
                        text=buttons[row][col],
                        command = lambda row = row,
                                         col = col: click(buttons[row][col]))
                    
        button.grid(row = row + 2,
                    column = col,
                    sticky = "nsew")                                    
       
root.grid_rowconfigure(3, weight = 1)       #прочие настройки сетки
root.grid_columnconfigure(3, weight = 1)

root.mainloop()                             #"главный цикл обработки событий"

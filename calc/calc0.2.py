from tkinter import *
from decimal import *

#почему decimal? пробовал с float - получилось не получилось

root = Tk()
root.title('calc')

buttons = (('7', '8', '9', '/'), #"кортеж" для
           ('4', '5', '6', '*'), #обозначение кнопок
           ('1', '2', '3', '-'),
           ('0', '.', '=', '+')
           )

activeStr = '' #хранение набираемого числа
stack = [] #числа и операции которые надо совершить

def calculate(): #логика калькулятора

    global stack #объявляем стак и
    global label #название глобальными

    result = 0 #присваиваем результату 0 на всякий случай
    operand2 = Decimal(stack.pop()) #методом pop получаем строки из списка
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        if operand1 == 0 or operand2 == 0: #долго думал как красиво запретить
            result = 'хорошая попытка'     #нет ничего красивее обычного if-else
        else:
            result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2

    label.configure(text=str(result)) #отображение результата в label в виде str

def click(text): #обработка нажатий клавиши

    global activeStr
    global stack

    if text == 'CE': #в качестве аргумента - текст на кнопке
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:             #операция будет проделана
            stack.append(label['text']) #если уже введены 2 числа
            calculate()                 #но юзер вводит третье
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

wdth=5
label = Label(root, text='0', font=("Times New Roman", 15, "bold"), bg="#6D94E3", foreground="#FFF", width=20)
label.grid(row=0, column=0, columnspan=3, sticky="nsew")

button = Button(root, text='CE', width=wdth, font=("Times New Roman", 15, "bold"), bg="#DFDDDD",
                                    foreground="#F30000", command=lambda text='CE': click(text))

button.grid(row=0, column=3, sticky="nsew") #кнопки располагаются с помощью грида
for row in range(4):
    for col in range(4):
        button = Button(root, width=wdth, font=("Times New Roman", 15, "bold"), bg="#DFDDDD", text=buttons[row][col],
                                 command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")
        #у каждой кнопки своя функция lambda,
        #потому что иначе оно не работало
        
root.grid_rowconfigure(6, weight=100)
root.grid_columnconfigure(4, weight=100)
root.resizable(False, False)

root.mainloop()

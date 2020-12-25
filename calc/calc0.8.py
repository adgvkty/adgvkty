from tkinter import *
from decimal import *            #float не работает
from math import *               #для cos, sin и пр.

root = Tk()                              #главное окно
root.title('Калькулятор')                #название проекта
root.resizable(False, False)             #запрет на изменение размера окна

buttons = ( ('Sqrt', 'X^2', 'Sin', 'Cos'),
            ('7', '8', '9', '/'),         #"кортеж" для
            ('4', '5', '6', '*'),         #обозначение кнопок
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
           )

activeStr = ''   #хранение набираемого числа
stack = []       #числа и операции которые надо совершить
memory = 0       #использовалась в попытке имплементировать память
wdth = 6         #переменная ширины кнопок

def calculate():                                #логика калькулятора

    global stack
    global label

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
                result = 'хорошая попытка'     
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
        memory = 0
    elif '0' <= text <= '9':
        activeStr += text             
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:           #всё гениальное - просто
            activeStr += text
            label.configure(text=activeStr)
    elif text in ('Sqrt', 'X^2', 'Cos', 'Sin'): #всё гениальное - просто 2x
        stack.append(label['text'])
        stack.append(text)
        stack.append(0)
        calculate()
        stack.clear()
        stack.append(label['text'])
        activeStr = ''
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

label = Label(root, text='0', font=("Times New Roman", 15, "bold"), bg="#f6f8f9", foreground="#455660", width=14) #поле ввода
label.grid(row=0, column=0, columnspan=2, sticky="nsew")                                                          #его конфурация в сетке

button = Button(root, text='CE', width=wdth, font=("Times New Roman", 15, "bold"), bg="#e5ebee",
                                    foreground="#F30000", command=lambda text='CE': click(text))
button.grid(row=0, column=3)                                                                                      #конфигурация CE в сетке

button = Button(root, text='<-', width=wdth, font=("Times New Roman", 15, "bold"), bg ="#e5ebee",
                                   foreground="#F30000", command=lambda text='<-': click(text))

button.grid(row=0, column=2)

for row in range(5):
    for col in range(4):
        button = Button(root, width = wdth, font=("Times New Roman", 15, "bold"), bg="#e5ebee", foreground = '#215b7a', text=buttons[row][col],
                                                                                     command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")                                                       #без lambda отказывалось работать
       
root.grid_rowconfigure(3, weight=1)         #остальные настройки сетки
root.grid_columnconfigure(3, weight=1)

root.mainloop()                             #"главный цикл обработки событий"

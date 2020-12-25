from tkinter import *
from decimal import *            
from math import *               

root = Tk()                     #главное окно проекта            
root.title('Калькулятор')       #название    
root.resizable(False, False)    #запрет на изменение размеров окна

buttons = ( ('M', 'm-', 'm+', 'mc'),        #кортеж для кнопок
            ('Sqrt', 'X^2', 'Sin', 'Cos'),
            ('7', '8', '9', '/'),       
            ('4', '5', '6', '*'),        
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
          )

activeStr = ''  #хранение набираемого числа
stack = []      #введенные числа и операции
memory = 0      #память
wdth = 6        #ширина кнопок (тестовая)
deg = 0
stackNS = ['2x', '4x', '8x', '16']
temp_str = ''
temp_label = ''
     
def calculate():              #логика калькулятора              

    global stack
    global label
    global memory

    result = 0
    
    operand2 = Decimal(stack.pop())             #поочередное вынимание из стопки
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
            if operand1 == 0 or operand2 == 0: 
                result = 'Error'                #запрет деления на 0
            else:
                result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    if operation == 'Sqrt':                   
        result = sqrt(operand1)
    if operation == 'X^2':
        result = operand1 ** 2
    if operation in ('Sin', 'Cos'):
        if deg == 1:
            operand1 = radians(operand1)
        if operation == 'Sin':
            result = sin(operand1)
        else:
            result = cos(operand1)
    if operation == 'M':
        if operand1 == 0:
            result = 'Error'
        else:
            memory = operand1
            result = 'Memorized'                #подтверждение сохранения
    if operation == 'm-':
        if memory == 0:
            result = 'Error'                    #ошибка пустой памяти
        else:
            result = memory - operand1
    if operation == 'm+':
        result = memory + operand1

    result = str(result)

    if result.isalpha():
        label.configure(text=result,
                        font = ("Times New Roman", 15, "bold"))
    else:
        result = Decimal(result)
        if len(str(result)) > 7:
            if result >= 1.0000E+30:
                label.configure(text='Num too large',
                            font = ("Times New Roman", 15, "bold"))
            elif result >= 1.0000E+6:
                result = '{:1E}'.format(result)
                label.configure(text = result,
                            font = ("Times New Roman", 9))
            else:
                result = str(result)
                if result.find('.') == 1:
                    if result.count('0') >= 4:
                        result = result[:10]
                        label.configure(text = result,
                                        font = ("Times New Roman", 9))
                    else:
                        result = result[:5]
                        label.configure(text = result,
                                        font = ("Times New Roman", 15, "bold"))
                else:
                    result = result[:5]
                    label.configure(text = result,
                                        font = ("Times New Roman", 15, "bold"))
        else:
            result = str(result)
            label.configure(text = result,
                            font = ("Times New Roman", 15, "bold"))
    
    activeStr = str(result)
 
    
def click(text):    #обработка нажатий клавиш, аргументом выступает текст

    global activeStr
    global stack
    global memory
    global deg

    if text == 'CE':       
        stack.clear()                  
        activeStr = ''
        label.configure(text='0',
                        font = ("Times New Roman", 15, "bold"))             #возврат шрифта на нормальный
    elif text == 'mc':                                                      
        memory = 0
        label.configure(text='Memory is empty')                             #текст ошибки памяти
    elif text == 'Del':
        if label['text'].isalpha():
            activeStr = ''                                              
            label.configure(text='0',
                            font = ("Times New Roman", 15, "bold"))
        if len(label['text']) == 1 or Decimal(label['text']) >= 1.000000e+6: #проверка на случай больших чисел
            activeStr = ''                                                   #или посл. цифры в строке
            label.configure(text='0',
                            font = ("Times New Roman", 15, "bold"))
        elif len(stack) == 1:                                               #проверка на случай оставшихся
            activeStr = str(stack.pop())                                    #в стаке чисел после calculate()
            activeStr = activeStr[:-1]
            label.configure(text=activeStr)
        else:                                                               #в этом else почти все операции
            activeStr = activeStr[:-1]
            label.configure(text=activeStr)
    elif '0' <= text <= '9':
            if activeStr == '0':
                activeStr = ''
                label.configure(text='0')
            else:
                activeStr += text             
                label.configure(text=activeStr)
    elif text in ('NS', 'DG/RD'):
        if text == 'NS':
            temp_str = label2['text']
            temp_str = temp_str[:2]
            stack.append(temp_str)
            temp_str = stack.pop()
            label.configure(text=temp_str)
        else:
            stack.clear()
            activeStr = ''
            label.configure(text = '0',
                            font = ("Times New Roman", 15, "bold"))
            if deg == 0:
                deg = 1
                label2.configure(text='10/DEG')
            else:
                deg = 0
                label2.configure(text='10/RAD')
    elif text == '.':                                                       #поиск точки в строке
        if activeStr.find('.') == -1:                                       #если не нашлась - поставиться
            activeStr += text                   
            label.configure(text=activeStr)
    elif text in ('Sqrt', 'X^2', 'Cos', 'Sin', 'M', 'm+', 'm-', 'mc'):                               
        if activeStr.isalpha():                                             #проверка на наличие букв
            label.configure(text='Error')
        else:
            stack.append(label['text'])
            stack.append(text)                                         
            stack.append(0)                                         
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
    else:                                      
        if len(stack) >= 2:                                                 #тут все остальные операции                  
            stack.append(label['text'])         
            calculate()                         
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

label1 = Label(root,
              text = '',
              font = ("Times New Roman", 15, "bold"),
              bg = "#f6f8f9",                        
              foreground = "#455660")                            

label1.grid(row=0,                                    
           column = 0,
           columnspan = 1,
           sticky = "nsew")

label2 = Label(root,
              text = '10/RAD',
              font = ("Times New Roman", 15, "bold"),
              bg = "#f6f8f9",                        
              foreground = "#455660",)                            

label2.grid(row=0,                                    
           column = 1,
           columnspan = 1,
           sticky = "nsew")

button = Button(root,                               
                text = 'DG/RD',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#215b7a",
                command = lambda text = 'DG/RD': click(text))
                                                                
button.grid(row = 0,
            column = 3)                                         

button = Button(root,                                            
                text = 'NS',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#215b7a",
                command = lambda text = 'NS': click(text))     
                                                                
button.grid(row = 0,
            column = 2)
                
label = Label(root,                                                         #основное поле
              text = '0',                             
              font = ("Times New Roman", 15, "bold"),
              bg = "#f6f8f9",                        
              foreground = "#455660",                
              width = 14)                            

label.grid(row=1,                                    
           column = 0,
           columnspan = 2,
           sticky = "nsew")                                                 #растягивание label и кнопок                        

button = Button(root,                               
                text = 'CE',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#F30000",
                command = lambda text = 'CE': click(text))
                                                                
button.grid(row = 1,
            column = 3)                                         

button = Button(root,                                            
                text = 'Del',
                width = wdth,
                font = ("Times New Roman", 15, "bold"),
                bg = "#e5ebee",
                foreground = "#F30000",
                command = lambda text = 'Del': click(text))     
                                                                
button.grid(row = 1,
            column = 2)

for row in range(6):                                            
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
       
root.grid_rowconfigure(4, weight = 1)    #прочие настройки сетки   
root.grid_columnconfigure(5, weight = 1) 

root.mainloop()                          #главный цикл обработки событий                       

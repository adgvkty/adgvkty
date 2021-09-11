from PIL import Image, ImageDraw
import sys

# Временно хранит в себе данные одного корабля
# Перед append в ships
ship = []

# Хранит массив всех кораблей 
ships = []

# Счетчик для распределения аргументов по массивам
i = 0

# Отрезаем из массива аргументов "picture.py"
# Делаем из оставшейся строки массив из строк сплитом
arguments = sys.argv[1:][0].split(" ")

# Итерируем по каждой строке
for arg in arguments:
    
    # Если счетчик равен 4, значит это последний аргумент определенного корабля
    # Мы аппендаем последний аргумент в массив корабля
    # И потом аппендим весь корабль в массив кораблей
    # Затем очищащем временные переменные и идём по новой
    if i == 4:
        if arg == "False":
            ship.append(False)
        else:
            ship.append(True)
        ships.append(ship)
        ship = []
        i = 0
        continue
    
    # Если длина < 3, значит это число, а не тип
    if len(arg) <= 3:
        ship.append(int(arg))
    else:
        ship.append(arg)
    i = i + 1

# Накладывает спрайт на изображение
def paste_image(image_bg, image_element, cx, cy, w, h, rotate=0, h_flip=False, v_flip=False):
    
    # Созданием копии обоих изображений
    image_bg_copy = image_bg.copy()
    image_element_copy = image_element.copy()

    # Ресайзим спрайт в соответствии с аргументами
    image_element_copy = image_element_copy.resize(size=(w, h))
    
    # Зеркалим изображение если надо
    if h_flip:
        image_element_copy = image_element_copy.transpose(Image.FLIP_LEFT_RIGHT)
    if v_flip:
        image_element_copy = image_element_copy.transpose(Image.FLIP_TOP_BOTTOM)
    
    # Ротейтим в соответствии с аргументами
    image_element_copy = image_element_copy.rotate(rotate, expand=True)
    
    # Получаем альфа канал спрайта
    _, _, _, alpha = image_element_copy.split()

    # На случай ротейта, если после него поменялись высота/широта
    w = image_element_copy.width
    h = image_element_copy.height
    x0 = cx - w // 2
    y0 = cy - h // 2
    x1 = x0 + w
    y1 = y0 + h

    # Вставляем изображение с маской, тем самым делая его сексуально прозрачным
    image_bg_copy.paste(image_element_copy, box=(x0, y0, x1, y1), mask=alpha)
    return image_bg_copy
    
def main(ships):
    
    # Считаем сколько линий нам надо
    linesAmount = len(ships) * 10
    
    # Открываем фон
    p = Image.open("pictures/sea.jpg")
    
    # Считаем размер клетки
    cell_size = int(p.size[0] / linesAmount)
    
    draw = ImageDraw.Draw(p)

    # Рисуем две линии, которые не нарисуются циклом
    draw.line((0, 999, 1000, 999))
    draw.line((999, 0, 999, 1000))

    # Циклами рисуем все остальные линии
    for i in range(linesAmount):
        draw.line((p.size[0]/linesAmount*i, 0, p.size[0]/linesAmount*i, 1000))
        
    for i in range(linesAmount):
        draw.line((0, p.size[1]/linesAmount*i, 1000, p.size[0]/linesAmount*i))
    
    # Рисуем циклом все корабли
    for ship in ships:
        
        # Распаковываем тупле
        shipType, x, y, r, flip = ship
        
        # Подгружаем спрайт (вероятно придется из переменной это делать)
        sprite = Image.open(f"pictures/{shipType}.png")

        # Считаем координаты для рисовки радиуса атаки
        leftUpPoint = (x-r, y-r)
        rightDownPoint = (x+r, y+r)
        coords = [leftUpPoint, rightDownPoint]
        draw.ellipse(coords)
        
        # Накладываем функцией спрайт на изображение
        p = paste_image(p, sprite, x, y, cell_size, cell_size, 0, flip)
        
        # Переприсваваем рисовалку на новое изображение
        draw = ImageDraw.Draw(p)

    # Сохраняем че получилось
    p.save("empty.png", "PNG")
    
main(ships)




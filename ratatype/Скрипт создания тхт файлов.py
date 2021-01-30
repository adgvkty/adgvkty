import requests
import re

n = 500

for i in range(n):
    response = requests.get('https://www.ratatype.com/ru/typing-test/test/ru/')
    response.encoding = 'utf-8'
    response = re.findall(r'<div class="mainTxt">.+', response.text)[0]
    response = response.replace('<div class="mainTxt">', '')
    response = response.replace('</div>', '')

    title = re.findall(r'\w+', response)[0]

    file = open(f'{title}.txt', 'w')
    file.write(response)
    file.close()
    print(f'{i}/{n}')


from re import A


s = "Hello"
s1 = s.encode("utf-8")
print(s1)
#s2 = s1.decode("utf-8")
#print(s2)
###################################################

f = open('text.txt', mode='r')
#print(f)
#print(f.read())
#for line in f:
#   print(line)
###################################################

f = open('text.txt', mode='w')
text = input("Enter your text: ")
f.write(text)
f.close()
###################################################

#открытие файлов с помощью констекстного менеджера
with open ('text.txt', 'w') as f:
  text = input("Enter your text: ")
  f.write(text)
print()
###################################################
k=0
with open('text.txt','r') as file:
  for line in file:
    k += 1
    if k == 2:
      print(line, end='')
      break
  for i in range(10):
###################################################
a = []
with open('text.txt','r') as file:
  for line in file:
    a.append(line)
print(a[2])
###################################################
with open ('image.jpeg', mode='rb'):
  with open ('new_image.jpeg', mode='wb') as new_file:
    data = file.read()
    new_file.write(str(data))
###################################################
#JSON текстовый формат обмена данными
#data.json
{
  "firstname":"Jane",
  "lasstname":"Doe",
  "age": 18,
  "city": "New-York",
  "married": false,
  "children": [
    {
      "firstname": "Annie",
      "lastname": "Doe"
    },
    {
      "firstname": "Mark",
      "lastname": "Doe"
    }
  ] 
}

# в другом файле

import json

with open('data.json', 'r') as f:
  data = json.loads(f.read())
# loads позволяет сделать экземпляр из текста  
print(data['lastname'])
#print(f"My name is {data['firstname']} {data['lastname']}, I'm {data['age']} years old.")
###################################################

import json

data = {
'Belasrus': 'Minsk',
'Poland': 'Warszawa',
'Japan': 'Tokyo'  
} 
with open ('data2.json', 'w'):
  temp = json.dumps(data, sort_keys=True, indent=4) #indent  кол-во отступов 
  f.write(temp)

###################################################

#CSV файлы
#data3.csv

Имя, Профессия, Год рождения
Вася, Токарь, 1993
Иван, Механик, 1978
Женя, Менеджер, 2000

# можно открыть в exel
###################################################
import csv

element = ['Даниил','ПРАГРАМИСТ','2018']
dictElement = {
  'Имя': 'Даниил,
  'Профессия': 'ПРАГРАМИСТ',
  'Год рождения': '2018'
}
fieldNames = ['Имя', 'Профессия','Год рождения']

with open("data3.csv",'a+', newline="\n") as csvFile:
  dataReader = csv.reader(csvFile, delimiter=",")
  dataWriter = csv.writer(csvFile, delimiter=",")

  dictReader = csv.DictReader(csvFile, fieldnames=fieldNames)
  dictWriter = csv.DictWriter(csvFile, fieldnames=fieldNames) # возможная запись в словари.
  for dictionary in dictReader:
    print(dictionary)
  #for row in dataReader:
    #print(",".join(row))
  #dataWriter.writerow(element)
  dictWriter.writerow(dictElement)
###################################################
import csv
with open ("classmates.csv", encoding='utf-8') as r_file:
  # Создаём объект reader, указываем символ-разделитель ","
  file_reader = csv.reader(r_file, delimiter = ",")
  # Счётчик для подсчёта количества строк и вывода заголовков столбцов
  count = 0
  # Считывание данных из CSV файла
  for row in file_reader:
    if count == 0:
      # Вывод строки, содержащей заголовки для столбцов
      print(f'Файл содержит столбцы: {",".join(row)}')
    else:
      # Вывод строк
      print(f'{row[0]} - {row[1]} и он родился в {row[2]} году.')
    count += 1
  print(f'Всего в файле {count} строк.')

###################################################

import openpyxl

# читаем excel-файл
wb = openpyxl.load_workbook('example.xlsx')

# печатаем список листов
sheets = wb.sheetnames
for sheet in sheets:
  print(sheet)

# получаем активный лист
sheet = wb.active

# печатаем значения ячейки А1
print(sheet['A1'].value)
# печатаем значение ячейки B1
print(sheet['B1'].value)
###################################################  
# Задание для самостоятельной работы

# Задача 1. 
# Декодировать в строку байтовое значение: b'r\xc3\xa9sum\xc3\xa9'. Затем результат преобразовать в байтовый вид в кодировке 'Latin1' и затем
# результат снова выводить в строку (результаты всех преобразований выводить на экран).

s = b'r\xc3\xa9sum\xc3\xa9'
s1 = s.decode("Latin1")
print (s1)
s2 = s1.encode("Latin1")
print (s2)
s3 = s2.decode("Latin1")
print (s3) 

###################################################  

# Задача 2.
# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные. Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать осставшиеся 2 строки. В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

s1 = input ("Input 1: ")+'\n'
s2 = input ("Input 2: ")+'\n'
s3 = input ("Input 3: ")+'\n'
s4 = input ("Input 4: ")+'\n'

f1 = open ('file1.txt','w')
f1.writelines([s1, s2])
f1. close ()

f1. open ('file1.txt', 'a', newline='\n')
f1.writelines([s3, s4])

###################################################  

# Задача 3.
# Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качетсве значений кортеж состоящий из 2-х элиментов - имя(str), возраст(int).
# Сделать около 5-6 элиментов словаря. Записать данный словарь на диск в json-файл.

###################################################  

# Задача 4.
# Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон".

###################################################  

# Задача 5.
# * Прочитать сохранённый csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими данными не нужен. Таблица должна выглядеть, как на примере табл (фото): 

###################################################  
  
  



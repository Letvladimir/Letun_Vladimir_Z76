def sumofTwoNum (a: float,b: float) -> float:
  """Return sum of two digits."""
  return a+b
result = sumofTwoNum(10,20)
print(result)
##################################################
def sumofTwoNum (a: float,b: float) -> float:
  """Return sum of two digits."""
  return a+b
result = sumofTwoNum(10,20)
print(sumofTwoNum.__doc__) #выведет что за комментарий атрибутом __doc__
##################################################
def powerUp(a: float) -> float: return a**2
print(powerUp(25))
##################################################
powerUp = lambda a: a**2
print(powerUp(25))
##################################################
def powerUp(a: float) -> float: return a**2
def superFunc(func,a): #сделаем функцию высшего порядка
  return func(a)
result = superFunc(powerUp, 25)
result2 = superFunc(lambda a: a:**2, 10)
print(result)
print(result2)
##################################################

# через def
def sumofTwoNum (a: float,b: float) -> float:
  """Return sum of two digits."""
  return a+b

def incrementList(a: float) ->:
   """Return sum of two digits."""
  return a*2

A = [i for i in range(10,20)]
B = []

result = list(map(incrementList, A)
print(A)
print(result)
##################################################

# через lambda и map
def sumofTwoNum (a: float,b: float) -> float:
  """Return sum of two digits."""
  return a+b

def incrementList(a: float) ->:
   """Return sum of two digits."""
  return a*2

A = [i for i in range(10,20)]      

result2 = list(map(lambda x: x**3, A))
print (result2)
##################################################

# через фильтр
def sumofTwoNum (a: float,b: float) -> float:
  """Return sum of two digits."""
  return a+b

def incrementList(a: float) ->:
   """Return sum of two digits."""
  return a*2

def filterList(a: float) -> bool:
  return a>=0

A = [i for i in range(10,20)]      
B = [i for i in range(-10,10)] 

result3 = list(filter(filterList, B))
print (result3)
##################################################

def sumofTwoNum (a: float,b: float) -> float:
  """Return sum of two digits."""
  return a+b

A = [i for i in range(10,20)]      
B = [i for i in range(-10,10)]   
  
# через reduce
from functools import reduce

result4 = reduce(sumOfTwoNum, A)
print(result4)
##################################################

#подитожем map, filter, reduce

result = map(lambda x: x**2,[1, 2, 3, 4, 5, 6])
print(list(reult))

result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(result))

from functools import reduce
result = reduce (lambda a, x: a + x**2, [1, 2, 3])
##################################################

def my_decorator(function_to_decorate):
  def main_block(x,y):
    print("Я сработаю до вызова функции")
    #function_to_decorate() # Сама декорируемая функция
    function_to_decorate(x,y) # Сама декорируемая функция
    print("Я сработаю после вызова функции")
  return main_block

@my_decorator
def hello():
  print("Cумма двух чисел равна {x+y}")
        
  
#@my_decorator
#def hello():
  #print("Hello world!")

#decorated_hello = my_decorator(Hello)
#decorated_hello()

Hello(10,20)
##################################################

# Задания для самостоятельной работы 
# Задача 1
# Написать лямбда-функцию определяющую чётное/нечётное. Функция принимает параметр (число) и если чётное, то выдаёт слово "чётное", если нет - то "нечётное".

def chetonst (a: int):
  return "Чётное" if a % 2 == 0 else "Нечётное"
# print(chetonst(3))
  print((lambda a:"Чётное" if a % 2 == 0 else "Нечётное")(3))
  
##################################################
  
# Задания для самостоятельной работы 
# Задача 2
#Дан список чисел. Вернуть список, где при помощи функции map() каждое число переведено в строку. В качестве функции в map используется lambda.
  
##################################################
  
# Задания для самостоятельной работы 
# Задача 3
# При помощи функции filter() из кортежа слов отфильтровать только те, которые являются полиндромами (которые читаются одинаково в обе стороны).
  
##################################################

  # Задания для самостоятельной работы 
# Задача 4
# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения. Подсказка from datetime import datetime  time = datetime.now()

from datetime import datetime

def time_decorator(function_to_decorate):
  def main_function():
    start = datetime.now()
    function_to_decatate()
    end = datetime.now()
    print(f"Функция завершилась за {round(end - start,2)} секунд.")
  return main_function

@time_decorator
def function1():
  time.sleep(1.5)

@time_decorator
def function2():
  time.sleep(2)

#function1()
function2()
#print(datetime.now())
##################################################
  
# Задания для самостоятельной работы 
# Задача 5**
# Сделать функцию которая на вход принимает строку. Анализирует её исключительно методом .isdigit() без доп.библиотек и переводит строку в число.Функция умеет распознавать отрицательные числа и десятичные дроби. 
# Пример: -6.7 -> вы ввели отрицательное дробное число: -6.7
# Пример: 5 -> вы ввели положительное целое число: 5
# Пример: 5.4r -> вы ввели не корректное число: 5.4r
# Пример: -.777 -> вы ввели отрицательное дробное число: -0.777


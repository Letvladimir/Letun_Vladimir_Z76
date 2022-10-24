a = 5 # or 5.5
print (type(a))

########################################################################################

class SomeClass:
# добавим поля, атрибуты
    attr1 = 22
    attr2 = "Hello"
    attr3 = True
# добавим методы
    def method1(self): # за счёт self метооду передаём экземпляр, нужен он для ссылки на объект из которого вызывается данный метод.
        print("Hello world!")
    
    def method2(self):
        print(self.attr1, self.attr2, self.attr3)

# создадим экземпляр данного класса
obj = SomeClass()
print(obj.attr1, obj.attr2, obj.attr3)
obj.method1() # либо метод пренад. экземп. класса этого или только классу или тем и тем 
obj.method2()
obj.attr1 = 0
obj.attr2 = 0
obj.attr3 = 0
obj.method2()

########################################################################################

# Опишем сотрудников с должностями и днями рождения

class Employee:
#     firstName = "Vasya"
#     lastName = "Vasilevich"
#     age = 30
#     dateOfBirth = "10-10-1990"
#     job = "Manager"
#     status = "Vacation"

    def __init__(self, firstName: str, lastName: str, age: str, dateOfBirth: str, job: str, status : str):
        self.firstName = firstName
        self

    def about(self):
        print(f"{self.firstName} {self.lastName}. Age {self.age} ({self.dateOfBirth}). Job: {self.job}")
    
    def changeStatus(self, status: str):
        self.status = status
        print ("Status has been changed.")

Vasya = Employee ("Mihail", "Fedorov", 25, "04-12-1996", "Sales manager", "Vacation")
# Vasya = Employee()
# Vasya.about()
# Vasya.changeStatus("Fired")
# print (Vasya.status)

#Наследование - позволяет наследовать атрибуты от других родительских классов

class Parent1:
  attr1 = 10
  attr2 = 20
  def method1(self):
    print(self.attr1, self.attr2)

class Parent2:
  attr3 =30 #атрибуты
  attr4 =40 #поле

  def method2(self):  #методы
    print(self.atr3, self.attr4)

class Child (Parent1,Parent2): #Child - дочерний класс #Parent - родительский
  attr5 = 50
  attr6 = 60
  
child = Child()
child.method1()
child.method2()

######################################################################

# Полиморфизм - представить объекты единой сущностью
class Cat:
  def info(self):
    print("Я кот")
  def make_sound(self):
    print ("Мииаууу")
    
class Dog:
  def info(self):
    print("Я собакен")
  def make_sound(self):
    print("ГГгггау")

cat = Cat()
dog = Dog()

house = (cat, dog)

for animal in house:  # вызвали одинаковый метод из сушности, когда разный результат от исходной сущности объекта
  animal.make_sound() 
  animal. info()
  animal.make_sound()

# полиморфизм функции 
data1 = "Sample text"
data2 = ["Sample text"]
data3 = {
  "text": "Sample text"
}
print(len(data1))
print(len(data2))
print(len(data3))

######################################################################

# Инкапсуляция - защита в атрибуты, делать их недоступными

class MyClass:
  __attr1 = 10
  def method1(self):
    print("Method 1 activated!")
  def _method2(self):
    print("Method 2 activated!")
  def __method3(self) :
    print("Method 3 activated!")
    
obj = MyClass()
obj.method1()
obj._method2()
obj._MyClass__method3()

######################################################################

# Абстракция - конструкторы позволяющие создавать последовательность из других последовательностей. 
from abc import ABC, abstractclassmethod

class ChessPiece(ABC):
  def draw(self):
    print("'Drew a chess piece')

  @abstractclassmethod
  def move(self):
    pass

class Horse(ChessPiece):
  color = "White"

  def move(self):
    print("'Побежал буквой Г'")

  def _str_(self):# Перегрузка операторов
    return "Это конь..."
    

horse = Horse()
# print(horse)
horse.move()

######################################################################

# MRO - method resolution order - порядок разрешения методов
# позволяет питону выяснить из какого класса предка нужна вызвать этот метод,
# если он не был обнаружен непосредственно в классе потомков 


######################################################################

# Задание для самостоятельной работы 
# Задание 1
# Создать родительский класс auto, у которого есть атрибуты: brand,age,color,mark и weight. 
# А так же методы: move, birthday и stop. Методы move и stop выводят сообщение на экран "move" и "stop", 
# а birthday увеличивает атрибут age на 1. 
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto:
    def __init__(self, brand, age, mark, color="white", weight=1500):
        self.brand = brand
        self.age = age
        self.color = color
        self.weight = weight
        self.mark = mark

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age = self.age + 1

exemple1 = Auto("adidas", 5, "passat", "red")

exemple1.move()


######################################################################

# Задание для самостоятельной работы 
# Задание 2
# Создать 2 класса truck и car, которые являются наследниками класса auto. Класс truck имеет дополнительный обязательный атрибут max_load. Переопределённый метод move, перед появлением надписи "move" выводит надпись "attention", его реализацию сделать при помощи оператора super. А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение "load" и снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move, после появления надписи "move" должна появиться надпись "max speed is <max_speed". Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.   

######################################################################

# Задание для самостоятельной работы 
# Задание 3
# *Для рассмотренного на уроке класса Circle реализовать метод производящий вычитаниедвух окружностей, вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением радиуса, то результатом вычитания будет точка класса Point.

######################################################################

# Задание для самостоятельной работы 
# Задание 4 
# Напишите программу с классом Student, в котором есть четыре атрибута: firstName, lastName, groupNumber и age. 
#Установить им любые значения по умолчанию. Необходимо создать пять методов: getFullName, getAge, getGroupNumber, setNameAge, setGroupNumber. 
# Метод getFullName нужен для получения данных об полном имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, метод GetGroupNumber нужен для получения данных о номере группы конкретного студента. 
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

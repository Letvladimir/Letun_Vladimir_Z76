from tokenize import Name


class MyClass:
    field1 = 100
    field2 = "Hello"

   # def __init__(self):

    def method(self):
        print("Method called")

    @staticmethod
    def method2():
        print("Static method called")

    @classmethod
    def method3(cls):
        cls.field1 = 0
        cls.field2 = ""
        print("Class method called")

    def about(self):
        print(f"Field1 = {self.field1}, Field2 = {self.field2}")

# A = MyClass()
# MyClass.method3()
# A.about()
# A.method()
# MyClass.method()

# A = MyClass()
# A.method2()
# MyClass.method2()

# MyClass.method3()

# A.about()
# A.method3()
# A.about()

######################################################

class NewClass:

    def __init__(self):
        self._x = "Hello"
        self.y = "World"
    # проперти можем контролировать все изменения

    x = property() #используется для определения свойств в классах 

    @x.getter
    def get_x(self): #отвечает за получение
        print ("Геттер сработал")
        return self._x
    
    @x.setter
    def set_x(self, value): # отвечает за изменение
        print("Сеттер сработал")
        self._x = value

    @x.deleter
    def del_x(self): # отвечает за удаление
        print ("Нельзя удалить!")
    
    @property
    def y(self):
        print("Геттер для Y сработал")
        return self._y

    @y.setter
    def y(self, value):
        print("Cеттер для Y сработал")
        self._y = value

    # x = property (get_x, set_x, del_x)


obj = NewClass()
x = obj.x
obj.x = 0
del obj.x
y = obj.y
# del obj.x 

# как работает делитер del
dictionary = {}
del dictionary
print (dictionary)

######################################################

# метакласс (класс класса)
class A:
    x = 0
    y = 0
a = A()
print(type(A))

class NewClass2:
    field1 = 0
    field2 = 0

    def method(self):
        print("Method")

data = {
    "name": "Name",
    "age": 20,
    "status": "Active"
}

User = type("User", (NewClass2,), data)
print(User)
new_user = User()
print(type(new_user)) 
print(new_user.field1)

# класс без методов если только поля доступные для экземпляров
class Book:
    def __init__(self, title, author, pageSize):
        self.title = title
        self.author = author
        self.pageSize = pageSize
        self.count = count

from dataclasses import dataclass 

@dataclass
class Newbook:
    title: str
    author: str
    pageSize: int

book1 = Book("Война и Мир","Лев Толстой", "90000")
book2 = Book("Война и Мир","Лев Толстой", "90000",50)

##############

from dataclasses import datclass
 

@dataclass
class BookData:
    title: str
    author: str
    pageSize: int
    count: int

class Book(BookData):
   
    def about(self):
        print(f"title: {self.title} .....")
    
    def decrement(self):
        self.count -= 1


book1 = Book("Война и Мир","Лев Толстой", "90000",50)
book1.about()
book1.decrement()

######################################################

#Задание для самостоятельной работы
#Задача 1 

# Написать программу с классом Product. 
# Представим, что это будет класс для любого товара в огромном супермаркете. 
# Добавить ему 3-4 любых атрибута, который есть у каждого товара в магазине. 
# Далее необходимо создать 2-3 класса, наследованных от Product (например Fruits, Vegetables и т.д). 
# Создать по одному экземпляру каждого класса.

from dataclasses import dataclass
@dataclass
class Product:
    price: float
    name: str
    weight: float
    amount: int

class Fruit(Product):
    def productInfo(self):
       print(f"Name : {self.name}, Price :{self.price}$ per unit")

    @property
    def totalPrice(self):
        return self.price * self.amount

    @property
    def totalWeight(self):
        return self.weight * self.amount


orange = Fruit(1,'orange',200,5)
orange.productInfo()
print(orange.totalPrice,orange.totalWeight)

######################################################

#Задание для самостоятельной работы
#Задача 2 

# Написать класс, который будет создавать треугольник по трём его сторонам. 
# В класс добавить метод, проверяющий возможность построения данного треугольника. 
# Добавить свойства треугольника (длины его сторон) с помощью @ property.


######################################################

#Задание для самостоятельной работы
#Задача 2 

# Написать программу, которая будет создавать класс данных из JSON объекта.
# (Дополнительно): Добавить метод для данного класса, который будет выводить все поля класса.

# Основы объектно-ориентированного программирования (ООП)

# Объекты обладают свойсвами и методами
# каждый объект принадлежит определенному классу (типу) или классам
# Класс - "чертеж" объекта.
# Конкретный реализованный объект называется экземпляр (инстанс) класса.

# Создание (определение) класса. Название принято писать с заглавной буквы.
class Cat:
    # метод-конструктор
    def __init__(self) -> None:
        # свойство (атрибут, поле)
        self.name = None
        self.color = None

    # метод (атрибут-метод) - функция, принадлежащая классу
    def meow(self):
        print("meow-meow")
        print(f"Name: {self.name}, color: {self.color}")

# создание объекта (экземпляра) на базе класса Cat
cat_1 = Cat()
cat_2 = Cat()

# запись данных в свойства
cat_1.name = "Tom"
cat_1.color = "white"

cat_2.name = "Jerry"
cat_2.color = "black"

# чтение данных из свойств
# print(cat_1.name)
# print(cat_2.name)

# вызов методов экземпляров
# cat_1.meow()
# cat_2.meow()


# Принцип ООП

# Принцип Наследования

# создание родительского (предкового) класса
class Animal:
    def __init__(self, legs):
        self.legs = legs

    def move(self):
        print("Я двигаюсь!")

# создание дочерних классов 
class Human(Animal):
    def __init__(self, name, legs):
        super().__init__(legs) # обращение к родителю с вызовом его метода
        self.name = name

    def speech(self):
        print(f"My name is {self.name}. Legs: {self.legs}")

class Cat_2(Animal):
    def __init__(self, name, legs, color):
        super().__init__(legs)
        self.name = name
        self.color = color

    def speech(self):
        print(f"My name is {self.name}. Legs: {self.legs}. Color: {self.color}")
    
    def meow(self):
        print("meow-meow")

# Создание объектов
bug = Animal(6)

man_1 = Human("John", 2)
women_1 = Human("Eva", 2)

cat_1 = Cat_2("Tom", 4, "Grey")
cat_2 = Cat_2("Jery", 4, "Yellow")


# использование объекта
bug.move()
print(bug.legs)

man_1.move()
man_1.speech()
women_1.move()
women_1.speech()

cat_1.move()
cat_1.speech()
cat_1.meow()
cat_2.move()
cat_2.speech()
cat_2.meow()
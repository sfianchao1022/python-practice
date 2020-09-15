# python is object oriented => class = method +variable
class Point():  # class的名稱第一個字要大寫
    def __init__(self, x, y):  # python的建構子constructor
        self.x = x
        self.y = y

    def move(self):  # pycharm會自動填入self
        print("move")

    def draw(self):
        print("draw")


point1 = Point(1, 2)
print(point1.x + point1.y)
point1.x = 10  # 可以直接在class外面定義variable
point1.y = 20
print(point1.x + point1.y)
point1.move()

class Person():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walk")

    def talk(self):
        print(f"Hi, I am {self.name}")


p1 = Person("Ian")
print(p1.name)
p1.talk()

# inheritance 繼承
class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    pass  # python不接受空的class 所以加一個pass讓python辨識


class Cat(Animal):
    def be_annoying(self):
        print("annoyinggggggggg")


dog1 = Dog()
cat1 = Cat()
dog1.walk()
cat1.walk()
cat1.be_annoying()


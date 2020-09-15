# google search "python 3 module index" "pypi"
import random  # 內建函式庫 位置：External Libraries/python3.8

# random
for i in range(3):
    print(random.random())  # default 0~1

for i in range(5):
    print(random.randint(4, 79))  # random 4~79 之間的整數

members = ["Mary", "Harry", "Mosh", "Ian", "John"]
print(random.choice(members))


class Dice:
    def __init__(self):
        pass

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # (first, second)不加小括弧 默認成tuple 唯讀的list


dice = Dice()
print(dice.roll())

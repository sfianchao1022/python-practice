#  function
def greet_user(first_name, last_name):  # 函式通常全部小寫 用底線連接
    print(f"{first_name} {last_name} is a programmer")


# 慣例函式與其他區塊之間間隔兩行
greet_user("Ian", "Chao")  # position arguement
greet_user(last_name="Wang", first_name="Mary")  # keyword arguement 不用管parameter的順序


def calculate_cost(total, shipping, discount):
    cost = (total + shipping) * discount
    print(cost)


calculate_cost(total=50, shipping=5, discount=0.9)  # make your code more readability


# square
def square(num):
    return num * num


def squ(number):
    print(number * number)


print(square(3))
print(squ(3))  # 若沒有return type會回傳none(object)


# converter
def kg_to_lbs(weight):
    return weight / 0.45


def lbs_to_kg(weight):
    return weight * 0.45


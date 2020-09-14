# handle error with Exceptions
try:
    age = int(input("age >"))
    income = 2000
    risk = income / age
    print(age)
except ValueError:  # 若輸入的值不是數字就會進入例外處理 程式不會error
    print("Invalid value")
except ZeroDivisionError:  # 終端機可以看到是什麼error
    print("can not divide zero")
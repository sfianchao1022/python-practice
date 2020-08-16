course = 'Python for "Beginners"'
course2 = "python's course for beginners"
email = '''
hi Ian,

this is the first email sent to you!

,best regards
'''
print(course)
print(course2)
print(email)

print("first character : "+course[0])  # 取得course字串index 0 的字元
print(course[0:3])  # 不包含index 3
anotherCourse = course[:]  # 取得course所有字元 等同於複製字串
print("same course : "+anotherCourse)
print(type(course[6]))
print(course[11])
print("last character : "+course[-1])  # 從開頭-1 回到字串最後一位字元
print(course[-3])
name = "jennifer"
print(name[1:-1])  # 從最後一個-1

firstName = 'Ian'
lastName = 'Chao'
# formatted Strings f'...{variable}...' 用大括弧包住變數可以直接寫在string內
print(firstName + ' [' + lastName + '] is a coder')
msg = f'{firstName} [{lastName}] is a coder'
print(msg)

courseName = 'python for beginners'
print(f'my course name is " {courseName} "')
print(type(len(courseName)))  # len()
print(len(courseName))
print(courseName.upper())  # upper()
print(courseName.lower())  # lower()

print(courseName.find('p'))  # find char 'p' at index 0
print(type(courseName.find('f')))
print(courseName.find('x'))  # can not find char 'x' in the string and return -1
print(courseName.find('beginners'))  # find 'beginners' start at index 11
print(courseName.replace('beginners', 'absolute beginners'))
print('python' in courseName)  # return boolean

# calculation
# import math -> python3 math module
print(10+4)
print(7-0.8)
print(10/3)  # float除法
print(10//3)  # integer除法
print(10*3)
print(10**3)  # 次方

print(round(3.2))  # round() 四捨五入
print(round(5.5))
print(round(5.4))
print(abs(-5.8))  # absolute 絕對值
print(abs(7.7))

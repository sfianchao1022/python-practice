# list類似array 使用中括號 可同時包含不同類型的元素
list_a = [3.14, 'Marry', 'John', 34, "台灣"]
print(list_a.index('John'))  # return list element index
print(50 in list_a)  # 50 not element in list, return boolean
print(list_a.pop())  # 最後一個進來的pop掉
list_a.append('Ian')  # 加在最後一個
list_a.insert(1, 'pi')  # insert(index, object)
list_a.remove(34)  # remove(object)
print(list_a[2])
print(list_a[-2])
print(list_a[2:4])  # 指到index 4的最前端 所以只包含到index 3
print(list_a[:])  # 使用[:]會return new list 所以會有中括號
list_a.clear()  # remove all element

numbers = [2, 5, 6, 2, 3, 7, 2, 9, 3]
print(numbers.count(2))  # count element 2 in the list
numbers.sort()  # sort() & reverse() no return type
numbers.reverse()
numbers2 = numbers.copy()  # numbers2 = numbers[:]
print(numbers2)

# tuple 唯讀的list
tup = (1, 3.14, 'orange')  # (wrong) tup[0] = 5 tuple無法被修改
print(tup[2])

# unpacking 開箱:將打包好的資料取出來 也適用於list
tup_a = (1, 2, 6, 'apple')
'''
簡化以下寫法 -> unpacking
a = tup_a[0]
b = tup_a[1]
c = tup_a[2]
d = tup_a[3]
'''
a, b, c, d = tup_a  # tuple 依序取出 element 存入變數中
print(d)

# python for loop 類似 java foreach 用法
for item in list_a:
    print(item)

# range()
for item in range(10):
    print(item)

for item in range(1, 10):
    print(item)

for item in range(1, 10, 2):  # print 1~10 公差2
    print(item)

prices = [30, 40, 50, 35, 99]
total = 0
for price in prices:
    total += price
print(f'Total : {total}')

# nested loop
for x in range(3):  # 3*3
    for y in range(3):
        print(f'({x},{y})')

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print('*' * x)

# nested loop
for i in numbers:
    output = ''
    for j in range(i):
        output += '*'
    print(output)

# find the Max number
'''print(max(num))'''
num = [3, 6, 10, 4, 7, 9]
max = num[0]
for temp in num:
    if temp > max:
        max = temp
print(max)

# 2D list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][2])  # 矩陣m*n m(向下延伸) -> outer list, n(向右延伸) -> inner list
for row in matrix:
    for item in row:
        print(item)

# remove duplicate numbers
nums = [2, 2, 4, 6, 3, 4, 6, 1]
new_num = []
for num in nums:
    if num not in new_num:
        new_num.append(num)
print(new_num)
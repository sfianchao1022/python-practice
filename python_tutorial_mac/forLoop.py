# list類似array 使用中括號 可同時包含不同類型的元素
list_a = [3.14, 'Marry', 'John', 34, "台灣"]

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
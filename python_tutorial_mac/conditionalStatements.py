# conditional statement
is_hot = False
is_Cold = False
if is_hot:
    print('It is a hot day')
    print('drink plenty of water')
elif is_Cold:  # elseif
    print('It is a cold day')
    print('wear warm clothes')
else:
    print('It is a lovely day')
print('enjoy your day')

has_high_income = True
has_good_credit = False
if has_good_credit and has_high_income:  # &&
    print('eligible for loan')
elif has_good_credit or has_high_income:  # ||
    print('OK for loan')
else:
    print('deny for loan')

name = 'Ian'
if len(name) < 3:
    print('name must be at least 8 characters.')
elif len(name) > 50:
    print('name must be a maximum of characters')
else:
    print('good name!')

# weight = int(input('weight ? : '))
# unit = input('(L)bs or (K)g ? : ')
# if unit.lower() == 'l':  # 全部轉成lower case
#     weight *= 0.45
#     print(f'you are {weight} kilograms')
# else:
#     weight /= 0.45
#     print(f'you are {weight} pounds')

# print * 1~10
print('print 1~10')
i = 1
while i <= 10:
    print('*' * i)
    i += 1  # python沒有i++
print('done')

# guess game
print('Guess game !')
secretNumber = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guessNumber = int(input('guess a number : '))
    if guessNumber == secretNumber:
        print('you win the game!')
        break  # 跳出while loop
    guessCount += 1
else:  # while後可以接else -> while 跑完以後要做的
    print('you lose!')
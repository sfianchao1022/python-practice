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
<<<<<<< HEAD
=======

weight = int(input('weight ? : '))
unit = input('(L)bs or (K)g ? : ')
if unit.lower() == 'l':  # 全部轉成lower case
    weight *= 0.45
    print(f'you are {weight} kilograms')
else:
    weight /= 0.45
    print(f'you are {weight} pounds')

# print * 1~10
print('print 1~10')
count = 1
while count <= 10:
    print('*' * count)
    count += 1  # python沒有i++
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

# car game
command = ''
started = False
while True:
    command = input('car game > ').lower()
    if command == 'start':
        # if判斷式內的變數為真(true)，就跑if 不用管原本變數是true or false
        if started:  # 等同於 if started == 'True'
            print('car already started')
        else:
            started = True
            print('car started')
    elif command == 'stop':
        # if判斷式內的變數不為真(not true)，就跑if 不用管原本變數是true or false
        if not started:  # 等同於 if started == 'False'
            print('car already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'quit':
        break
    elif command == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        help - get some help
        ''')
    else:
        print("sorry we don't understand your command")
>>>>>>> 22f5f8903c72e122f61118a20749a40ee666be27

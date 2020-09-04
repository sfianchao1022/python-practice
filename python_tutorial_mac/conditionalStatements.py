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

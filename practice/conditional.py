user_id = input('id?')
user_pw = input('pw?')

if user_id == 'hyeon01' or 'admin':
    if user_pw == '1234':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
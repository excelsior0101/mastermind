from mastermind_engine import gen_num, check_num

count = 0
while True:
    count += 1
    user_num = str(input('Введите чило: '))
    result = check_num(gen_num=gen_num, user_num=user_num)
    if result == True:
        print('Было потрачено', count, 'ходов.')
        quit = input('Хотите еще партию? yes/no: ')
        if quit == 'no':
            break
        else:
            count == 0

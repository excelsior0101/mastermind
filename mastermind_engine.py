import random

def generate_num():
    num = ''

    for i in range(4):
        while True:
            char = str(random.randint(0, 9))
            if char == '0' and i == 0:
                continue
            if char not in num:
                num += char
                break
    return num

def check_num(gen_num, user_num):
    bulls_cows = {
        'bulls': 0,
        'cows': 0
    }
    for char in user_num:
        if char in gen_num:
            if gen_num.index(char) == user_num.index(char):
                bulls_cows['bulls'] += 1
            else:
                bulls_cows['cows'] += 1
    print(bulls_cows)
    if bulls_cows['bulls'] == 4:
        return True

gen_num = generate_num()
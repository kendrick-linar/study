import random

def game(user):
    progress = True
    num = random.randint(1, 100)
    
    print('Попробуй угадай число от 1 до 100')
    
    while True:
        user_num = user
        if user_num != num:
            comparison(user_num, num)
        else:
            print('Поздравляю, вы выйграли!')
            break
                      
def user_input():    
    user = int(input('Ваше предположение: '))
    return user

def comparison(user_num, num):
    if user_num > num:
        print(f'{user_num} больше загаданного числа')
        user_input()
    elif user_num < num:
        print(f'{user_num} меньше загаданного числа')
        user_input()

file = open('game.log_2', 'w+')
user = user_input()
file.write(str(user))
game(user)
file.close
import random

def game():
    progress = True
    num = random.randint(1, 100)
    
    print('Попробуй угадай число от 1 до 100')
    

    while True:
        user_num = user_input()
        if user_num != num:
            comparison(user_num)
        else:
            print('Поздравляю, вы выйграли!)
            break
                

                
        
def user_input():    
    user = int(input('Ваше предположение: ')
    return user

def comparison(user_num):
    if user_num > num:
        print(f'{user_num} больше загаданного числа')
    elif user_num < num:
        print(f'{user_num} меньше загаданного числа')
        
            
    
    

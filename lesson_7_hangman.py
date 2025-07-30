def game():
    progress = True
    word = ['orange']
    lifes = 3
    word_in_play = get_word(word)
   
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))
    while progress:
        user_guess = input('Введите слово: ')    
        template = build_template(template, word_in_play, user_guess)   
        guessed = list_to_string_convert(template)
        print(f'Текущий результат: {guessed}')
        #print(f'debug: progress - {progress}')
        progress = check_win(guessed)
        #print(f'debug: progress - {progress}')

        if check_mistake(word_in_play, user_guess):
            lifes -= 1
            print(f'Осталось жизней {lifes}')           
        #print(f'debug: progress - {progress}')
        if lifes == 0:
            print('Игра окончена!')
            break

def welcome_speech(t):
    #print(f'Debug welcome_speech: t - {t}')
    num_t = '_' * len(t)
    #print(f'Debug welcome_speech: t - {t}')
    #print(f'Добро пожаловать в игру, у вас слово состоящее из {len(t)} букв {num_t}')

def get_word(w):
    #print(f'Debug get_word: w - {w}')
    return w[0]
    

def start_template(w):
    #print(f'Debug start_template: w -{w}')
    quantity = len(w)
    t = []
    for _ in range(quantity):
        t.append('_')   
    return t
    

def list_to_string_convert(t):
    #print(f'Debug list_to_string: t - {t}')
    word = ''
    for i in t:
        word += i
    #print(f'Debug list_to_string: word - {word}')               
    return word

def build_template(t, w, g=' '):
    #print(f'Debug build_template: t - {t}, w - {w}, g - {g}')
    new_template = t
    for i in range(len(w)):
        if w[i] == g:            
            new_template[i] = g 
    #print(f'Debug build_template: t - {t}, w - {w}, g - {g}')                            
    return t

def check_win(g):
    #print(f'debug check_win: g - {g}')
    progress = True
    count = 0
    for i in g:
        #print(f'debug check_win: i - {i}')
        if i == '_':
            count += 1
    if count == 0:
        print('Вы выйграли!')
        progress = False
    return progress

def check_mistake(w, g):
    #print(f'debug check_mistake:  ,w - {w}, g - {g}')
    return '_' not in g

game()

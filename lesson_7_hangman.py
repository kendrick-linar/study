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
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            print(f'Осталось жизней {lifes}')
            lifes -= 1

        if lifes == 0:
            break

def welcome_speech(t):
    num_t = '_' * len(t)
    print(f'Добро пожаловать в игру, у вас слово состоящее из {len(t)} букв {num_t}')

def get_word(w):
    return w[0]

def start_template(w):
    quantity = len(w)
    t = []
    for _ in range(quantity):
        t.append('_')
    return t

def list_to_string_convert(t):
    word = ''
    for i in t:
        word += i        
    return word

def build_template(t, w, g=' '):
    new_template = t
    for i in range(len(w)):
        if w[i] == g:            
            new_template[i] = g               
    return t

def check_win(g):
    progress = True
    count = 0
    for i in g:
        if i == '_':
            count += 1
    if count > 0:
        progress = False
    return progress

def check_mistake(w, g):
    return '_' not in g

game()
        
	







    
    

def game():
    progress = True
    word = ['orange']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

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

print(list_to_string_convert(['_']))



    
    

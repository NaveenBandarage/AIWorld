with open('newfile.txt', 'r') as file:
    text = file.read().lower()
print('text length', len(text))
chars = sorted(list(set(text))) # getting all unique chars
print('total chars: ', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

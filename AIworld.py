from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import io
# needed this https://stackoverflow.com/questions/48720833/could-not-find-a-version-that-satisfies-the-requirement-tensorflow
path = 'newfile.txt'
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower()
print('Length of text:', len(text))

#sorts all the characters in a unique list so by the time its run it basically like has all the alphabet
chars = sorted(list(set(text)))
print('Total number of chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))


# source ./venv/bin/activate - THIS IS THE COMMAND TO ACTIVATE VIRTUAL ENVIRONMETN
# divides the text into sequences of 40 characters or 40 character chunks. 
maxlen = 40
step = 3
sentencesArray = []
nextChars = []
for i in range(0, len(text) - maxlen, step):
    sentencesArray.append(text[i: i + maxlen])
    nextChars.append(text[i + maxlen])
print('Sequences:', len(sentencesArray))

#turning these 40 character chunks into vectors/matrices for input and output
print('Now turning into vectors')
# Getting the x
x = np.zeros((len(sentencesArray), maxlen, len(chars)), dtype=np.bool)
# Getting the y
y = np.zeros((len(sentencesArray), len(chars)), dtype=np.bool)

# Now that we have sentence arrays we are converting these into numbers (one hot vectorisation)
for i, sentence in enumerate(sentencesArray):
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[nextChars[i]]] = 1


# Creating a model from single lstm.
print('Build model...')
# Taken from tensorflow and github
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars), activation='softmax'))
optimizer = RMSprop(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


def sample(preds, temperature=1.0):
    # This helps with sampling.
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def on_epoch_end(epoch, _):
    # Function invoked at end of each epoch. Prints generated text.
    print()
    print('----- Generating text after Epoch: %d' % epoch)
    #Random starting index with the diversity set 
    start_index = random.randint(0, len(text) - maxlen - 1)
    for diversity in [0.2, 0.5]:
        print('----- diversity:', diversity)

        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(400):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()


#Generating the output based on what we have written
def generate_output():
    generated = ''

    usr_input = input("Write your Travis Scott Lyrics Here: ")
    sentence = ('{0:0>' + str(Tx) + '}').format(usr_input).lower()
    generated += usr_input

    sys.stdout.write("\n\nHere is your verse: \n\n")
    sys.stdout.write(usr_input)
    for i in range(400):

        x_pred = np.zeros((1, Tx, len(chars)))

        for t, char in enumerate(sentence):
            if char != '0':
                x_pred[0, t, char_indices[char]] = 1.

        preds = model.predict(x_pred, verbose=0)[0]
        next_index = sample(preds, temperature=0.2)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()

        if next_char == '\n':
            continue


print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x, y,
          batch_size=128,
          epochs=30,
          callbacks=[print_callback])

Tx = 40
while True:
    userInput = input('\nDo you want to keep generating (Y/N): \n')
    if (userInput == 'N'):
        print("Travis scott generator closing down.")
        break
    generate_output()

#!/usr/bin/python3

from keras.utils.np_utils import to_categorical
from keras.datasets import reuters
from keras import models
from keras import layers
import numpy as np
import matplotlib.pyplot as plt

def vectorize_sequences(sequences, dimension = 10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

def classify_reuters():
    (train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

    '''
    f = np.load('./imdb.npz')
    train_data, train_labels = f['x_train'][:10000], f['y_train'][:10000]
    test_data, test_labels   = f['x_test'][:10000], f['y_test'][:10000]
    f.close()
    '''

    # print(test_data.shape)
    x_train = vectorize_sequences(train_data)
    x_test  = vectorize_sequences(test_data)

    y_train = to_categorical(train_labels)
    y_test  = to_categorical(test_labels)

    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(46, activation='softmax'))

    x_val = x_train[:1000]
    partial_x_train = x_train[1000:]

    y_val = y_train[:1000]
    partial_y_train = y_train[1000:]

    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(partial_x_train,
                        partial_y_train,
                        epochs=20,
                        batch_size=512,
                        validation_data = (x_val, y_val))

    plot(history)


def plot(history):
    history_dict = history.history
    loss_values  = history_dict['loss']
    val_loss_values = history_dict['val_loss']

    epochs = range(1, len(loss_values) + 1)

    plt.plot(epochs, loss_values, 'bo', label='Training loss')
    plt.plot(epochs, val_loss_values, 'b', label = 'validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()



################################################################################

if __name__ == '__main__':
    classify_reuters()

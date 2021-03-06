#!/usr/bin/python3

from keras.datasets import mnist
import numpy as np

''''
f = np.load('./mnist.npz')
train_images, train_labels = f['x_train'], f['y_train']
test_images, test_labels   = f['x_test'], f['y_test']
f.close()
'''

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# print(train_images.shape)
# print(len(train_labels))

from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (28, 28, 1)))
network.add(layers.MaxPooling2D((2, 2)))
network.add(layers.Conv2D(64, (3, 3), activation = 'relu'))
network.add(layers.MaxPooling2D((2,2)))
network.add(layers.Conv2D(64, (3,3), activation = 'relu'))

print(network.summary())

network.add(layers.Flatten())
network.add(layers.Dense(64, activation = 'relu'))
network.add(layers.Dense(10, activation = 'softmax'))

print(network.summary())

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000, 28, 28, 1))


from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels  = to_categorical(test_labels)

network.compile(optimizer = 'rmsprop',
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])

network.fit(train_images, train_labels, epochs = 5, batch_size = 64)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print(test_loss, test_acc)


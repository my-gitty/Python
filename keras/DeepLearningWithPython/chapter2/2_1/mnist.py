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
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

train_images = np.reshape(train_images, (60000, 28 * 28))
train_images = train_images.astype('float32')/255

print(type(train_images))
print(train_images.shape)

test_images = test_images.reshape((10000, 28 * 28))


from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels  = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=10, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print(test_loss, test_acc)

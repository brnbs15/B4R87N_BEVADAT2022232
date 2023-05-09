import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow import keras
from typing import Tuple



def mnist_digit_data():
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    train_images = train_images / 255
    train_labels = train_labels / 255
    return train_images, train_labels,test_images, test_labels

def mnist_model() -> keras.Sequential:
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])
    return model

def model_compile(model : keras.Sequential) -> keras.Sequential:
    model.compile(optimizer='adam',
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])
    return model


def model_fit(model:keras.Sequential,epochs, train_images, train_labels)-> keras.Sequential:
    model.fit(train_images, train_labels, epochs)
    return model


def model_evaluate(model: keras.Sequential, test_images, test_labels) -> Tuple[float , float]:
    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    return test_loss,test_acc
import tensorflow as tf
import numpy as np
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def cifar100_data():
    (train_images, train_labels), (test_images,test_labels) = tf.keras.datasets.cifar100.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    return train_images, train_labels, test_images, test_labels

def cifar100_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(100, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(100, activation='softmax')
    ])

    return model

def model_compile(model):
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False)
    model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])
    return model

def model_fit(model, epochs, train_images, train_labels):
    model.fit(train_images, train_labels, epochs=epochs, verbose=1)
    return model

def model_evaluate(model, test_images, test_labels):
    results = model.evaluate(test_images, test_labels, verbose=0)
    test_loss, test_acc = results[0], results[1]
    return test_loss, test_acc
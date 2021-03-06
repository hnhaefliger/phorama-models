import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D
import numpy as np

class PhoramaFeatures:
    def __init__(self, load_path):
        inputs = Input(shape=(None, None, 3))
        inner = inputs

        inner = Conv2D(3, (3,3), padding='same', activation='sigmoid')(inner)

        self.model = Model(inputs=inputs, outputs=inner)
        self.model.compile(loss='mse', optimizer='Adam')

    def predict(self, data):
        return self.model.predict(data)

    def train_on_batch(self, x, y):
        return self.model.train_on_batch(x, y)

    def setTrainable(self, trainable):
        self.model.trainable = trainable

    def __call__(self, x):
        return self.model(x)

    def save(self, path):
        return self.model.save(path)


    

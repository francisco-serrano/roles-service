import numpy as np
from keras.models import load_model


class RolesNeuralNet:
    def __init__(self, h5_file):
        self.classifier = load_model(h5_file)

    def make_prediction(self, ipa_array_text):
        ipa_array = np.array(ipa_array_text.split(','), dtype=int)

        prediction = self.classifier.predict(np.reshape(ipa_array, (1, 12)))
        prediction = np.argmax(prediction) + 1

        return str(prediction)

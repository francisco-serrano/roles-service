import numpy as np
from keras.models import load_model


class RolesNeuralNet:
    def __init__(self, h5_file):
        self.classifier = load_model(h5_file)

    def make_prediction(self, ipa_arrays_text):

        def make_single_prediction(x):
            ipa_array = np.array(x.split(','), dtype=int)

            return np.reshape(self.classifier.predict(np.reshape(ipa_array, (1, 12))), (9,)).tolist()

        predictions = list(map(lambda x: make_single_prediction(x), ipa_arrays_text.split(';')))

        return predictions

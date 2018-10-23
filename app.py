from flask import Flask, request, Response
from model import RolesNeuralNet

app = Flask(__name__)
neural_net = RolesNeuralNet('model.h5')


@app.route('/obtener_roles', methods=['GET'])
def classify_ipa():
    ipa_arrays_text = request.args.get('ipa_arrays')

    prediction = neural_net.make_prediction(ipa_arrays_text)

    return Response(str(prediction), mimetype='text/plain')


if __name__ == '__main__':
    app.run()

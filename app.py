from flask import Flask, request, Response
from model import RolesNeuralNet

app = Flask(__name__)
neural_net = RolesNeuralNet('model.h5')


@app.route('/obtener_roles', methods=['GET'])
def classify_ipa():
    ipa_array_text = request.args.get('ipa_array')

    return Response(neural_net.make_prediction(ipa_array_text), mimetype='text/plain')


if __name__ == '__main__':
    app.run()

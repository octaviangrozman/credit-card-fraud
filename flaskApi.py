from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
import json

import RandomForest

app = Flask(__name__)

RandomForestClassifier = RandomForest.RandomForest()

@app.route('/predictFraud', methods=['POST'])
def predict_fraud():
    input_data = request.get_json()
    if u"features" not in input_data:
        return json.dumps({u"error": u"No features found in input"}), 400
    if not input_data[u"features"] or not isinstance(input_data[u"features"], list):
        return json.dumps({u"error": u"No feature values available"}), 400
    if isinstance(input_data[u"features"][0], list):
        results = RandomForestClassifier.checkIfFraud(input_data[u"features"]).tolist()
    else:
        results = RandomForestClassifier.checkIfFraud([input_data[u"features"]]).tolist()
    return jsonify(results), 200



if __name__ == '__main__':
    app.run(debug=True)
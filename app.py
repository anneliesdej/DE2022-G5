from flask import Flask, request

from heartattack_predictor import HeartAttackPredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/heartattack_predictor/', methods=['POST']) 
def predict_str():
    prediction_inout = request.get_json()
    return hap.predict_single_record(prediction_inout)


hap = HeartAttackPredictor()
app.run(host='0.0.0.0', port=5000)
# importing Flask and other modules
import json
import os

import requests
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/predict_heartattack', methods=["GET", "POST"])
def predict_heartattack():
    if request.method == "POST":
        prediction_input = [
            {
                "exng": int(request.form.get("exng")),
                "caa": int(request.form.get("caa")),
                "cp": int(request.form.get("cp")),
                "fbs": int(request.form.get("fbs")),
                "restecg": int(request.form.get("restecg")),
                "slp": int(request.form.get("slp")),
                "thall": int(request.form.get("thall")),
                "trtbps": float(request.form.get("trtbps")),
                "chol": float(request.form.get("chol")),
                "thallachh": float(request.form.get("thallachh")),
                "oldpeak": float(request.form.get("oldpeak")),
                "age": int(request.form.get("age"))
            }
        ]
        print(prediction_input)
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        predictor_api_url = os.environ['PREDICTOR_API']
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

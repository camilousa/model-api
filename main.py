import boto3
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

s3 = boto3.resource('s3')
s3.meta.client.download_file('german-credit-255423', 'model/model.joblib', 'model.joblib')
model = joblib.load("model.joblib")

@app.route("/")
def index():
    return "Hi Flask"


@app.route("/predict", methods=["POST"])
def predict():
    request_data = request.get_json()
    print("request_data")
    age = request_data["age"]
    sex = request_data["sex"]
    credit_amount = request_data["credit_amount"]
    duration = request_data["duration"]
    purpose = request_data["purpose"]
    housing = request_data["housing"]
    prediction = model.predict([[age, credit_amount, duration, sex, purpose, housing]])
    return jsonify({"prediction": prediction.tolist()})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    app.run()


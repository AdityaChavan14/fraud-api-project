from flask import Flask, request, jsonify
import joblib
import numpy as np

#create flask app
app = Flask(__name__)

#load trained model
model = joblib.load("fraud_detection_model.pkl")


#home endpoint
@app.route("/")
def home():
    return "Fraud detection API is running"

#Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
	try:
        #get JSON data
		data = request.get_json()

	#convert dictionary to list
		features = list(data.values())

	#convert to numpy array
		final_input = np.array(features).reshape(1,-1)

	#predict
		prediction = model.predict(final_input)[0]

	#return json response
		return jsonify({"prediction": int(prediction)})

	except Exception as e:
		return jsonify({"error":str(e)})


import os
if __name__ =="__main__":
    port = int(os.environ.get("PORT",5000))	
    app.run(host="0.0.0.0", port=port)




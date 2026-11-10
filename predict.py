import pickle
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model and DictVectorizer
model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Initialize Flask app
app = Flask('insurance_predict')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get the patient/customer data from the POST request in JSON format
    customer = request.get_json()

    # 2. Transform the data using DictVectorizer
    X = dv.transform([customer])

    # 3. Make the prediction (this outputs a log-transformed value)
    y_pred_log = model.predict(X)[0]

    # 4. Convert the prediction back to exact dollars using expm1
    y_pred_dollars = np.expm1(y_pred_log)

    # 5. Format the output
    result = {
        'estimated_medical_cost': round(float(y_pred_dollars), 2)
    }

    return jsonify(result)

if __name__ == "__main__":
    # Run the app on local host, port 9696
    app.run(debug=True, host='0.0.0.0', port=9696)
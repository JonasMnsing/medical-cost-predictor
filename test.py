import requests

# url = 'http://localhost:9696/predict'
url = 'https://medical-cost-predictor-quk0.onrender.com/predict'

# A sample high-risk profile (smoker with high BMI)
customer = {
    "age": 30,
    "sex": "male",
    "bmi": 35.5,
    "children": 1,
    "smoker": "yes",
    "region": "southwest"
}

print("Sending request to the cloud...")
print("Note: If the server has been inactive for 15 minutes, this may take ~50 seconds to wake up.")

response = requests.post(url, json=customer).json()
print(response)
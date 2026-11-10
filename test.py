import requests

url = 'http://localhost:9696/predict'

# A sample high-risk profile (smoker with high BMI)
customer = {
    "age": 30,
    "sex": "male",
    "bmi": 35.5,
    "children": 1,
    "smoker": "yes",
    "region": "southwest"
}

response = requests.post(url, json=customer).json()
print(response)
# Model serving tutorial

Deployment instructions:

1. Install virtualenv: `pip install virtualenv`

2. Create the new environment: `python3 -m venv env`

3. Activate the environment: `source env/bin/activate`

4. Install the dependencies: `pip install -r requirements.txt`

5. Start the server: `uvicorn main:app --reload`

6. Testing the service using a tool like Postman:

```
POST /predict HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

[
  {
    "customerID": "7703-ZEKEF",
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "No",
    "tenure": 23,
    "PhoneService": "Yes",
    "MultipleLines": "Yes",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "Yes",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 81,
    "TotalCharges": 1917.1
  }
]
```